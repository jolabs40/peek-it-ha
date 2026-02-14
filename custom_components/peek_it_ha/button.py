"""Boutons ADB pour gérer les permissions Assist et Overlay de peek-it.

Connexion ADB TCP directe via adb-shell (même IP que la config peek-it).
"""
import logging
import os

from homeassistant.components.button import ButtonEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import CONF_IP_ADDRESS, CONF_NAME, PEEKIT_PACKAGE, ADB_PORT

_LOGGER = logging.getLogger(__name__)

PEEKIT_ASSIST_COMPONENT = f"{PEEKIT_PACKAGE}/{PEEKIT_PACKAGE}.VoiceInputActivity"


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Crée les 4 boutons ADB peek-it."""
    ip = entry.data[CONF_IP_ADDRESS]
    name = entry.data.get(CONF_NAME, "peek-it")

    async_add_entities([
        PeekItEnableAssistButton(hass, ip, name, entry.entry_id),
        PeekItDisableAssistButton(hass, ip, name, entry.entry_id),
        PeekItEnableOverlayButton(hass, ip, name, entry.entry_id),
        PeekItDisableOverlayButton(hass, ip, name, entry.entry_id),
    ])


class PeekItAdbButton(ButtonEntity):
    """Classe de base pour les boutons ADB peek-it."""

    _attr_has_entity_name = True

    def __init__(self, hass: HomeAssistant, ip: str, device_name: str, entry_id: str) -> None:
        self._ip = ip
        self._device_name = device_name

    def _key_path(self) -> str:
        """Chemin de la clé RSA ADB (stockée dans le répertoire HA)."""
        return os.path.join(
            self.hass.config.config_dir, ".storage", "peek_it_adb_key"
        )

    async def _run_adb(self, commands: list[str]) -> bool:
        """Connexion ADB TCP directe et exécution des commandes shell."""
        try:
            from adb_shell.adb_device import AdbDeviceTcp
            from adb_shell.auth.keygen import keygen
        except ImportError:
            _LOGGER.error(
                "adb-shell non installé — installer avec : "
                "pip install adb-shell"
            )
            return False

        try:
            key_path = self._key_path()

            # Générer la paire de clés RSA au premier usage
            if not os.path.exists(key_path):
                _LOGGER.info("Génération de la clé ADB : %s", key_path)
                await self.hass.async_add_executor_job(keygen, key_path)

            # Créer le signer
            signer = await self.hass.async_add_executor_job(
                self._create_signer, key_path
            )

            # Connexion
            device = AdbDeviceTcp(self._ip, ADB_PORT, default_transport_timeout_s=10.0)
            await self.hass.async_add_executor_job(
                device.connect, [signer], None, None, 10.0
            )

            # Exécuter les commandes
            for cmd in commands:
                result = await self.hass.async_add_executor_job(device.shell, cmd)
                _LOGGER.info("ADB [%s] %s → %s", self._ip, cmd, (result or "").strip())

            await self.hass.async_add_executor_job(device.close)
            return True

        except Exception as e:
            _LOGGER.error("Erreur ADB sur %s : %s", self._ip, e)
            return False

    @staticmethod
    def _create_signer(key_path: str):
        """Crée un signer RSA ADB (appel bloquant)."""
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


# --- Boutons Assist ---

class PeekItEnableAssistButton(PeekItAdbButton):
    """Bouton : définir peek-it comme assistant par défaut."""

    _attr_icon = "mdi:microphone"
    _attr_translation_key = "enable_assist"

    def __init__(self, hass, ip, device_name, entry_id):
        super().__init__(hass, ip, device_name, entry_id)
        self._attr_unique_id = f"peek_it_enable_assist_{ip}"

    async def async_press(self) -> None:
        ok = await self._run_adb([
            f"settings put secure assistant {PEEKIT_ASSIST_COMPONENT}",
        ])
        if ok:
            _LOGGER.info("Assist peek-it activé sur %s", self._ip)


class PeekItDisableAssistButton(PeekItAdbButton):
    """Bouton : restaurer l'assistant par défaut."""

    _attr_icon = "mdi:microphone-off"
    _attr_translation_key = "disable_assist"

    def __init__(self, hass, ip, device_name, entry_id):
        super().__init__(hass, ip, device_name, entry_id)
        self._attr_unique_id = f"peek_it_disable_assist_{ip}"

    async def async_press(self) -> None:
        ok = await self._run_adb([
            "settings delete secure assistant",
        ])
        if ok:
            _LOGGER.info("Assist peek-it désactivé sur %s", self._ip)


# --- Boutons Overlay ---

class PeekItEnableOverlayButton(PeekItAdbButton):
    """Bouton : accorder la permission overlay (SYSTEM_ALERT_WINDOW)."""

    _attr_icon = "mdi:picture-in-picture-top-right"
    _attr_translation_key = "enable_overlay"

    def __init__(self, hass, ip, device_name, entry_id):
        super().__init__(hass, ip, device_name, entry_id)
        self._attr_unique_id = f"peek_it_enable_overlay_{ip}"

    async def async_press(self) -> None:
        ok = await self._run_adb([
            f"appops set {PEEKIT_PACKAGE} SYSTEM_ALERT_WINDOW allow",
        ])
        if ok:
            _LOGGER.info("Overlay peek-it activé sur %s", self._ip)


class PeekItDisableOverlayButton(PeekItAdbButton):
    """Bouton : révoquer la permission overlay (SYSTEM_ALERT_WINDOW)."""

    _attr_icon = "mdi:picture-in-picture-top-right-outline"
    _attr_translation_key = "disable_overlay"

    def __init__(self, hass, ip, device_name, entry_id):
        super().__init__(hass, ip, device_name, entry_id)
        self._attr_unique_id = f"peek_it_disable_overlay_{ip}"

    async def async_press(self) -> None:
        ok = await self._run_adb([
            f"appops set {PEEKIT_PACKAGE} SYSTEM_ALERT_WINDOW deny",
        ])
        if ok:
            _LOGGER.info("Overlay peek-it désactivé sur %s", self._ip)
