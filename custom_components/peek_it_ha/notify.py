"""Strict notification platform for Peek-it [HA]."""
from __future__ import annotations

import logging

from homeassistant.components import network
from homeassistant.components.notify import NotifyEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import (
    DOMAIN,
    MANUFACTURER,
    MODEL,
)
from .coordinator import PeekItCoordinator
from .http import async_post_json

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    coordinator: PeekItCoordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([PeekItNotificationEntity(coordinator)])


class PeekItNotificationEntity(NotifyEntity):
    """Notify entity that POSTs structured payloads to the TV."""

    _attr_has_entity_name = True

    def __init__(self, coordinator: PeekItCoordinator) -> None:
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
        """Build and send the strict payload."""

        # 1. Get HA local IP so the TV can send back logs
        try:
            ha_ip = await network.async_get_source_ip(
                self.hass, target_ip=self._coordinator.ip
            )
        except Exception:  # noqa: BLE001 — best-effort lookup
            ha_ip = "127.0.0.1"

        # 2. Base payload structure
        payload: dict = {
            "action": "DISPLAY",
            "duration": 10000,
            "source": "HA",
            "ha_ip": str(ha_ip),
            "elements": [],
        }

        # 3. Build or merge data
        input_data = data or {}

        # Common optional fields
        if "priority" in input_data:
            payload["priority"] = str(input_data["priority"])
        if "duration" in input_data:
            payload["duration"] = int(input_data["duration"])
        if "action" in input_data:
            payload["action"] = str(input_data["action"])
        if "animationIn" in input_data:
            payload["animationIn"] = str(input_data["animationIn"])
        if "animationOut" in input_data:
            payload["animationOut"] = str(input_data["animationOut"])

        # Sound passthrough
        if "sound" in input_data:
            payload["sound"] = str(input_data["sound"])
        if "soundVolume" in input_data:
            payload["soundVolume"] = float(input_data["soundVolume"])

        # TTS passthrough
        if "tts" in input_data:
            payload["tts"] = str(input_data["tts"])
        if "ttsLang" in input_data:
            payload["ttsLang"] = str(input_data["ttsLang"])
        if "ttsSpeed" in input_data:
            payload["ttsSpeed"] = float(input_data["ttsSpeed"])
        if "ttsPitch" in input_data:
            payload["ttsPitch"] = float(input_data["ttsPitch"])
        if "ttsVolume" in input_data:
            payload["ttsVolume"] = float(input_data["ttsVolume"])

        # Mode 3: template_id + params (server resolves the template)
        if "template_id" in input_data:
            payload["template_id"] = str(input_data["template_id"])
            if "params" in input_data and isinstance(input_data["params"], dict):
                payload["params"] = {
                    str(k): str(v) for k, v in input_data["params"].items()
                }

        # Mode 2: Full JSON from the Designer
        elif "elements" in input_data:
            raw_elements = input_data.get("elements", [])
            payload["elements"] = [self._sanitize_element(el) for el in raw_elements]

        # Mode 1: Simple message
        else:
            if message:
                payload["elements"].append(self._sanitize_element({
                    "type": "box",
                    "style": {"left": 0, "top": 80, "width": 100, "height": 20,
                              "bgColor": "#CC000000"}
                }))
                payload["elements"].append(self._sanitize_element({
                    "type": "message",
                    "content": message,
                    "style": {"left": 5, "top": 82, "width": 90, "height": 16,
                              "size": 30, "color": "#FFFFFF", "align": "center"}
                }))
                if title:
                    payload["elements"].append(self._sanitize_element({
                        "type": "title",
                        "content": title,
                        "style": {"left": 5, "top": 72, "width": 90, "height": 8,
                                  "size": 35, "color": "#3d7eff",
                                  "align": "center", "weight": "bold"}
                    }))

        await async_post_json(
            self.hass,
            self._url,
            payload,
            headers=self._headers,
            context=f"notify {self._coordinator.device_name}",
        )

    def _sanitize_element(self, el: dict) -> dict:
        """Force types for the strict Java protocol."""
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
            "focusColor": str(s.get("focusColor", "#FFFFFF")),
            "focusBgColor": str(s.get("focusBgColor", "#00000000")),
        }

        # Optional style properties (only include if present)
        for key in ("shadowColor", "shadowOpacity", "shadowBlur",
                    "shadowOffsetX", "shadowOffsetY"):
            if key in s:
                clean_style[key] = (
                    float(s[key]) if key != "shadowColor" else str(s[key])
                )
        if "animation" in s:
            clean_style["animation"] = str(s["animation"])
        if "animationSpeed" in s:
            clean_style["animationSpeed"] = float(s["animationSpeed"])
        if "rotation" in s:
            clean_style["rotation"] = float(s["rotation"])

        result = {
            "type": str(el.get("type", "box")),
            "content": str(el.get("content", "")),
            "action": str(el.get("action", "")),
            "focusable": bool(el.get("focusable", False)),
            "directFocus": bool(el.get("directFocus", False)),
            "style": clean_style,
        }
        if el.get("paramKey"):
            result["paramKey"] = str(el["paramKey"])
        if el.get("actionParamKey"):
            result["actionParamKey"] = str(el["actionParamKey"])
        return result
