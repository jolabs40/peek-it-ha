"""Tests for the NotifyEntity payload builder (3 modes) and the domain
``notify``/``tts`` services (parallel fan-out, offline skip, target)."""
from __future__ import annotations

from homeassistant.components.notify import (
    ATTR_MESSAGE,
    ATTR_TITLE,
    DOMAIN as NOTIFY_DOMAIN,
)
from homeassistant.core import HomeAssistant
from pytest_homeassistant_custom_component.common import MockConfigEntry
from pytest_homeassistant_custom_component.test_util.aiohttp import (
    AiohttpClientMocker,
)

from custom_components.peek_it_ha.const import (
    CONF_API_KEY,
    CONF_IP_ADDRESS,
    CONF_NAME,
    CONF_PORT,
    CONF_WEBHOOK_SECRET,
    DEFAULT_PORT,
    DOMAIN,
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


def _second_entry() -> MockConfigEntry:
    """A second configured TV at 192.0.2.20."""
    return MockConfigEntry(
        domain=DOMAIN,
        title="Kitchen TV",
        data={
            CONF_IP_ADDRESS: "192.0.2.20",
            CONF_PORT: DEFAULT_PORT,
            CONF_NAME: "Kitchen TV",
            CONF_API_KEY: "",
            CONF_WEBHOOK_SECRET: "test-secret-def456",
        },
        unique_id="192.0.2.20",
    )


async def test_notify_skips_offline_tv(
    hass: HomeAssistant,
    aioclient_mock: AiohttpClientMocker,
    mock_config_entry,
) -> None:
    """An offline coordinator is skipped — no /api/notify POST is made."""
    await _setup(hass, aioclient_mock, mock_config_entry)

    # Force the TV offline (as if the last status poll failed).
    coord = hass.data[DOMAIN][mock_config_entry.entry_id]
    coord.is_online = False

    aioclient_mock.clear_requests()
    aioclient_mock.post(
        "http://192.0.2.10:8081/api/notify", status=200, text="ok"
    )

    await hass.services.async_call(
        "peek_it_ha", "notify", {"message": "Hello"}, blocking=True
    )
    await hass.async_block_till_done()

    posts = [c for c in aioclient_mock.mock_calls if c[0].lower() == "post"]
    assert not posts, "Offline TV should not be contacted"


async def test_notify_target_filters_to_single_tv(
    hass: HomeAssistant,
    aioclient_mock: AiohttpClientMocker,
    mock_config_entry,
) -> None:
    """With two TVs, a `target` (device name) only hits the matching one."""
    entry2 = _second_entry()
    aioclient_mock.get("http://192.0.2.20:8081/api/status", json=_ok_status())
    aioclient_mock.post(
        "http://192.0.2.20:8081/api/notify", status=200, text="ok"
    )
    await _setup(hass, aioclient_mock, mock_config_entry)
    entry2.add_to_hass(hass)
    assert await hass.config_entries.async_setup(entry2.entry_id)
    await hass.async_block_till_done()

    aioclient_mock.clear_requests()
    aioclient_mock.post(
        "http://192.0.2.10:8081/api/notify", status=200, text="ok"
    )
    aioclient_mock.post(
        "http://192.0.2.20:8081/api/notify", status=200, text="ok"
    )

    await hass.services.async_call(
        "peek_it_ha",
        "notify",
        {"message": "Salon only", "target": "Living Room TV"},
        blocking=True,
    )
    await hass.async_block_till_done()

    urls = [str(c[1]) for c in aioclient_mock.mock_calls
            if c[0].lower() == "post"]
    assert any("192.0.2.10" in u for u in urls)
    assert not any("192.0.2.20" in u for u in urls)


async def test_notify_entity_available_follows_coordinator(
    hass: HomeAssistant,
    aioclient_mock: AiohttpClientMocker,
    mock_config_entry,
) -> None:
    """notify.<device> availability tracks coordinator.is_online live."""
    await _setup(hass, aioclient_mock, mock_config_entry)

    state = hass.states.get("notify.living_room_tv")
    assert state is not None and state.state != "unavailable"

    coord = hass.data[DOMAIN][mock_config_entry.entry_id]
    coord.is_online = False
    coord.async_update_listeners()
    await hass.async_block_till_done()

    state = hass.states.get("notify.living_room_tv")
    assert state is not None and state.state == "unavailable"
