"""Tests for the NotifyEntity payload builder (3 modes)."""
from __future__ import annotations

from homeassistant.components.notify import (
    ATTR_MESSAGE,
    ATTR_TITLE,
    DOMAIN as NOTIFY_DOMAIN,
)
from homeassistant.core import HomeAssistant
from pytest_homeassistant_custom_component.test_util.aiohttp import (
    AiohttpClientMocker,
)


def _ok_status() -> dict:
    return {"api_key_required": False, "api_key_valid": True}


async def _setup(hass, aioclient_mock, entry) -> None:
    aioclient_mock.get(
        "http://192.0.2.10:8081/api/status", json=_ok_status()
    )
    aioclient_mock.post(
        "http://192.0.2.10:8081/api/notify", status=200, text="ok"
    )
    entry.add_to_hass(hass)
    assert await hass.config_entries.async_setup(entry.entry_id)
    await hass.async_block_till_done()


async def test_simple_message_builds_box_and_message(
    hass: HomeAssistant,
    aioclient_mock: AiohttpClientMocker,
    mock_config_entry,
) -> None:
    await _setup(hass, aioclient_mock, mock_config_entry)

    await hass.services.async_call(
        NOTIFY_DOMAIN,
        "send_message",
        {
            "entity_id": "notify.living_room_tv",
            ATTR_MESSAGE: "Hello",
            ATTR_TITLE: "World",
        },
        blocking=True,
    )
    await hass.async_block_till_done()

    posts = [c for c in aioclient_mock.mock_calls
             if c[0].lower() == "post" and str(c[1]).endswith("/api/notify")]
    assert posts, "Notify payload was not POSTed"
    payload = posts[-1][2]
    types = [el["type"] for el in payload["elements"]]
    assert "box" in types
    assert "message" in types
    assert "title" in types


async def test_template_mode_passes_template_id(
    hass: HomeAssistant,
    aioclient_mock: AiohttpClientMocker,
    mock_config_entry,
) -> None:
    """The domain `notify` service forwards template_id + params."""
    await _setup(hass, aioclient_mock, mock_config_entry)
    aioclient_mock.clear_requests()
    aioclient_mock.post(
        "http://192.0.2.10:8081/api/notify", status=200, text="ok"
    )

    await hass.services.async_call(
        "peek_it_ha",
        "notify",
        {
            "template_id": "abc-123",
            "params": {"name": "Frédéric", "count": 5},
        },
        blocking=True,
    )
    await hass.async_block_till_done()

    posts = [c for c in aioclient_mock.mock_calls if c[0].lower() == "post"]
    assert posts
    payload = posts[-1][2]
    assert payload["template_id"] == "abc-123"
    assert payload["params"] == {"name": "Frédéric", "count": "5"}


async def test_elements_mode_passes_raw_elements(
    hass: HomeAssistant,
    aioclient_mock: AiohttpClientMocker,
    mock_config_entry,
) -> None:
    await _setup(hass, aioclient_mock, mock_config_entry)
    aioclient_mock.clear_requests()
    aioclient_mock.post(
        "http://192.0.2.10:8081/api/notify", status=200, text="ok"
    )

    await hass.services.async_call(
        "peek_it_ha",
        "notify",
        {
            "elements": [
                {"type": "box", "style": {"left": 10, "top": 10,
                                          "width": 80, "height": 80}}
            ]
        },
        blocking=True,
    )
    await hass.async_block_till_done()

    posts = [c for c in aioclient_mock.mock_calls if c[0].lower() == "post"]
    assert posts
    payload = posts[-1][2]
    assert len(payload["elements"]) == 1
    assert payload["elements"][0]["type"] == "box"


async def test_tts_service_payload(
    hass: HomeAssistant,
    aioclient_mock: AiohttpClientMocker,
    mock_config_entry,
) -> None:
    await _setup(hass, aioclient_mock, mock_config_entry)
    aioclient_mock.post(
        "http://192.0.2.10:8081/api/tts", status=200, text="ok"
    )

    await hass.services.async_call(
        "peek_it_ha",
        "tts",
        {"text": "Bonjour", "lang": "fr", "speed": 1.2},
        blocking=True,
    )
    await hass.async_block_till_done()

    posts = [c for c in aioclient_mock.mock_calls
             if c[0].lower() == "post" and str(c[1]).endswith("/api/tts")]
    assert posts
    payload = posts[-1][2]
    assert payload == {
        "text": "Bonjour",
        "lang": "fr",
        "speed": 1.2,
        "pitch": 1.0,
        "volume": 1.0,
    }
