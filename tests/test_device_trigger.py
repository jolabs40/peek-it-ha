"""Tests for device triggers (C3) and the webhook device_id enrichment."""
from __future__ import annotations

from homeassistant.core import HomeAssistant
from homeassistant.helpers import device_registry as dr
from homeassistant.setup import async_setup_component
from pytest_homeassistant_custom_component.test_util.aiohttp import (
    AiohttpClientMocker,
)

from custom_components.peek_it_ha import _device_id_for_ip, handle_webhook_log
from custom_components.peek_it_ha.const import (
    DOMAIN,
    EVENT_BUTTON_PRESS,
    WEBHOOK_ID,
)
from custom_components.peek_it_ha.device_trigger import async_get_triggers


class _FakeRequest:
    """Minimal stand-in for an aiohttp Request with a chosen source IP."""

    def __init__(self, remote: str, secret: str, payload: dict) -> None:
        self.remote = remote
        self.headers = {"X-Peek-Secret": secret}
        self._payload = payload

    async def json(self) -> dict:
        return self._payload


async def _setup(hass, aioclient_mock, entry) -> None:
    await async_setup_component(hass, "webhook", {})
    aioclient_mock.get(
        "http://192.0.2.10:8081/api/status",
        json={"api_key_required": False, "api_key_valid": True},
    )
    entry.add_to_hass(hass)
    assert await hass.config_entries.async_setup(entry.entry_id)
    await hass.async_block_till_done()


def _device_id(hass) -> str:
    device = dr.async_get(hass).async_get_device(
        identifiers={(DOMAIN, "192.0.2.10")}
    )
    assert device is not None
    return device.id


async def test_get_triggers_lists_button_press(
    hass: HomeAssistant,
    aioclient_mock: AiohttpClientMocker,
    mock_config_entry,
) -> None:
    await _setup(hass, aioclient_mock, mock_config_entry)
    dev_id = _device_id(hass)

    triggers = await async_get_triggers(hass, dev_id)
    assert {
        "platform": "device",
        "domain": DOMAIN,
        "device_id": dev_id,
        "type": "button_press",
    } in triggers


async def test_device_id_for_ip_resolution(
    hass: HomeAssistant,
    aioclient_mock: AiohttpClientMocker,
    mock_config_entry,
) -> None:
    await _setup(hass, aioclient_mock, mock_config_entry)
    assert _device_id_for_ip(hass, "192.0.2.10") == _device_id(hass)
    assert _device_id_for_ip(hass, "10.0.0.99") is None
    assert _device_id_for_ip(hass, None) is None


async def test_webhook_button_event_carries_device_id(
    hass: HomeAssistant,
    aioclient_mock: AiohttpClientMocker,
    mock_config_entry,
) -> None:
    """A BUTTON_CLICK from a known TV IP enriches the event with device_id."""
    await _setup(hass, aioclient_mock, mock_config_entry)

    events = []
    hass.bus.async_listen(EVENT_BUTTON_PRESS, lambda e: events.append(e))

    req = _FakeRequest(
        "192.0.2.10", "test-secret-abc123",
        {"level": "ACTION", "message": "BUTTON_CLICK:play"},
    )
    resp = await handle_webhook_log(hass, WEBHOOK_ID, req)
    await hass.async_block_till_done()

    assert resp.status == 200
    assert len(events) == 1
    assert events[0].data["action"] == "play"
    assert events[0].data["device_id"] == _device_id(hass)
