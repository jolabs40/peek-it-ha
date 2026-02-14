"""Button entities for peek-it HA — ADB permissions management."""
import logging
import os

from homeassistant.components.button import ButtonEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN, CONF_IP_ADDRESS, CONF_NAME

_LOGGER = logging.getLogger(__name__)

ADB_PORT = 5555
PEEKIT_PACKAGE = "net.jolabs40.peekit"
PEEKIT_ASSIST_COMPONENT = f"{PEEKIT_PACKAGE}/{PEEKIT_PACKAGE}.VoiceInputActivity"


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up peek-it ADB button entities."""
    ip = entry.data[CONF_IP_ADDRESS]
    name = entry.data.get(CONF_NAME, "peek-it")

    async_add_entities([
        PeekItEnableAssistButton(hass, ip, name, entry.entry_id),
        PeekItDisableAssistButton(hass, ip, name, entry.entry_id),
    ])


class PeekItAdbButton(ButtonEntity):
    """Base class for peek-it ADB buttons."""

    def __init__(self, hass: HomeAssistant, ip: str, device_name: str, entry_id: str) -> None:
        self._ip = ip
        self._device_name = device_name
        self._attr_has_entity_name = True
        self._attr_device_info = {
            "identifiers": {(DOMAIN, entry_id)},
            "name": device_name,
            "manufacturer": "peek-it",
        }

    def _key_path(self) -> str:
        """Return the path to the ADB RSA key (stored in HA config dir)."""
        return os.path.join(
            self.hass.config.config_dir, ".storage", "peek_it_adb_key"
        )

    async def _run_adb(self, commands: list[str]) -> bool:
        """Connect via ADB TCP and execute shell commands."""
        try:
            from adb_shell.adb_device import AdbDeviceTcp
            from adb_shell.auth.keygen import keygen

            key_path = self._key_path()

            # Generate RSA key pair on first use
            if not os.path.exists(key_path):
                _LOGGER.info("Generating ADB key pair at %s", key_path)
                await self.hass.async_add_executor_job(keygen, key_path)

            # Create signer
            signer = await self.hass.async_add_executor_job(
                self._create_signer, key_path
            )

            # Connect
            device = AdbDeviceTcp(self._ip, ADB_PORT, default_transport_timeout_s=10.0)
            await self.hass.async_add_executor_job(
                device.connect, [signer], None, None, 10.0
            )

            # Execute commands
            for cmd in commands:
                result = await self.hass.async_add_executor_job(device.shell, cmd)
                _LOGGER.info("ADB [%s] %s → %s", self._ip, cmd, (result or "").strip())

            await self.hass.async_add_executor_job(device.close)
            return True

        except Exception as e:
            _LOGGER.error("ADB error on %s: %s", self._ip, e)
            return False

    @staticmethod
    def _create_signer(key_path: str):
        """Create an ADB RSA signer (blocking call)."""
        try:
            from adb_shell.auth.sign_cryptography import CryptographySigner
            return CryptographySigner(key_path)
        except ImportError:
            from adb_shell.auth.sign_pythonrsa import PythonRSASigner
            with open(key_path) as f:
                priv = f.read()
            with open(key_path + ".pub") as f:
                pub = f.read()
            return PythonRSASigner(priv, pub)


class PeekItEnableAssistButton(PeekItAdbButton):
    """Button: set peek-it as default assistant + force overlay permission."""

    _attr_icon = "mdi:microphone"
    _attr_translation_key = "enable_assist"

    def __init__(self, hass, ip, device_name, entry_id):
        super().__init__(hass, ip, device_name, entry_id)
        self._attr_unique_id = f"peek_it_enable_assist_{ip}"

    @property
    def name(self) -> str:
        return "Enable Assist"

    async def async_press(self) -> None:
        """Set peek-it as default assistant and grant overlay permission."""
        ok = await self._run_adb([
            f"settings put secure assistant {PEEKIT_ASSIST_COMPONENT}",
            f"appops set {PEEKIT_PACKAGE} SYSTEM_ALERT_WINDOW allow",
        ])
        if ok:
            _LOGGER.info("peek-it Assist enabled on %s", self._ip)
        else:
            _LOGGER.error("Failed to enable peek-it Assist on %s", self._ip)


class PeekItDisableAssistButton(PeekItAdbButton):
    """Button: restore default assistant + revoke overlay permission."""

    _attr_icon = "mdi:microphone-off"
    _attr_translation_key = "disable_assist"

    def __init__(self, hass, ip, device_name, entry_id):
        super().__init__(hass, ip, device_name, entry_id)
        self._attr_unique_id = f"peek_it_disable_assist_{ip}"

    @property
    def name(self) -> str:
        return "Disable Assist"

    async def async_press(self) -> None:
        """Restore default assistant and revoke overlay permission."""
        ok = await self._run_adb([
            "settings delete secure assistant",
            f"appops set {PEEKIT_PACKAGE} SYSTEM_ALERT_WINDOW deny",
        ])
        if ok:
            _LOGGER.info("peek-it Assist disabled on %s", self._ip)
        else:
            _LOGGER.error("Failed to disable peek-it Assist on %s", self._ip)
