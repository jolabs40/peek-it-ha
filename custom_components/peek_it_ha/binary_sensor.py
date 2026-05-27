"""Binary sensors for Peek-it [TV] : connectivité + permissions.

All four entities (status + overlay/accessibility/microphone permissions)
share a single :class:`PeekItCoordinator` so a single HTTP poll feeds
every state.
"""
from __future__ import annotations

import logging

from homeassistant.components.binary_sensor import (
    BinarySensorDeviceClass,
    BinarySensorEntity,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN, MANUFACTURER, MODEL
from .coordinator import PeekItCoordinator

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the binary sensors."""
    coordinator: PeekItCoordinator = hass.data[DOMAIN][entry.entry_id]

    async_add_entities([
        PeekItStatusSensor(coordinator),
        PeekItPermissionSensor(coordinator, "overlay",
                               "mdi:picture-in-picture-top-right",
                               "permission_overlay"),
        PeekItPermissionSensor(coordinator, "accessibility",
                               "mdi:human", "permission_accessibility"),
        PeekItPermissionSensor(coordinator, "microphone",
                               "mdi:microphone", "permission_microphone"),
    ])


class _PeekItEntity(CoordinatorEntity[PeekItCoordinator]):
    """Mixin attaching the shared DeviceInfo to all peek-it entities."""

    _attr_has_entity_name = True

    def __init__(self, coordinator: PeekItCoordinator) -> None:
        super().__init__(coordinator)
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, coordinator.ip)},
            name=coordinator.device_name,
            manufacturer=MANUFACTURER,
            model=MODEL,
            configuration_url=coordinator.designer_url,
        )


class PeekItStatusSensor(_PeekItEntity, BinarySensorEntity):
    """Connectivity sensor: on iff the TV answered the last /api/status poll."""

    _attr_device_class = BinarySensorDeviceClass.CONNECTIVITY
    _attr_translation_key = "status"

    def __init__(self, coordinator: PeekItCoordinator) -> None:
        super().__init__(coordinator)
        self._attr_name = None  # use the device name
        self._attr_unique_id = f"peek_it_ha_status_{coordinator.ip}"

    @property
    def is_on(self) -> bool:
        return self.coordinator.is_online

    @property
    def available(self) -> bool:
        # The connectivity sensor must stay available even when offline
        # so users can see the "off" state.
        return True

    @property
    def extra_state_attributes(self) -> dict[str, str]:
        return {"designer_url": self.coordinator.designer_url}


class PeekItPermissionSensor(_PeekItEntity, BinarySensorEntity):
    """Capteur binaire pour une permission Android (overlay, accessibilité, micro)."""

    def __init__(
        self,
        coordinator: PeekItCoordinator,
        perm_key: str,
        icon: str,
        translation_key: str,
    ) -> None:
        super().__init__(coordinator)
        self._perm_key = perm_key
        self._attr_icon = icon
        self._attr_translation_key = translation_key
        self._attr_unique_id = f"peek_it_ha_{perm_key}_{coordinator.ip}"

    @property
    def is_on(self) -> bool | None:
        data = self.coordinator.data or {}
        perms = data.get("permissions", {})
        return perms.get(self._perm_key)

    @property
    def available(self) -> bool:
        return self.coordinator.is_online and self.coordinator.data is not None
