"""Peek-it [HA] integration setup with log forwarding and TTS services."""
from __future__ import annotations

import asyncio
import logging
import secrets

from aiohttp.web import Request, Response
from homeassistant.components import network, webhook
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, ServiceCall, SupportsResponse
from homeassistant.helpers import device_registry as dr, issue_registry as ir

from .const import (
    CONF_API_KEY,
    CONF_IP_ADDRESS,
    CONF_NAME,
    CONF_PORT,
    CONF_WEBHOOK_SECRET,
    DEFAULT_PORT,
    DOMAIN,
    ISSUE_ANDROIDTV_MISSING,
    WEBHOOK_ID,
    WEBHOOK_SECRET_HEADER,
)
from .coordinator import PeekItCoordinator
from .http import async_get_json, async_post_json
from .payload import build_notify_payload, build_tts_payload

PLATFORMS = ["binary_sensor", "notify", "button"]

_LOGGER = logging.getLogger(__name__)

_WEBHOOK_REGISTERED_KEY = "_webhook_registered"


def _ensure_webhook_secret(hass: HomeAssistant, entry: ConfigEntry) -> str:
    """Return the entry's webhook secret, generating one if missing (migration)."""
    secret = entry.data.get(CONF_WEBHOOK_SECRET)
    if secret:
        return secret
    secret = secrets.token_urlsafe(32)
    new_data = {**entry.data, CONF_WEBHOOK_SECRET: secret}
    hass.config_entries.async_update_entry(entry, data=new_data)
    _LOGGER.warning(
        "Peek-it [HA]: generated a new webhook secret for entry '%s'. "
        "Re-open the integration options and resave so the TV picks up "
        "the new X-Peek-Secret value.",
        entry.title,
    )
    return secret


def _iter_coordinators(hass: HomeAssistant):
    """Yield every PeekItCoordinator currently stored in hass.data."""
    for value in hass.data.get(DOMAIN, {}).values():
        if isinstance(value, PeekItCoordinator):
            yield value


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up the integration."""
    hass.data.setdefault(DOMAIN, {})

    # Migration: every entry must carry a webhook secret.
    _ensure_webhook_secret(hass, entry)

    coordinator = PeekItCoordinator(
        hass,
        ip=entry.data[CONF_IP_ADDRESS],
        port=entry.data.get(CONF_PORT, DEFAULT_PORT),
        api_key=entry.data.get(CONF_API_KEY, ""),
        name=entry.data.get(CONF_NAME, "peek-it"),
    )
    # Do not block setup on first refresh — the TV may be offline.
    await coordinator.async_refresh()
    hass.data[DOMAIN][entry.entry_id] = coordinator

    # 1. Register webhook (once for the whole integration — all entries share it)
    if not hass.data[DOMAIN].get(_WEBHOOK_REGISTERED_KEY):
        webhook.async_register(
            hass,
            DOMAIN,
            "Peek-it Debug Listener",
            WEBHOOK_ID,
            handle_webhook_log,
        )
        hass.data[DOMAIN][_WEBHOOK_REGISTERED_KEY] = True

    # 2. Register services (once only)
    if not hass.services.has_service(DOMAIN, "get_templates"):
        hass.services.async_register(
            DOMAIN,
            "get_templates",
            async_get_templates,
            supports_response=SupportsResponse.ONLY,
        )
    if not hass.services.has_service(DOMAIN, "notify"):
        hass.services.async_register(DOMAIN, "notify", async_notify)
    if not hass.services.has_service(DOMAIN, "tts"):
        hass.services.async_register(DOMAIN, "tts", async_tts)
    if not hass.services.has_service(DOMAIN, "tts_stop"):
        hass.services.async_register(DOMAIN, "tts_stop", async_tts_stop)

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    # Repair issue: signale (sans bloquer) que l'intégration Android TV
    # est recommandée pour les boutons ADB.
    if not hass.config_entries.async_entries("androidtv"):
        ir.async_create_issue(
            hass,
            DOMAIN,
            ISSUE_ANDROIDTV_MISSING,
            is_fixable=False,
            severity=ir.IssueSeverity.WARNING,
            translation_key=ISSUE_ANDROIDTV_MISSING,
        )
    else:
        ir.async_delete_issue(hass, DOMAIN, ISSUE_ANDROIDTV_MISSING)

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id, None)
        # Tear down shared resources only when the last entry leaves.
        remaining = [k for k in hass.data[DOMAIN] if k != _WEBHOOK_REGISTERED_KEY]
        if not remaining:
            if hass.data[DOMAIN].pop(_WEBHOOK_REGISTERED_KEY, False):
                webhook.async_unregister(hass, WEBHOOK_ID)
            hass.services.async_remove(DOMAIN, "get_templates")
            hass.services.async_remove(DOMAIN, "notify")
            hass.services.async_remove(DOMAIN, "tts")
            hass.services.async_remove(DOMAIN, "tts_stop")
    return unload_ok


async def _resolve_ha_ip(hass: HomeAssistant, target_ip: str) -> str:
    """Best-effort source IP for the TV to call back."""
    try:
        return await network.async_get_source_ip(hass, target_ip=target_ip)
    except Exception:  # noqa: BLE001 — network lookup is best-effort
        return "127.0.0.1"


def _common_headers(api_key: str) -> dict[str, str]:
    return {"X-API-Key": api_key} if api_key else {}


def _select_coordinators(
    hass: HomeAssistant, target: str | list[str] | None
) -> list[PeekItCoordinator]:
    """Résout un ``target`` optionnel vers les coordinators correspondants.

    ``target`` accepte un device_id Home Assistant, un nom de device ou une
    IP (str ou liste). Falsy → toutes les TV configurées (broadcast, le
    comportement historique, donc rétrocompatible).
    """
    coordinators = list(_iter_coordinators(hass))
    if not target:
        return coordinators

    wanted = {target} if isinstance(target, str) else set(target)
    dev_reg = dr.async_get(hass)
    selected: list[PeekItCoordinator] = []
    for coord in coordinators:
        ids = {coord.ip, coord.device_name}
        device = dev_reg.async_get_device(identifiers={(DOMAIN, coord.ip)})
        if device is not None:
            ids.add(device.id)
            if device.name:
                ids.add(device.name)
            if device.name_by_user:
                ids.add(device.name_by_user)
        if ids & wanted:
            selected.append(coord)

    if not selected:
        _LOGGER.warning(
            "Peek-it: aucune TV configurée ne correspond à target %s — rien envoyé",
            target,
        )
    return selected


def _online_targets(
    coordinators: list[PeekItCoordinator], context: str
) -> list[PeekItCoordinator]:
    """Écarte les TV hors ligne (fail-fast) et renvoie celles en ligne.

    S'appuie sur ``coordinator.is_online`` (déjà calculé par le poll
    ``/api/status`` qui pilote le binary_sensor de statut) pour ne pas
    bloquer l'appel de service sur une TV éteinte (~19 s de retries).
    """
    online = [c for c in coordinators if c.is_online]
    skipped = [c.device_name for c in coordinators if not c.is_online]
    if skipped:
        _LOGGER.info(
            "Peek-it: TV hors ligne ignorée(s) pour %s : %s",
            context, ", ".join(skipped),
        )
    return online


async def _notify_one(
    hass: HomeAssistant, coord: PeekItCoordinator, call_data: dict
) -> None:
    ha_ip = await _resolve_ha_ip(hass, coord.ip)
    payload = build_notify_payload(
        call_data,
        str(ha_ip),
        message=call_data.get("message"),
        title=call_data.get("title"),
    )
    await async_post_json(
        hass,
        f"http://{coord.ip}:{coord.port}/api/notify",
        payload,
        headers=_common_headers(coord.api_key),
        context=f"notify {coord.device_name}",
    )


async def _tts_one(
    hass: HomeAssistant, coord: PeekItCoordinator, call_data: dict
) -> None:
    await async_post_json(
        hass,
        f"http://{coord.ip}:{coord.port}/api/tts",
        build_tts_payload(call_data),
        headers=_common_headers(coord.api_key),
        context=f"tts {coord.device_name}",
    )


async def _tts_stop_one(hass: HomeAssistant, coord: PeekItCoordinator) -> None:
    await async_post_json(
        hass,
        f"http://{coord.ip}:{coord.port}/api/tts/stop",
        {},
        headers=_common_headers(coord.api_key),
        context=f"tts_stop {coord.device_name}",
    )


async def async_notify(call: ServiceCall) -> None:
    """Envoie une notification — à toutes les TV, ou à ``target`` si fourni.

    Le fan-out est concurrent (``asyncio.gather``) : le coût total est celui
    de la TV la plus lente, plus la somme. Les TV hors ligne sont écartées.
    """
    hass = call.hass
    call_data = dict(call.data)
    coords = _online_targets(
        _select_coordinators(hass, call_data.pop("target", None)), "notify"
    )
    if not coords:
        return
    await asyncio.gather(
        *(_notify_one(hass, c, call_data) for c in coords),
        return_exceptions=True,
    )


async def async_tts(call: ServiceCall) -> None:
    """Envoie un TTS — à toutes les TV, ou à ``target`` si fourni."""
    hass = call.hass
    call_data = dict(call.data)
    coords = _online_targets(
        _select_coordinators(hass, call_data.pop("target", None)), "tts"
    )
    if not coords:
        return
    await asyncio.gather(
        *(_tts_one(hass, c, call_data) for c in coords),
        return_exceptions=True,
    )


async def async_tts_stop(call: ServiceCall) -> None:
    """Arrête le TTS — sur toutes les TV, ou sur ``target`` si fourni."""
    hass = call.hass
    call_data = dict(call.data)
    coords = _online_targets(
        _select_coordinators(hass, call_data.pop("target", None)), "tts_stop"
    )
    if not coords:
        return
    await asyncio.gather(
        *(_tts_stop_one(hass, c) for c in coords),
        return_exceptions=True,
    )


async def async_get_templates(call: ServiceCall) -> dict:
    """Retrieve the template list from all configured devices."""
    hass = call.hass
    result: dict = {}

    for coord in _iter_coordinators(hass):
        url = f"http://{coord.ip}:{coord.port}/api/templates/list"
        status, data = await async_get_json(
            hass,
            url,
            headers=_common_headers(coord.api_key),
            context=f"templates {coord.device_name}",
        )
        if status == 200 and data is not None:
            result[coord.device_name] = data
        elif status is None:
            result[coord.device_name] = {"error": "Connection failed"}
        else:
            result[coord.device_name] = {"error": f"HTTP {status}"}

    return result


def _valid_webhook_secret(hass: HomeAssistant, presented_secret: str | None) -> bool:
    """Return True iff the presented secret matches at least one configured entry."""
    if not presented_secret:
        return False
    for entry in hass.config_entries.async_entries(DOMAIN):
        expected = entry.data.get(CONF_WEBHOOK_SECRET)
        if expected and secrets.compare_digest(expected, presented_secret):
            return True
    return False


async def handle_webhook_log(hass: HomeAssistant, webhook_id: str, request: Request) -> Response:
    """Handle incoming logs and button actions from the TV.

    Requires a valid ``X-Peek-Secret`` header. Without it the request is
    rejected with HTTP 401 so a LAN attacker cannot fire fake
    ``peekit_button_press`` events.
    """
    presented = request.headers.get(WEBHOOK_SECRET_HEADER)
    if not _valid_webhook_secret(hass, presented):
        _LOGGER.warning(
            "Peek-it webhook rejected: missing or invalid %s header from %s",
            WEBHOOK_SECRET_HEADER,
            request.remote,
        )
        return Response(status=401, text="Unauthorized")

    try:
        data = await request.json()
        level = data.get("level", "INFO")
        message = data.get("message", "No message")

        if level == "ACTION" and message.startswith("BUTTON_CLICK:"):
            action_id = message.replace("BUTTON_CLICK:", "")
            hass.bus.async_fire("peekit_button_press", {"action": action_id})
            _LOGGER.info("[PEEK-IT] Button pressed: %s", action_id)
            return Response(text="Action received")

        log_msg = f"[PEEK-IT REPORT] {message}"

        if level == "ERROR":
            _LOGGER.error(log_msg)
        elif level == "WARN":
            _LOGGER.warning(log_msg)
        else:
            _LOGGER.info(log_msg)

    except Exception as e:  # noqa: BLE001
        _LOGGER.error("Webhook receive error peek-it: %s", e)

    return Response(text="Log received")
