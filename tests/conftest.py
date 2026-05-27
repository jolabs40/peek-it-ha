"""Shared pytest fixtures for peek_it_ha tests."""
from __future__ import annotations

from collections.abc import Generator
from unittest.mock import patch

import pytest
from pytest_homeassistant_custom_component.common import MockConfigEntry

from custom_components.peek_it_ha.const import (
    CONF_API_KEY,
    CONF_IP_ADDRESS,
    CONF_NAME,
    CONF_PORT,
    CONF_WEBHOOK_SECRET,
    DEFAULT_PORT,
    DOMAIN,
)


pytest_plugins = "pytest_homeassistant_custom_component"


@pytest.fixture(autouse=True)
def auto_enable_custom_integrations(enable_custom_integrations):
    """Enable loading of the local custom component."""
    yield


@pytest.fixture
def mock_setup_entry() -> Generator[None, None, None]:
    """Skip the actual setup so config_flow tests stay fast."""
    with patch(
        "custom_components.peek_it_ha.async_setup_entry",
        return_value=True,
    ):
        yield


@pytest.fixture
def mock_config_entry() -> MockConfigEntry:
    """A typical peek_it_ha config entry — webhook secret already provisioned."""
    return MockConfigEntry(
        domain=DOMAIN,
        title="Living Room TV",
        data={
            CONF_IP_ADDRESS: "192.0.2.10",
            CONF_PORT: DEFAULT_PORT,
            CONF_NAME: "Living Room TV",
            CONF_API_KEY: "",
            CONF_WEBHOOK_SECRET: "test-secret-abc123",
        },
        unique_id="192.0.2.10",
    )


@pytest.fixture
def legacy_config_entry() -> MockConfigEntry:
    """A pre-1.1.0 entry with no webhook secret yet (used to test migration)."""
    return MockConfigEntry(
        domain=DOMAIN,
        title="Old TV",
        data={
            CONF_IP_ADDRESS: "192.0.2.11",
            CONF_PORT: DEFAULT_PORT,
            CONF_NAME: "Old TV",
            CONF_API_KEY: "",
        },
        unique_id="192.0.2.11",
    )


@pytest.fixture
def status_payload() -> dict:
    """A minimal valid /api/status payload."""
    return {
        "api_key_required": False,
        "api_key_valid": True,
        "permissions": {
            "overlay": True,
            "accessibility": False,
            "microphone": True,
        },
    }
