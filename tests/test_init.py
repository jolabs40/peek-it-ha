"""Tests for the integration setup/unload, migration and services registration."""
from __future__ import annotations

from homeassistant.core import HomeAssistant
from homeassistant.helpers import issue_registry as ir
from pytest_homeassistant_custom_component.test_util.aiohttp import (
    AiohttpClientMocker,
)

from custom_components.peek_it_ha.const import (
    CONF_WEBHOOK_SECRET,
    DOMAIN,
    ISSUE_ANDROIDTV_MISSING,
)


def _ok_status() -> dict:
    return {
        "api_key_required": False,
        "api_key_valid": True,
        "permissions": {
            "overlay": True,
            "accessibility": False,
            "microphone": True,
        },
    }


async def test_setup_entry_registers_services(
    hass: HomeAssistant,
    aioclient_mock: AiohttpClientMocker,
    mock_config_entry,
) -> None:
    """All four domain services are registered on setup."""
    aioclient_mock.get("http://192.0.2.10:8081/api/status", json=_ok_status())
    mock_config_entry.add_to_hass(hass)

    assert await hass.config_entries.async_setup(mock_config_entry.entry_id)
    await hass.async_block_till_done()

    for service in ("notify", "tts", "tts_stop", "get_templates"):
        assert hass.services.has_service(DOMAIN, service), service


async def test_setup_migrates_missing_webhook_secret(
    hass: HomeAssistant,
    aioclient_mock: AiohttpClientMocker,
    legacy_config_entry,
) -> None:
    """A pre-1.1.0 entry without a secret gets one auto-generated."""
    aioclient_mock.get("http://192.0.2.11:8081/api/status", json=_ok_status())
    legacy_config_entry.add_to_hass(hass)

    assert CONF_WEBHOOK_SECRET not in legacy_config_entry.data
    assert await hass.config_entries.async_setup(legacy_config_entry.entry_id)
    await hass.async_block_till_done()

    secret = legacy_config_entry.data.get(CONF_WEBHOOK_SECRET)
    assert secret and len(secret) > 20  # token_urlsafe(32) is ~43 chars


async def test_unload_entry_cleans_state(
    hass: HomeAssistant,
    aioclient_mock: AiohttpClientMocker,
    mock_config_entry,
) -> None:
    """Unloading the last entry tears down services and shared state."""
    aioclient_mock.get("http://192.0.2.10:8081/api/status", json=_ok_status())
    mock_config_entry.add_to_hass(hass)

    assert await hass.config_entries.async_setup(mock_config_entry.entry_id)
    await hass.async_block_till_done()
    assert hass.services.has_service(DOMAIN, "notify")

    assert await hass.config_entries.async_unload(mock_config_entry.entry_id)
    await hass.async_block_till_done()
    assert not hass.services.has_service(DOMAIN, "notify")


async def test_androidtv_repair_issue_created(
    hass: HomeAssistant,
    aioclient_mock: AiohttpClientMocker,
    mock_config_entry,
) -> None:
    """When AndroidTV is not installed, a repair issue is registered."""
    aioclient_mock.get("http://192.0.2.10:8081/api/status", json=_ok_status())
    mock_config_entry.add_to_hass(hass)

    assert await hass.config_entries.async_setup(mock_config_entry.entry_id)
    await hass.async_block_till_done()

    registry = ir.async_get(hass)
    assert registry.async_get_issue(DOMAIN, ISSUE_ANDROIDTV_MISSING) is not None
