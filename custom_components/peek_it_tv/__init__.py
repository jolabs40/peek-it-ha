"""Initialisation de l'intégration peek-it TV avec gestion des logs retour."""
import logging
import aiohttp
from aiohttp.web import Request, Response
from homeassistant.components import webhook, network
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, ServiceCall, SupportsResponse
from .const import DOMAIN, WEBHOOK_ID, DEFAULT_PORT, CONF_IP_ADDRESS, CONF_NAME, CONF_PORT, CONF_API_KEY

PLATFORMS = ["binary_sensor", "notify"]

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Configuration de l'intégration."""
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = entry.data
    
    # 1. Enregistrement du Webhook pour recevoir les logs de la Box
    # L'URL sera: http://IP_HA:8123/api/webhook/peek_it_debug
    webhook.async_register(
        hass, 
        DOMAIN, 
        "peek-it Debug Listener", 
        WEBHOOK_ID, 
        handle_webhook_log
    )
    
    # 2. Enregistrement des services (une seule fois)
    if not hass.services.has_service(DOMAIN, "get_templates"):
        hass.services.async_register(
            DOMAIN,
            "get_templates",
            async_get_templates,
            supports_response=SupportsResponse.ONLY,
        )
    if not hass.services.has_service(DOMAIN, "notify"):
        hass.services.async_register(
            DOMAIN,
            "notify",
            async_notify,
        )

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Suppression."""
    webhook.async_unregister(hass, WEBHOOK_ID)
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)
        # Désenregistrer le service quand plus aucune box configurée
        if not hass.data[DOMAIN]:
            hass.services.async_remove(DOMAIN, "get_templates")
            hass.services.async_remove(DOMAIN, "notify")
    return unload_ok

async def async_notify(call: ServiceCall) -> None:
    """Envoie une notification à toutes les box configurées."""
    hass = call.hass
    call_data = dict(call.data)

    for entry_data in hass.data.get(DOMAIN, {}).values():
        name = entry_data.get(CONF_NAME, "Box")
        ip = entry_data.get(CONF_IP_ADDRESS)
        port = entry_data.get(CONF_PORT, DEFAULT_PORT)
        api_key = entry_data.get(CONF_API_KEY, "")
        url = f"http://{ip}:{port}/api/notify"
        headers = {"X-API-Key": api_key} if api_key else {}

        # Récupération de l'IP locale de HA pour le retour de logs
        try:
            ha_ip = await network.async_get_source_ip(hass, target_ip=ip)
        except Exception:
            ha_ip = "127.0.0.1"

        # Construction du payload
        payload = {
            "action": str(call_data.get("action", "DISPLAY")),
            "duration": int(call_data.get("duration", 10000)),
            "source": "HA",
            "ha_ip": str(ha_ip),
            "elements": [],
        }

        # Champs optionnels
        if "priority" in call_data:
            payload["priority"] = str(call_data["priority"])
        if "animationIn" in call_data:
            payload["animationIn"] = str(call_data["animationIn"])
        if "animationOut" in call_data:
            payload["animationOut"] = str(call_data["animationOut"])

        # Mode template_id
        if "template_id" in call_data:
            payload["template_id"] = str(call_data["template_id"])
            if "params" in call_data and isinstance(call_data["params"], dict):
                payload["params"] = {str(k): str(v) for k, v in call_data["params"].items()}

        # Mode elements
        elif "elements" in call_data:
            payload["elements"] = call_data["elements"]

        # Mode message simple
        elif "message" in call_data:
            message = str(call_data["message"])
            payload["elements"].append({
                "type": "box",
                "style": {"left": 0, "top": 80, "width": 100, "height": 20, "bgColor": "#CC000000"}
            })
            payload["elements"].append({
                "type": "message", "content": message,
                "style": {"left": 5, "top": 82, "width": 90, "height": 16, "size": 30, "color": "#FFFFFF", "align": "center"}
            })
            if "title" in call_data:
                payload["elements"].append({
                    "type": "title", "content": str(call_data["title"]),
                    "style": {"left": 5, "top": 72, "width": 90, "height": 8, "size": 35, "color": "#3d7eff", "align": "center", "weight": "bold"}
                })

        # Envoi
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url, json=payload, headers=headers, timeout=5) as response:
                    if response.status != 200:
                        err_text = await response.text()
                        _LOGGER.error(f"Erreur Box TV {name} ({response.status}): {err_text}")
                    else:
                        _LOGGER.debug(f"Notification envoyée à {name} ({ip}:{port})")
        except Exception as e:
            _LOGGER.error(f"Erreur connexion {name}: {e}")


async def async_get_templates(call: ServiceCall) -> dict:
    """Récupère la liste des templates depuis toutes les box configurées."""
    hass = call.hass
    result = {}

    for entry_data in hass.data.get(DOMAIN, {}).values():
        name = entry_data.get(CONF_NAME, "Box")
        ip = entry_data.get(CONF_IP_ADDRESS)
        port = entry_data.get(CONF_PORT, DEFAULT_PORT)
        api_key = entry_data.get(CONF_API_KEY, "")
        url = f"http://{ip}:{port}/api/templates/list"
        headers = {"X-API-Key": api_key} if api_key else {}

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, headers=headers, timeout=5) as response:
                    if response.status == 200:
                        result[name] = await response.json()
                    else:
                        result[name] = {"error": f"HTTP {response.status}"}
        except aiohttp.ClientError as e:
            result[name] = {"error": f"Connexion impossible: {e}"}
        except Exception as e:
            result[name] = {"error": str(e)}

    return result


async def handle_webhook_log(hass: HomeAssistant, webhook_id: str, request: Request) -> Response:
    """Fonction appelée quand la Box envoie un log ou une action bouton."""
    try:
        data = await request.json()
        level = data.get("level", "INFO")
        message = data.get("message", "No message")

        # Action bouton : émet un event HA pour les automations
        if level == "ACTION" and message.startswith("BUTTON_CLICK:"):
            action_id = message.replace("BUTTON_CLICK:", "")
            hass.bus.async_fire("peekit_button_press", {"action": action_id})
            _LOGGER.info(f"[BOX TV] Bouton pressé : {action_id}")
            return Response(text="Action received")

        log_msg = f"[BOX TV REPORT] {message}"

        if level == "ERROR":
            _LOGGER.error(log_msg)
        elif level == "WARN":
            _LOGGER.warning(log_msg)
        else:
            _LOGGER.info(log_msg)

    except Exception as e:
        _LOGGER.error(f"Erreur réception webhook peek-it: {e}")

    return Response(text="Log received")
