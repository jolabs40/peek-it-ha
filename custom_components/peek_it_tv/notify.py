"""Plateforme de notification Stricte pour peek-it TV."""
import logging
import aiohttp
from homeassistant.components.notify import NotifyEntity
from homeassistant.components import network
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN, DEFAULT_PORT, CONF_IP_ADDRESS, CONF_NAME, CONF_PORT, CONF_API_KEY

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None:
    data = hass.data[DOMAIN][entry.entry_id]
    port = data.get(CONF_PORT, DEFAULT_PORT)
    api_key = data.get(CONF_API_KEY, "")
    async_add_entities([PeekItNotificationEntity(hass, data[CONF_NAME], data[CONF_IP_ADDRESS], port, api_key)])

class PeekItNotificationEntity(NotifyEntity):
    def __init__(self, hass, name, ip, port=DEFAULT_PORT, api_key=""):
        self.hass = hass
        self._name = name
        self._ip = ip
        self._port = port
        self._api_key = api_key
        self._url = f"http://{ip}:{port}/api/notify"
        self._attr_unique_id = f"peek_it_sender_{ip}"
        self._attr_name = name

    async def async_send_message(self, message: str, title: str = None, data: dict = None) -> None:
        """Construit et envoie le Payload Strict."""

        # 1. Récupération de l'IP locale de HA pour que la Box puisse répondre (Logs)
        try:
            ha_ip = await network.async_get_source_ip(self.hass, target_ip=self._ip)
        except Exception:
            ha_ip = "127.0.0.1" # Fallback

        # 2. Structure de base (Protocole V8)
        payload = {
            "action": "DISPLAY",
            "duration": 10000,
            "source": "HA",
            "ha_ip": str(ha_ip), # Indispensable pour le retour de logs
            "elements": []
        }

        # 3. Construction ou Fusion des données
        input_data = data or {}

        # Champs communs optionnels
        if "priority" in input_data:
            payload["priority"] = str(input_data["priority"])
        if "duration" in input_data:
            payload["duration"] = int(input_data["duration"])
        if "action" in input_data:
            payload["action"] = str(input_data["action"])

        # Mode 3 : template_id + params (le serveur résout le template)
        if "template_id" in input_data:
            payload["template_id"] = str(input_data["template_id"])
            if "params" in input_data and isinstance(input_data["params"], dict):
                payload["params"] = {str(k): str(v) for k, v in input_data["params"].items()}
            # Pas d'elements : le serveur les chargera depuis le template

        # Mode 2 : JSON complet fourni via le Designer (copié dans 'data')
        elif "elements" in input_data:
            raw_elements = input_data.get("elements", [])

            # Nettoyage strict des éléments pour éviter le crash Gson
            clean_elements = []
            for el in raw_elements:
                clean_elements.append(self._sanitize_element(el))
            payload["elements"] = clean_elements

        # Mode 1 : Message Simple
        else:
            if message:
                # Fond
                payload["elements"].append(self._sanitize_element({
                    "type": "box",
                    "style": {"left": 0, "top": 80, "width": 100, "height": 20, "bgColor": "#CC000000"}
                }))
                # Texte
                payload["elements"].append(self._sanitize_element({
                    "type": "message",
                    "content": message,
                    "style": {"left": 5, "top": 82, "width": 90, "height": 16, "size": 30, "color": "#FFFFFF", "align": "center"}
                }))
                # Titre optionnel
                if title:
                    payload["elements"].append(self._sanitize_element({
                        "type": "title",
                        "content": title,
                        "style": {"left": 5, "top": 72, "width": 90, "height": 8, "size": 35, "color": "#3d7eff", "align": "center", "weight": "bold"}
                    }))

        # 4. Envoi
        headers = {"X-API-Key": self._api_key} if self._api_key else {}
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(self._url, json=payload, headers=headers, timeout=5) as response:
                    if response.status != 200:
                        err_text = await response.text()
                        _LOGGER.error(f"Erreur Box TV ({response.status}): {err_text}")
                    else:
                        _LOGGER.debug(f"Payload envoyé à {self._ip}")
        except Exception as e:
            _LOGGER.error(f"Erreur connexion TV: {e}")

    def _sanitize_element(self, el):
        """Force les types pour le protocole Java Strict."""
        s = el.get("style", {})
        
        clean_style = {
            "left": float(s.get("left", 0)),
            "top": float(s.get("top", 0)),
            "width": float(s.get("width", 10)),
            "height": float(s.get("height", 10)),
            "opacity": float(s.get("opacity", 1.0)),
            "size": int(s.get("size", 20)),
            "radius": int(s.get("radius", 0)),
            "borderWidth": int(s.get("borderWidth", 0)),
            "color": str(s.get("color", "#FFFFFF")),
            "bgColor": str(s.get("bgColor", "#00000000")),
            "borderColor": str(s.get("borderColor", "#00000000")),
            "font": str(s.get("font", "Roboto")),
            "weight": str(s.get("weight", "normal")),
            "align": str(s.get("align", "center")),
            "focusColor": str(s.get("focusColor", "#FFFFFF"))
        }

        result = {
            "type": str(el.get("type", "box")),
            "content": str(el.get("content", "")),
            "action": str(el.get("action", "")),
            "focusable": bool(el.get("focusable", False)),
            "directFocus": bool(el.get("directFocus", False)),
            "style": clean_style
        }
        if el.get("paramKey"):
            result["paramKey"] = str(el["paramKey"])
        if el.get("actionParamKey"):
            result["actionParamKey"] = str(el["actionParamKey"])
        return result
