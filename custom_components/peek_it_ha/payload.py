"""Construction des payloads ``/api/notify`` et ``/api/tts``.

Centralise la fabrication du payload pour qu'un champ (image, preset…) ne
soit ajouté qu'à un seul endroit, partagé par le service de domaine
(``__init__.py``) et l'entité notify (``notify.py``). Le contrat strict
attendu par l'app Android (noms de champs + types forcés) est respecté ici.
"""
from __future__ import annotations

from typing import Any


def build_notify_payload(
    data: dict[str, Any],
    ha_ip: str,
    *,
    message: str | None = None,
    title: str | None = None,
    sanitize: bool = False,
) -> dict[str, Any]:
    """Construit le payload strict ``/api/notify`` (3 modes).

    ``data`` porte les champs optionnels (``action``, ``duration``,
    ``priority``, ``sound``, ``tts``…) ainsi que ``template_id``/``params`` ou
    ``elements``. ``message``/``title`` alimentent le mode simple.

    ``sanitize`` fait passer chaque élément par :func:`sanitize_element`
    (utilisé par l'entité notify ; le service transmet les éléments bruts).
    Les deux comportements historiques sont préservés à l'identique.
    """
    payload: dict[str, Any] = {
        "action": str(data.get("action", "DISPLAY")),
        "duration": int(data.get("duration", 10000)),
        "source": "HA",
        "ha_ip": str(ha_ip),
        "elements": [],
    }

    # Champs optionnels communs
    if "priority" in data:
        payload["priority"] = str(data["priority"])
    if "animationIn" in data:
        payload["animationIn"] = str(data["animationIn"])
    if "animationOut" in data:
        payload["animationOut"] = str(data["animationOut"])

    if "sound" in data:
        payload["sound"] = str(data["sound"])
    if "soundVolume" in data:
        payload["soundVolume"] = float(data["soundVolume"])

    if "tts" in data:
        payload["tts"] = str(data["tts"])
    if "ttsLang" in data:
        payload["ttsLang"] = str(data["ttsLang"])
    if "ttsSpeed" in data:
        payload["ttsSpeed"] = float(data["ttsSpeed"])
    if "ttsPitch" in data:
        payload["ttsPitch"] = float(data["ttsPitch"])
    if "ttsVolume" in data:
        payload["ttsVolume"] = float(data["ttsVolume"])

    # Mode 3 : template_id (+ params) — l'app résout le template
    if "template_id" in data:
        payload["template_id"] = str(data["template_id"])
        if "params" in data and isinstance(data["params"], dict):
            payload["params"] = {
                str(k): str(v) for k, v in data["params"].items()
            }
    # Mode 2 : elements bruts (Designer)
    elif "elements" in data:
        raw = data["elements"]
        payload["elements"] = (
            [sanitize_element(el) for el in raw] if sanitize else raw
        )
    # Mode 1 : message simple
    elif message:
        elements = _simple_elements(message, title)
        payload["elements"] = (
            [sanitize_element(el) for el in elements] if sanitize else elements
        )

    return payload


def _simple_elements(message: str, title: str | None) -> list[dict]:
    """Éléments du mode simple : box de fond + message [+ title]."""
    elements: list[dict] = [
        {
            "type": "box",
            "style": {"left": 0, "top": 80, "width": 100, "height": 20,
                      "bgColor": "#CC000000"},
        },
        {
            "type": "message", "content": str(message),
            "style": {"left": 5, "top": 82, "width": 90, "height": 16,
                      "size": 30, "color": "#FFFFFF", "align": "center"},
        },
    ]
    if title:
        elements.append({
            "type": "title", "content": str(title),
            "style": {"left": 5, "top": 72, "width": 90, "height": 8,
                      "size": 35, "color": "#3d7eff",
                      "align": "center", "weight": "bold"},
        })
    return elements


def build_tts_payload(data: dict[str, Any]) -> dict[str, Any]:
    """Construit le payload ``/api/tts``."""
    return {
        "text": str(data.get("text", "")),
        "lang": str(data.get("lang", "en")),
        "speed": float(data.get("speed", 1.0)),
        "pitch": float(data.get("pitch", 1.0)),
        "volume": float(data.get("volume", 1.0)),
    }


def sanitize_element(el: dict) -> dict:
    """Force les types pour le protocole strict (Java) de l'app Android."""
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

    # Propriétés de style optionnelles (incluses seulement si présentes)
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
