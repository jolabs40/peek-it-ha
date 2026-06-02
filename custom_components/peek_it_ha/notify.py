"""Strict notification platform for Peek-it [HA]."""
from __future__ import annotations

import logging

from homeassistant.components import network
from homeassistant.components.notify import NotifyEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import (
    DOMAIN,
    MANUFACTURER,
    MODEL,
)
from .coordinator import PeekItCoordinator
from .http import async_post_json
from .payload import build_notify_payload

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    coordinator: PeekItCoordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([PeekItNotificationEntity(coordinator)])


class PeekItNotificationEntity(CoordinatorEntity[PeekItCoordinator], NotifyEntity):
    """Notify entity that POSTs structured payloads to the TV.

    Hérite de ``CoordinatorEntity`` pour réécrire son état (et donc
    réévaluer ``available``) à chaque poll ``/api/status`` : sans cette
    souscription, ``available`` restait figé à sa valeur du setup et
    l'entité pouvait afficher ``unavailable`` alors que le binary_sensor
    de statut de la même TV était ``on``.
    """

    _attr_has_entity_name = True

    def __init__(self, coordinator: PeekItCoordinator) -> None:
        super().__init__(coordinator)
        self._coordinator = coordinator
        self._attr_name = None  # Use the device name
        self._attr_unique_id = f"peek_it_ha_sender_{coordinator.ip}"
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, coordinator.ip)},
            name=coordinator.device_name,
            manufacturer=MANUFACTURER,
            model=MODEL,
            configuration_url=coordinator.designer_url,
        )

    @property
    def available(self) -> bool:
        return self._coordinator.is_online

    @property
    def _url(self) -> str:
        return f"http://{self._coordinator.ip}:{self._coordinator.port}/api/notify"

    @property
    def _headers(self) -> dict[str, str]:
        return {"X-API-Key": self._coordinator.api_key} if self._coordinator.api_key else {}

    async def async_send_message(
        self,
        message: str,
        title: str | None = None,
        data: dict | None = None,
    ) -> None:
        """Build and send the strict payload.

        Le payload est construit par :func:`build_notify_payload` (partagé
        avec le service de domaine) avec ``sanitize=True`` : l'entité notify
        force les types de chaque élément pour le protocole strict de l'app.
        """
        # IP locale HA pour que la TV renvoie ses logs/callbacks
        try:
            ha_ip = await network.async_get_source_ip(
                self.hass, target_ip=self._coordinator.ip
            )
        except Exception:  # noqa: BLE001 — best-effort lookup
            ha_ip = "127.0.0.1"

        payload = build_notify_payload(
            data or {},
            str(ha_ip),
            message=message,
            title=title,
            sanitize=True,
        )

        await async_post_json(
            self.hass,
            self._url,
            payload,
            headers=self._headers,
            context=f"notify {self._coordinator.device_name}",
        )
