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
    default_tts_lang: str | None = None,
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
    elif "tts" in data and default_tts_lang:
        # B2 : langue TTS par défaut = langue HA, si non précisée.
        payload["ttsLang"] = str(default_tts_lang)
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
    # Mode 1 : message simple (+ presets optionnels B3 / image C1)
    elif message or data.get("image_url"):
        elements = _simple_elements(
            message or "",
            title,
            position=data.get("position"),
            icon=data.get("icon"),
            color=data.get("color"),
            level=data.get("level"),
            image_url=data.get("image_url"),
            image_fit=data.get("image_fit"),
        )
        payload["elements"] = (
            [sanitize_element(el) for el in elements] if sanitize else elements
        )

    return payload


# B3 — presets du mode simple
_POSITION_BOX_TOP = {"top": 18.0, "center": 42.0, "bottom": 78.0}
_LEVELS = {
    "info": {"accent": "#18BCF2", "icon": "mdi:information"},
    "warning": {"accent": "#FFB300", "icon": "mdi:alert"},
    "alert": {"accent": "#FF3B30", "icon": "mdi:alert-octagon"},
}


def _legacy_simple_elements(message: str, title: str | None) -> list[dict]:
    """Mode simple historique (aucun preset) : box de fond + message [+ title].

    Conservé à l'identique pour garantir zéro régression du rendu par défaut.
    """
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


def _simple_elements(
    message: str,
    title: str | None,
    *,
    position: str | None = None,
    icon: str | None = None,
    color: str | None = None,
    level: str | None = None,
    image_url: str | None = None,
    image_fit: str | None = None,
) -> list[dict]:
    """Éléments du mode simple.

    Sans aucun preset → :func:`_legacy_simple_elements` (rendu inchangé).
    Avec presets (B3) ou image (C1) → layout dédié : la box/message à la
    ``position`` choisie, l'icône (``icon`` ou icône du ``level``) et le titre
    empilés au-dessus, dans la couleur d'accent (``color`` ou couleur du
    ``level``), plus une éventuelle image.
    """
    if not (position or icon or color or level or image_url):
        return _legacy_simple_elements(message, title)

    level_cfg = _LEVELS.get(str(level).lower(), {}) if level else {}
    accent = color or level_cfg.get("accent") or "#3d7eff"
    glyph = icon or level_cfg.get("icon")
    box_top = _POSITION_BOX_TOP.get(
        str(position).lower() if position else "bottom", 78.0
    )

    elements: list[dict] = []
    if message:
        elements.append({
            "type": "box",
            "style": {"left": 0, "top": box_top, "width": 100, "height": 20,
                      "bgColor": "#CC000000"},
        })
        elements.append({
            "type": "message", "content": str(message),
            "style": {"left": 5, "top": box_top + 2, "width": 90, "height": 16,
                      "size": 30, "color": "#FFFFFF", "align": "center"},
        })

    # Icône puis titre empilés au-dessus de la box.
    y = box_top
    if glyph:
        y -= 9
        elements.append({
            "type": "text", "content": str(glyph),
            "style": {"left": 0, "top": y, "width": 100, "height": 7,
                      "size": 44, "color": accent, "align": "center"},
        })
    if title:
        y -= 9
        elements.append({
            "type": "title", "content": str(title),
            "style": {"left": 5, "top": y, "width": 90, "height": 7,
                      "size": 34, "color": accent,
                      "align": "center", "weight": "bold"},
        })

    if image_url:
        elements.append({
            "type": "image", "content": str(image_url),
            "style": {"left": 30, "top": 6, "width": 40, "height": 52,
                      "fit": str(image_fit) if image_fit else "contain"},
        })

    return elements


def build_save_template_payload(data: dict[str, Any]) -> dict[str, Any]:
    """Construit le payload ``/api/templates/save``.

    ``data`` porte ``template_id`` (id de sauvegarde, requis), ``name``
    (libellé affiché, optionnel), ``elements`` (liste, passée par
    :func:`sanitize_element` pour forcer les types Java comme le mode 2 de
    ``notify``) et ``overwrite`` (bool, défaut ``True``). Le ``target`` est
    retiré en amont par ``_dispatch`` et n'arrive pas ici.
    """
    raw = data.get("elements") or []
    payload: dict[str, Any] = {
        "id": str(data.get("template_id", "")),
        "elements": [sanitize_element(el) for el in raw],
        "overwrite": bool(data.get("overwrite", True)),
        "source": "HA",
    }
    if data.get("name"):
        payload["name"] = str(data["name"])
    return payload


def build_tts_payload(
    data: dict[str, Any], *, default_lang: str = "en"
) -> dict[str, Any]:
    """Construit le payload ``/api/tts``.

    ``default_lang`` (typiquement ``hass.config.language``) est utilisé quand
    l'appelant ne fournit pas de ``lang``.
    """
    return {
        "text": str(data.get("text", "")),
        "lang": str(data.get("lang") or default_lang),
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
    if "fit" in s:
        clean_style["fit"] = str(s["fit"])

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
