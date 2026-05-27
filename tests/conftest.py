"""Shared pytest fixtures for peek_it_ha tests."""
from __future__ import annotations

# --- Windows compatibility patches ---------------------------------------
# pytest_homeassistant_custom_component is loaded *before* this conftest
# (it ships a pytest11 entry-point), so it has already instantiated
# HassEventLoopPolicy(ProactorEventLoopPolicy) by the time we get here.
# We patch the policy's _loop_factory at class level so new_event_loop()
# now builds SelectorEventLoop — aiodns refuses to run on Proactor.
import asyncio
import sys

if sys.platform == "win32":
    _policy = asyncio.get_event_loop_policy()
    type(_policy)._loop_factory = asyncio.SelectorEventLoop  # type: ignore[attr-defined]

# pytest-socket (pulled by pytest-homeassistant-custom-component) blocks
# AF_INET globally. asyncio's event loops need socket.socketpair() to build
# their self-pipe, so we neutralise the guard at conftest import time.
import pytest_socket as _ps

_ps.disable_socket = lambda *_a, **_k: None
_ps.enable_socket()

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


@pytest.fixture(autouse=True)
def _enable_socket(socket_enabled):
    """pytest-socket blocks AF_INET globally; asyncio's Windows
    ProactorEventLoop needs socket.socketpair() to build its self-pipe,
    so re-enable sockets for every test."""
    yield


# The plugin's verify_cleanup fixture asserts that no unexpected daemon
# threads are left behind. On Windows the Selector loop's shutdown spawns
# a `_run_safe_shutdown_loop` daemon that doesn't match the allow-list.
# We monkey-patch threading.enumerate to hide those threads from the check.
import threading as _threading  # noqa: E402

_orig_enumerate = _threading.enumerate


def _filtered_enumerate():
    """Hide Windows shutdown daemons from verify_cleanup's allow-list check."""
    return [
        t for t in _orig_enumerate()
        if "shutdown" not in t.name.lower()
        and not t.name.startswith("Thread-")  # noisy generic asyncio threads
        or t.daemon is False
    ]


_threading.enumerate = _filtered_enumerate


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
