"""Capteur binaire pour l'état de peek-it TV."""
from datetime import timedelta
import logging
import aiohttp
from homeassistant.components.binary_sensor import BinarySensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from .const import DOMAIN, DEFAULT_PORT, CONF_IP_ADDRESS, CONF_NAME, CONF_PORT

_LOGGER = logging.getLogger(__name__)
SCAN_INTERVAL = timedelta(seconds=30)

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities):
    """Configuration du capteur."""
    data = hass.data[DOMAIN][entry.entry_id]
    port = data.get(CONF_PORT, DEFAULT_PORT)
    async_add_entities([PeekItStatusSensor(data[CONF_NAME], data[CONF_IP_ADDRESS], port)], True)

class PeekItStatusSensor(BinarySensorEntity):
    """Représente l'état de connexion à l'application TV."""

    def __init__(self, name, ip, port=DEFAULT_PORT):
        self._name = f"{name} Status"
        self._ip = ip
        self._port = port
        self._is_on = False
        self._attr_unique_id = f"peek_it_status_{ip}"
        self._attr_device_class = "connectivity"

    @property
    def name(self):
        return self._name

    @property
    def is_on(self):
        return self._is_on

    @property
    def extra_state_attributes(self):
        """Attribut pour fournir le lien vers le Designer."""
        return {
            "designer_url": f"http://{self._ip}:{self._port}/index.html"
        }

    async def async_update(self):
        """Interroge l'API /api/status."""
        url = f"http://{self._ip}:{self._port}/api/status"
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, timeout=2) as response:
                    if response.status == 200:
                        self._is_on = True
                    else:
                        self._is_on = False
        except Exception:
            self._is_on = False
