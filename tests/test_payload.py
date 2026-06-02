"""Unit tests for the shared payload builder (B2 lang, B3 presets, C1 image)."""
from __future__ import annotations

from custom_components.peek_it_ha.payload import (
    _legacy_simple_elements,
    build_notify_payload,
    build_tts_payload,
)


def test_simple_mode_unchanged_without_presets() -> None:
    """No preset field → byte-for-byte the legacy box/message/title elements."""
    payload = build_notify_payload({}, "1.2.3.4", message="Hello", title="Hi")
    assert payload["elements"] == _legacy_simple_elements("Hello", "Hi")
    assert [e["type"] for e in payload["elements"]] == ["box", "message", "title"]


def test_tts_payload_default_lang() -> None:
    assert build_tts_payload({"text": "hi"}, default_lang="fr")["lang"] == "fr"
    assert (
        build_tts_payload({"text": "hi", "lang": "de"}, default_lang="fr")["lang"]
        == "de"
    )


def test_notify_tts_default_lang_injected() -> None:
    """ttsLang defaults to the HA language only when tts is present and unset."""
    p = build_notify_payload(
        {"tts": "bonjour"}, "1.2.3.4", message="x", default_tts_lang="fr"
    )
    assert p["ttsLang"] == "fr"

    p2 = build_notify_payload(
        {"tts": "bonjour", "ttsLang": "de"}, "1.2.3.4", message="x",
        default_tts_lang="fr",
    )
    assert p2["ttsLang"] == "de"

    p3 = build_notify_payload({}, "1.2.3.4", message="x", default_tts_lang="fr")
    assert "ttsLang" not in p3


def test_presets_level_adds_icon_and_accent() -> None:
    payload = build_notify_payload({"level": "warning"}, "1.2.3.4", message="Careful")
    icon = next(e for e in payload["elements"] if e["type"] == "text")
    assert icon["content"] == "mdi:alert"
    assert icon["style"]["color"] == "#FFB300"


def test_presets_position_moves_box() -> None:
    payload = build_notify_payload({"position": "top"}, "1.2.3.4", message="Top")
    box = next(e for e in payload["elements"] if e["type"] == "box")
    assert box["style"]["top"] == 18.0


def test_color_overrides_level_accent() -> None:
    payload = build_notify_payload(
        {"level": "info", "color": "#ABCDEF"}, "1.2.3.4", message="x", title="T"
    )
    title = next(e for e in payload["elements"] if e["type"] == "title")
    assert title["style"]["color"] == "#ABCDEF"


def test_image_url_adds_image_element() -> None:
    payload = build_notify_payload(
        {"image_url": "http://x/y.jpg", "image_fit": "cover"},
        "1.2.3.4", message="Visitor",
    )
    img = next(e for e in payload["elements"] if e["type"] == "image")
    assert img["content"] == "http://x/y.jpg"
    assert img["style"]["fit"] == "cover"


def test_image_only_without_message() -> None:
    """image_url alone (no message) still produces an image, no message box."""
    payload = build_notify_payload(
        {"image_url": "http://x/y.jpg"}, "1.2.3.4", message=None
    )
    types = [e["type"] for e in payload["elements"]]
    assert "image" in types
    assert "message" not in types and "box" not in types


def test_sanitize_preserves_image_fit() -> None:
    """The entity path (sanitize=True) keeps style.fit on image elements."""
    payload = build_notify_payload(
        {"image_url": "http://x/y.jpg", "image_fit": "cover"},
        "1.2.3.4", message="x", sanitize=True,
    )
    img = next(e for e in payload["elements"] if e["type"] == "image")
    assert img["style"]["fit"] == "cover"
