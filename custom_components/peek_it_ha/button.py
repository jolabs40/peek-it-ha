"""Boutons ADB pour gérer les permissions Assist et Overlay de peek-it.

Utilise le service androidtv.adb_command de l'intégration Android TV de HA.
L'entity_id du media_player Android TV doit être configuré dans les paramètres.
"""
import logging

from homeassistant.components.button import ButtonEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import CONF_IP_ADDRESS, CONF_NAME, CONF_ATV_ENTITY, PEEKIT_PACKAGE

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
    atv_entity = entry.data.get(CONF_ATV_ENTITY, "")

    async_add_entities([
        PeekItEnableAssistButton(hass, ip, name, entry.entry_id, atv_entity),
        PeekItDisableAssistButton(hass, ip, name, entry.entry_id, atv_entity),
        PeekItEnableOverlayButton(hass, ip, name, entry.entry_id, atv_entity),
        PeekItDisableOverlayButton(hass, ip, name, entry.entry_id, atv_entity),
    ])


class PeekItAdbButton(ButtonEntity):
    """Classe de base pour les boutons ADB peek-it."""

    _attr_has_entity_name = True

    def __init__(self, hass: HomeAssistant, ip: str, device_name: str,
                 entry_id: str, atv_entity: str) -> None:
        self._ip = ip
        self._device_name = device_name
        self._atv_entity = atv_entity

    async def _run_adb(self, command: str) -> bool:
        """Envoie une commande ADB via le service androidtv.adb_command."""
        if not self._atv_entity:
            _LOGGER.error(
                "Entity Android TV non configurée — aller dans Options > "
                "Paramètres et renseigner l'entity_id (ex: media_player.shield)"
            )
            return False

        try:
            await self.hass.services.async_call(
                "androidtv",
                "adb_command",
                {"entity_id": self._atv_entity, "command": command},
                blocking=True,
            )
            _LOGGER.info("ADB [%s] %s", self._atv_entity, command)
            return True
        except Exception as e:
            _LOGGER.error("Erreur ADB via %s : %s", self._atv_entity, e)
            return False


# --- Boutons Assist ---

class PeekItEnableAssistButton(PeekItAdbButton):
    """Bouton : définir peek-it comme assistant par défaut."""

    _attr_icon = "mdi:microphone"
    _attr_translation_key = "enable_assist"

    def __init__(self, hass, ip, device_name, entry_id, atv_entity):
        super().__init__(hass, ip, device_name, entry_id, atv_entity)
        self._attr_unique_id = f"peek_it_enable_assist_{ip}"

    async def async_press(self) -> None:
        ok = await self._run_adb(
            f"settings put secure assistant {PEEKIT_ASSIST_COMPONENT}"
        )
        if ok:
            _LOGGER.info("Assist peek-it activé sur %s", self._ip)


class PeekItDisableAssistButton(PeekItAdbButton):
    """Bouton : restaurer l'assistant par défaut."""

    _attr_icon = "mdi:microphone-off"
    _attr_translation_key = "disable_assist"

    def __init__(self, hass, ip, device_name, entry_id, atv_entity):
        super().__init__(hass, ip, device_name, entry_id, atv_entity)
        self._attr_unique_id = f"peek_it_disable_assist_{ip}"

    async def async_press(self) -> None:
        ok = await self._run_adb("settings delete secure assistant")
        if ok:
            _LOGGER.info("Assist peek-it désactivé sur %s", self._ip)


# --- Boutons Overlay ---

class PeekItEnableOverlayButton(PeekItAdbButton):
    """Bouton : accorder la permission overlay (SYSTEM_ALERT_WINDOW)."""

    _attr_icon = "mdi:picture-in-picture-top-right"
    _attr_translation_key = "enable_overlay"

    def __init__(self, hass, ip, device_name, entry_id, atv_entity):
        super().__init__(hass, ip, device_name, entry_id, atv_entity)
        self._attr_unique_id = f"peek_it_enable_overlay_{ip}"

    async def async_press(self) -> None:
        ok = await self._run_adb(
            f"appops set {PEEKIT_PACKAGE} SYSTEM_ALERT_WINDOW allow"
        )
        if ok:
            _LOGGER.info("Overlay peek-it activé sur %s", self._ip)


class PeekItDisableOverlayButton(PeekItAdbButton):
    """Bouton : révoquer la permission overlay (SYSTEM_ALERT_WINDOW)."""

    _attr_icon = "mdi:picture-in-picture-top-right-outline"
    _attr_translation_key = "disable_overlay"

    def __init__(self, hass, ip, device_name, entry_id, atv_entity):
        super().__init__(hass, ip, device_name, entry_id, atv_entity)
        self._attr_unique_id = f"peek_it_disable_overlay_{ip}"

    async def async_press(self) -> None:
        ok = await self._run_adb(
            f"appops set {PEEKIT_PACKAGE} SYSTEM_ALERT_WINDOW deny"
        )
        if ok:
            _LOGGER.info("Overlay peek-it désactivé sur %s", self._ip)
