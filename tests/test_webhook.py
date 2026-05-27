"""Tests for the /api/webhook/peek_it_debug listener (security + dispatch)."""
from __future__ import annotations

from homeassistant.core import HomeAssistant
from homeassistant.setup import async_setup_component
from pytest_homeassistant_custom_component.test_util.aiohttp import (
    AiohttpClientMocker,
)


def _ok_status() -> dict:
    return {"api_key_required": False, "api_key_valid": True}


async def _setup(hass, aioclient_mock, entry) -> None:
    # Webhook component must be loaded for async_register
    await async_setup_component(hass, "webhook", {})
    aioclient_mock.get(
        "http://192.0.2.10:8081/api/status", json=_ok_status()
    )
    entry.add_to_hass(hass)
    assert await hass.config_entries.async_setup(entry.entry_id)
    await hass.async_block_till_done()


async def test_webhook_rejects_without_secret(
    hass: HomeAssistant,
    hass_client_no_auth,
    aioclient_mock: AiohttpClientMocker,
    mock_config_entry,
) -> None:
    await _setup(hass, aioclient_mock, mock_config_entry)
    client = await hass_client_no_auth()

    events = []
    hass.bus.async_listen("peekit_button_press",
                          lambda e: events.append(e))

    response = await client.post(
        "/api/webhook/peek_it_debug",
        json={"level": "ACTION", "message": "BUTTON_CLICK:overlay"},
    )
    assert response.status == 401
    await hass.async_block_till_done()
    assert not events


async def test_webhook_rejects_wrong_secret(
    hass: HomeAssistant,
    hass_client_no_auth,
    aioclient_mock: AiohttpClientMocker,
    mock_config_entry,
) -> None:
    await _setup(hass, aioclient_mock, mock_config_entry)
    client = await hass_client_no_auth()

    response = await client.post(
        "/api/webhook/peek_it_debug",
        json={"level": "ACTION", "message": "BUTTON_CLICK:overlay"},
        headers={"X-Peek-Secret": "wrong"},
    )
    assert response.status == 401


async def test_webhook_accepts_valid_secret_and_fires_event(
    hass: HomeAssistant,
    hass_client_no_auth,
    aioclient_mock: AiohttpClientMocker,
    mock_config_entry,
) -> None:
    await _setup(hass, aioclient_mock, mock_config_entry)
    client = await hass_client_no_auth()

    events = []
    hass.bus.async_listen("peekit_button_press",
                          lambda e: events.append(e))

    response = await client.post(
        "/api/webhook/peek_it_debug",
        json={"level": "ACTION", "message": "BUTTON_CLICK:overlay"},
        headers={"X-Peek-Secret": "test-secret-abc123"},
    )
    assert response.status == 200
    await hass.async_block_till_done()
    assert len(events) == 1
    assert events[0].data == {"action": "overlay"}


async def test_webhook_log_level_does_not_fire_event(
    hass: HomeAssistant,
    hass_client_no_auth,
    aioclient_mock: AiohttpClientMocker,
    mock_config_entry,
) -> None:
    await _setup(hass, aioclient_mock, mock_config_entry)
    client = await hass_client_no_auth()

    events = []
    hass.bus.async_listen("peekit_button_press",
                          lambda e: events.append(e))

    response = await client.post(
        "/api/webhook/peek_it_debug",
        json={"level": "WARN", "message": "low memory"},
        headers={"X-Peek-Secret": "test-secret-abc123"},
    )
    assert response.status == 200
    await hass.async_block_till_done()
    assert not events
