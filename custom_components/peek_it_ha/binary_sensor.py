"""Binary sensor for Peek-it [TV] connection status."""
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
    """Set up the binary sensor."""
    data = hass.data[DOMAIN][entry.entry_id]
    port = data.get(CONF_PORT, DEFAULT_PORT)
    api_key = data.get(CONF_API_KEY, "")
    async_add_entities([PeekItStatusSensor(data[CONF_NAME], data[CONF_IP_ADDRESS], port, api_key)], True)

class PeekItStatusSensor(BinarySensorEntity):
    """Represents the connection status of the Peek-it [TV] app."""

    def __init__(self, name, ip, port=DEFAULT_PORT, api_key=""):
        self._name = f"{name} Status"
        self._ip = ip
        self._port = port
        self._api_key = api_key
        self._is_on = False
        self._attr_unique_id = f"peek_it_ha_status_{ip}"
        self._attr_device_class = "connectivity"

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
        """Poll /api/status to check connectivity."""
        url = f"http://{self._ip}:{self._port}/api/status"
        headers = {"X-API-Key": self._api_key} if self._api_key else {}
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, headers=headers, timeout=2) as response:
                    if response.status == 200:
                        self._is_on = True
                    else:
                        self._is_on = False
        except Exception:
            self._is_on = False
