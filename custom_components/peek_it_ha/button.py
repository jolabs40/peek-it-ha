"""Boutons ADB pour gérer les permissions Assist et Overlay de peek-it.

Connexion ADB TCP directe via adb-shell (même IP que la config peek-it).
"""
from __future__ import annotations

import logging
import os

from homeassistant.components.button import ButtonEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import EntityCategory
from homeassistant.core import HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import (
    ADB_PORT,
    DOMAIN,
    MANUFACTURER,
    MODEL,
    PEEKIT_ACCESSIBILITY_COMPONENT,
    PEEKIT_PACKAGE,
)
from .coordinator import PeekItCoordinator

_LOGGER = logging.getLogger(__name__)

PEEKIT_ASSIST_COMPONENT = f"{PEEKIT_PACKAGE}/{PEEKIT_PACKAGE}.VoiceInputActivity"


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Crée les 6 boutons ADB peek-it."""
    coordinator: PeekItCoordinator = hass.data[DOMAIN][entry.entry_id]

    async_add_entities([
        PeekItEnableAssistButton(coordinator),
        PeekItDisableAssistButton(coordinator),
        PeekItEnableOverlayButton(coordinator),
        PeekItDisableOverlayButton(coordinator),
        PeekItEnableAccessibilityButton(coordinator),
        PeekItDisableAccessibilityButton(coordinator),
    ])


class PeekItAdbButton(ButtonEntity):
    """Classe de base pour les boutons ADB peek-it."""

    _attr_has_entity_name = True
    _attr_entity_category = EntityCategory.CONFIG

    def __init__(self, coordinator: PeekItCoordinator) -> None:
        self._coordinator = coordinator
        self._ip = coordinator.ip
        self._device_name = coordinator.device_name
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, coordinator.ip)},
            name=coordinator.device_name,
            manufacturer=MANUFACTURER,
            model=MODEL,
            configuration_url=coordinator.designer_url,
        )

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
            exists = await self.hass.async_add_executor_job(
                os.path.exists, key_path
            )
            if not exists:
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

        except Exception as e:  # noqa: BLE001 — adb-shell raises various errors
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

    def __init__(self, coordinator: PeekItCoordinator) -> None:
        super().__init__(coordinator)
        self._attr_unique_id = f"peek_it_enable_assist_{coordinator.ip}"

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

    def __init__(self, coordinator: PeekItCoordinator) -> None:
        super().__init__(coordinator)
        self._attr_unique_id = f"peek_it_disable_assist_{coordinator.ip}"

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

    def __init__(self, coordinator: PeekItCoordinator) -> None:
        super().__init__(coordinator)
        self._attr_unique_id = f"peek_it_enable_overlay_{coordinator.ip}"

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

    def __init__(self, coordinator: PeekItCoordinator) -> None:
        super().__init__(coordinator)
        self._attr_unique_id = f"peek_it_disable_overlay_{coordinator.ip}"

    async def async_press(self) -> None:
        ok = await self._run_adb([
            f"appops set {PEEKIT_PACKAGE} SYSTEM_ALERT_WINDOW deny",
        ])
        if ok:
            _LOGGER.info("Overlay peek-it désactivé sur %s", self._ip)


# --- Boutons Accessibilité ---

class PeekItEnableAccessibilityButton(PeekItAdbButton):
    """Bouton : activer le service d'accessibilité MenuKeyService."""

    _attr_icon = "mdi:human"
    _attr_translation_key = "enable_accessibility"

    def __init__(self, coordinator: PeekItCoordinator) -> None:
        super().__init__(coordinator)
        self._attr_unique_id = f"peek_it_enable_accessibility_{coordinator.ip}"

    async def async_press(self) -> None:
        cmd = (
            f'current=$(settings get secure enabled_accessibility_services) && '
            f'if echo "$current" | grep -q \'{PEEKIT_ACCESSIBILITY_COMPONENT}\'; then echo ok; else '
            f'if [ -z "$current" ] || [ "$current" = "null" ]; then '
            f'settings put secure enabled_accessibility_services {PEEKIT_ACCESSIBILITY_COMPONENT}; else '
            f'settings put secure enabled_accessibility_services "$current:{PEEKIT_ACCESSIBILITY_COMPONENT}"; fi; fi'
        )
        ok = await self._run_adb([cmd])
        if ok:
            _LOGGER.info("Accessibilité peek-it activée sur %s", self._ip)


class PeekItDisableAccessibilityButton(PeekItAdbButton):
    """Bouton : désactiver le service d'accessibilité MenuKeyService."""

    _attr_icon = "mdi:human-male-board-poll"
    _attr_translation_key = "disable_accessibility"

    def __init__(self, coordinator: PeekItCoordinator) -> None:
        super().__init__(coordinator)
        self._attr_unique_id = f"peek_it_disable_accessibility_{coordinator.ip}"

    async def async_press(self) -> None:
        c = PEEKIT_ACCESSIBILITY_COMPONENT
        cmd = (
            "current=$(settings get secure enabled_accessibility_services) && "
            f"new=$(echo \"$current\" | sed 's#{c}##' | sed 's/^://;s/:$//;s/::/:/' ) && "
            "if [ -z \"$new\" ] || [ \"$new\" = \"null\" ]; then "
            "settings put secure enabled_accessibility_services null; else "
            "settings put secure enabled_accessibility_services \"$new\"; fi"
        )
        ok = await self._run_adb([cmd])
        if ok:
            _LOGGER.info("Accessibilité peek-it désactivée sur %s", self._ip)
