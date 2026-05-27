"""Tests for binary_sensor entities (status + permissions)."""
from __future__ import annotations

from homeassistant.const import STATE_OFF, STATE_ON
from homeassistant.core import HomeAssistant
from pytest_homeassistant_custom_component.test_util.aiohttp import (
    AiohttpClientMocker,
)


async def test_status_on_when_tv_responds(
    hass: HomeAssistant,
    aioclient_mock: AiohttpClientMocker,
    mock_config_entry,
    status_payload,
) -> None:
    aioclient_mock.get(
        "http://192.0.2.10:8081/api/status", json=status_payload
    )
    mock_config_entry.add_to_hass(hass)
    assert await hass.config_entries.async_setup(mock_config_entry.entry_id)
    await hass.async_block_till_done()

    state = hass.states.get("binary_sensor.living_room_tv")
    assert state is not None
    assert state.state == STATE_ON


async def test_status_off_on_connection_failure(
    hass: HomeAssistant,
    aioclient_mock: AiohttpClientMocker,
    mock_config_entry,
) -> None:
    aioclient_mock.get(
        "http://192.0.2.10:8081/api/status", status=500, text="boom"
    )
    mock_config_entry.add_to_hass(hass)
    assert await hass.config_entries.async_setup(mock_config_entry.entry_id)
    await hass.async_block_till_done()

    state = hass.states.get("binary_sensor.living_room_tv")
    assert state is not None
    assert state.state == STATE_OFF


async def test_permission_sensors_reflect_payload(
    hass: HomeAssistant,
    aioclient_mock: AiohttpClientMocker,
    mock_config_entry,
    status_payload,
) -> None:
    aioclient_mock.get(
        "http://192.0.2.10:8081/api/status", json=status_payload
    )
    mock_config_entry.add_to_hass(hass)
    assert await hass.config_entries.async_setup(mock_config_entry.entry_id)
    await hass.async_block_till_done()

    overlay = hass.states.get("binary_sensor.living_room_tv_overlay_permission")
    micro = hass.states.get("binary_sensor.living_room_tv_microphone_permission")
    a11y = hass.states.get("binary_sensor.living_room_tv_accessibility_permission")
    assert overlay is not None and overlay.state == STATE_ON
    assert micro is not None and micro.state == STATE_ON
    assert a11y is not None and a11y.state == STATE_OFF


async def test_designer_url_attribute(
    hass: HomeAssistant,
    aioclient_mock: AiohttpClientMocker,
    mock_config_entry,
    status_payload,
) -> None:
    aioclient_mock.get(
        "http://192.0.2.10:8081/api/status", json=status_payload
    )
    mock_config_entry.add_to_hass(hass)
    assert await hass.config_entries.async_setup(mock_config_entry.entry_id)
    await hass.async_block_till_done()

    state = hass.states.get("binary_sensor.living_room_tv")
    assert state is not None
    assert state.attributes["designer_url"] == "http://192.0.2.10:8081/"


async def test_single_poll_for_all_entities(
    hass: HomeAssistant,
    aioclient_mock: AiohttpClientMocker,
    mock_config_entry,
    status_payload,
) -> None:
    """The four binary sensors share one /api/status call (coordinator)."""
    aioclient_mock.get(
        "http://192.0.2.10:8081/api/status", json=status_payload
    )
    mock_config_entry.add_to_hass(hass)
    assert await hass.config_entries.async_setup(mock_config_entry.entry_id)
    await hass.async_block_till_done()

    status_calls = [
        c for c in aioclient_mock.mock_calls
        if c[0] == "get" and "/api/status" in str(c[1])
    ]
    # First refresh after setup. No additional polls per entity.
    assert len(status_calls) == 1
