"""Binary sensors for Peek-it [TV] : connectivité + permissions."""
from datetime import timedelta
import logging
import aiohttp
from homeassistant.components.binary_sensor import BinarySensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from .const import DOMAIN, DEFAULT_PORT, CONF_IP_ADDRESS, CONF_NAME, CONF_PORT, CONF_API_KEY

_LOGGER = logging.getLogger(__name__)
SCAN_INTERVAL = timedelta(seconds=30)

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities):
    """Set up the binary sensors."""
    data = hass.data[DOMAIN][entry.entry_id]
    ip = data[CONF_IP_ADDRESS]
    port = data.get(CONF_PORT, DEFAULT_PORT)
    api_key = data.get(CONF_API_KEY, "")
    name = data[CONF_NAME]

    status_sensor = PeekItStatusSensor(name, ip, port, api_key)
    async_add_entities([
        status_sensor,
        PeekItPermissionSensor(name, ip, status_sensor, "overlay",
                               "mdi:picture-in-picture-top-right", "permission_overlay"),
        PeekItPermissionSensor(name, ip, status_sensor, "accessibility",
                               "mdi:human", "permission_accessibility"),
        PeekItPermissionSensor(name, ip, status_sensor, "microphone",
                               "mdi:microphone", "permission_microphone"),
    ], True)


class PeekItStatusSensor(BinarySensorEntity):
    """Capteur de connectivité Peek-it [TV]."""

    def __init__(self, name, ip, port=DEFAULT_PORT, api_key=""):
        self._name = f"{name} Status"
        self._ip = ip
        self._port = port
        self._api_key = api_key
        self._is_on = False
        self._attr_unique_id = f"peek_it_ha_status_{ip}"
        self._attr_device_class = "connectivity"
        self._status_data = {}

    @property
    def name(self):
        return self._name

    @property
    def is_on(self):
        return self._is_on

    @property
    def extra_state_attributes(self):
        """Provide a direct link to the Designer."""
        return {
            "designer_url": f"http://{self._ip}:{self._port}/index.html"
        }

    async def async_update(self):
        """Poll /api/status to check connectivity and retrieve permissions."""
        url = f"http://{self._ip}:{self._port}/api/status"
        headers = {"X-API-Key": self._api_key} if self._api_key else {}
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, headers=headers, timeout=2) as response:
                    if response.status == 200:
                        self._is_on = True
                        self._status_data = await response.json()
                    else:
                        self._is_on = False
                        self._status_data = {}
        except Exception:
            self._is_on = False
            self._status_data = {}


class PeekItPermissionSensor(BinarySensorEntity):
    """Capteur binaire pour une permission Android (overlay, accessibilité, micro)."""

    _attr_has_entity_name = True

    def __init__(self, device_name, ip, status_sensor, perm_key, icon, translation_key):
        self._status_sensor = status_sensor
        self._perm_key = perm_key
        self._attr_icon = icon
        self._attr_translation_key = translation_key
        self._attr_unique_id = f"peek_it_ha_{perm_key}_{ip}"

    @property
    def is_on(self):
        perms = self._status_sensor._status_data.get("permissions", {})
        return perms.get(self._perm_key, False)

    async def async_update(self):
        """Pas de polling propre : les données viennent du status_sensor."""
        pass
