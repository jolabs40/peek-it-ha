"""Tests for the config_flow."""
from __future__ import annotations

from ipaddress import ip_address

import pytest
from homeassistant import config_entries, data_entry_flow
from homeassistant.components.zeroconf import ZeroconfServiceInfo
from homeassistant.core import HomeAssistant
from pytest_homeassistant_custom_component.test_util.aiohttp import (
    AiohttpClientMocker,
)

from custom_components.peek_it_ha.const import (
    CONF_API_KEY,
    CONF_IP_ADDRESS,
    CONF_NAME,
    CONF_PAIR_CODE,
    CONF_PORT,
    CONF_WEBHOOK_SECRET,
    DEFAULT_PORT,
    DOMAIN,
)


def _zeroconf_info(host: str = "192.0.2.10", port: int = DEFAULT_PORT,
                   name: str = "Living Room TV") -> ZeroconfServiceInfo:
    return ZeroconfServiceInfo(
        ip_address=ip_address(host),
        ip_addresses=[ip_address(host)],
        port=port,
        hostname=f"{name}.local.",
        type="_peekit._tcp.local.",
        name=f"{name}._peekit._tcp.local.",
        properties={},
    )


@pytest.mark.usefixtures("mock_setup_entry")
async def test_user_flow_success(
    hass: HomeAssistant, aioclient_mock: AiohttpClientMocker
) -> None:
    """The manual user flow stores a webhook secret and posts the welcome."""
    aioclient_mock.get(
        "http://192.0.2.10:8081/api/status",
        json={"api_key_required": False, "api_key_valid": True},
    )
    aioclient_mock.post(
        "http://192.0.2.10:8081/api/notify",
        status=200,
        text="ok",
    )

    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": config_entries.SOURCE_USER}
    )
    assert result["type"] == data_entry_flow.FlowResultType.FORM

    result2 = await hass.config_entries.flow.async_configure(
        result["flow_id"],
        user_input={
            CONF_IP_ADDRESS: "192.0.2.10",
            CONF_PORT: 8081,
            CONF_NAME: "Living Room TV",
            CONF_PAIR_CODE: "",
        },
    )
    assert result2["type"] == data_entry_flow.FlowResultType.CREATE_ENTRY
    assert result2["title"] == "Living Room TV"
    assert result2["data"][CONF_IP_ADDRESS] == "192.0.2.10"
    assert result2["data"][CONF_WEBHOOK_SECRET]  # secret was generated


@pytest.mark.usefixtures("mock_setup_entry")
async def test_user_flow_cannot_connect(
    hass: HomeAssistant, aioclient_mock: AiohttpClientMocker
) -> None:
    """A 500 from the TV surfaces as a cannot_connect error."""
    aioclient_mock.get(
        "http://192.0.2.10:8081/api/status", status=500, text="boom"
    )

    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": config_entries.SOURCE_USER}
    )
    result2 = await hass.config_entries.flow.async_configure(
        result["flow_id"],
        user_input={
            CONF_IP_ADDRESS: "192.0.2.10",
            CONF_PORT: 8081,
            CONF_NAME: "Living Room TV",
            CONF_PAIR_CODE: "",
        },
    )
    assert result2["type"] == data_entry_flow.FlowResultType.FORM
    assert result2["errors"] == {"base": "cannot_connect"}


@pytest.mark.usefixtures("mock_setup_entry")
async def test_user_flow_auth_required(
    hass: HomeAssistant, aioclient_mock: AiohttpClientMocker
) -> None:
    """HTTP 401 from /api/status maps to auth_required."""
    aioclient_mock.get(
        "http://192.0.2.10:8081/api/status", status=401, text="unauthorized"
    )

    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": config_entries.SOURCE_USER}
    )
    result2 = await hass.config_entries.flow.async_configure(
        result["flow_id"],
        user_input={
            CONF_IP_ADDRESS: "192.0.2.10",
            CONF_PORT: 8081,
            CONF_NAME: "Living Room TV",
            CONF_PAIR_CODE: "",
        },
    )
    assert result2["type"] == data_entry_flow.FlowResultType.FORM
    assert result2["errors"] == {"base": "auth_required"}


@pytest.mark.usefixtures("mock_setup_entry")
async def test_user_flow_auth_required_via_payload(
    hass: HomeAssistant, aioclient_mock: AiohttpClientMocker
) -> None:
    """200 + api_key_required & not key_valid also maps to auth_required."""
    aioclient_mock.get(
        "http://192.0.2.10:8081/api/status",
        json={"api_key_required": True, "api_key_valid": False},
    )

    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": config_entries.SOURCE_USER}
    )
    result2 = await hass.config_entries.flow.async_configure(
        result["flow_id"],
        user_input={
            CONF_IP_ADDRESS: "192.0.2.10",
            CONF_PORT: 8081,
            CONF_NAME: "Living Room TV",
            CONF_PAIR_CODE: "",
        },
    )
    assert result2["type"] == data_entry_flow.FlowResultType.FORM
    assert result2["errors"] == {"base": "auth_required"}


@pytest.mark.usefixtures("mock_setup_entry")
async def test_zeroconf_flow_success(
    hass: HomeAssistant, aioclient_mock: AiohttpClientMocker
) -> None:
    """Zeroconf flow opens the confirm step and creates an entry on submit."""
    aioclient_mock.get(
        "http://192.0.2.10:8081/api/status",
        json={"api_key_required": False, "api_key_valid": True},
    )
    aioclient_mock.post(
        "http://192.0.2.10:8081/api/notify", status=200, text="ok"
    )

    result = await hass.config_entries.flow.async_init(
        DOMAIN,
        context={"source": config_entries.SOURCE_ZEROCONF},
        data=_zeroconf_info(),
    )
    assert result["type"] == data_entry_flow.FlowResultType.FORM
    assert result["step_id"] == "zeroconf_confirm"

    result2 = await hass.config_entries.flow.async_configure(
        result["flow_id"], user_input={CONF_NAME: "Living Room TV"}
    )
    assert result2["type"] == data_entry_flow.FlowResultType.CREATE_ENTRY
    assert result2["data"][CONF_WEBHOOK_SECRET]


@pytest.mark.usefixtures("mock_setup_entry")
async def test_zeroconf_auth_required_branch(
    hass: HomeAssistant, aioclient_mock: AiohttpClientMocker
) -> None:
    """Zeroconf detects 401 and routes through zeroconf_confirm_auth."""
    aioclient_mock.get(
        "http://192.0.2.10:8081/api/status", status=401, text="unauthorized"
    )

    result = await hass.config_entries.flow.async_init(
        DOMAIN,
        context={"source": config_entries.SOURCE_ZEROCONF},
        data=_zeroconf_info(),
    )
    assert result["type"] == data_entry_flow.FlowResultType.FORM
    assert result["step_id"] == "zeroconf_confirm_auth"

    # Now retry with a pairing code : /api/pair returns the real key, then
    # /api/status with that key validates and the entry is created.
    aioclient_mock.clear_requests()
    aioclient_mock.post(
        "http://192.0.2.10:8081/api/pair",
        json={"status": "ok", "api_key": "good-key"},
    )
    aioclient_mock.get(
        "http://192.0.2.10:8081/api/status",
        json={"api_key_required": True, "api_key_valid": True},
    )
    aioclient_mock.post(
        "http://192.0.2.10:8081/api/notify", status=200, text="ok"
    )

    result2 = await hass.config_entries.flow.async_configure(
        result["flow_id"],
        user_input={CONF_NAME: "Living Room TV", CONF_PAIR_CODE: "123456"},
    )
    assert result2["type"] == data_entry_flow.FlowResultType.CREATE_ENTRY
    assert result2["data"][CONF_API_KEY] == "good-key"


async def test_zeroconf_aborts_already_configured(
    hass: HomeAssistant, mock_config_entry
) -> None:
    """A second discovery for the same host aborts with already_configured."""
    mock_config_entry.add_to_hass(hass)

    result = await hass.config_entries.flow.async_init(
        DOMAIN,
        context={"source": config_entries.SOURCE_ZEROCONF},
        data=_zeroconf_info(host="192.0.2.10"),
    )
    assert result["type"] == data_entry_flow.FlowResultType.ABORT
    assert result["reason"] == "already_configured"


@pytest.mark.usefixtures("mock_setup_entry")
async def test_welcome_notification_includes_secret(
    hass: HomeAssistant, aioclient_mock: AiohttpClientMocker
) -> None:
    """The welcome notification payload must carry the new webhook_secret."""
    aioclient_mock.get(
        "http://192.0.2.10:8081/api/status",
        json={"api_key_required": False, "api_key_valid": True},
    )
    aioclient_mock.post(
        "http://192.0.2.10:8081/api/notify", status=200, text="ok"
    )

    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": config_entries.SOURCE_USER}
    )
    result2 = await hass.config_entries.flow.async_configure(
        result["flow_id"],
        user_input={
            CONF_IP_ADDRESS: "192.0.2.10",
            CONF_PORT: 8081,
            CONF_NAME: "Living Room TV",
            CONF_PAIR_CODE: "",
        },
    )
    assert result2["type"] == data_entry_flow.FlowResultType.CREATE_ENTRY

    posted = [c for c in aioclient_mock.mock_calls if c[0].lower() == "post"]
    assert posted, "No welcome notification was POSTed"
    payload = posted[-1][2]
    assert payload["webhook_secret"] == result2["data"][CONF_WEBHOOK_SECRET]
