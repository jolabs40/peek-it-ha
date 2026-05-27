"""DataUpdateCoordinator for Peek-it [HA].

A single coordinator polls ``GET /api/status`` once per
:data:`STATUS_SCAN_INTERVAL_SECONDS`. All entities (status, permission
sensors, notify, buttons) read from the same snapshot — there is exactly
one outbound HTTP request per TV per interval, regardless of how many
entities are exposed.
"""
from __future__ import annotations

import asyncio
import logging
from datetime import timedelta
from typing import Any

import aiohttp
from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.update_coordinator import (
    DataUpdateCoordinator,
    UpdateFailed,
)

from .const import (
    DOMAIN,
    STATUS_SCAN_INTERVAL_SECONDS,
    STATUS_TIMEOUT_SECONDS,
)

_LOGGER = logging.getLogger(__name__)


class PeekItCoordinator(DataUpdateCoordinator[dict[str, Any]]):
    """Polls /api/status and exposes the JSON snapshot to all platforms."""

    def __init__(
        self,
        hass: HomeAssistant,
        *,
        ip: str,
        port: int,
        api_key: str,
        name: str,
    ) -> None:
        super().__init__(
            hass,
            _LOGGER,
            name=f"{DOMAIN}_{ip}",
            update_interval=timedelta(seconds=STATUS_SCAN_INTERVAL_SECONDS),
        )
        self.ip = ip
        self.port = port
        self.api_key = api_key
        self.device_name = name
        self.is_online: bool = False

    @property
    def status_url(self) -> str:
        return f"http://{self.ip}:{self.port}/api/status"

    @property
    def designer_url(self) -> str:
        return f"http://{self.ip}:{self.port}/"

    def _headers(self) -> dict[str, str]:
        return {"X-API-Key": self.api_key} if self.api_key else {}

    async def _async_update_data(self) -> dict[str, Any]:
        """Fetch the status snapshot."""
        session = async_get_clientsession(self.hass)
        try:
            async with session.get(
                self.status_url,
                headers=self._headers(),
                timeout=aiohttp.ClientTimeout(total=STATUS_TIMEOUT_SECONDS),
            ) as response:
                if response.status != 200:
                    self.is_online = False
                    raise UpdateFailed(
                        f"HTTP {response.status} from {self.status_url}"
                    )
                self.is_online = True
                return await response.json()
        except (aiohttp.ClientError, asyncio.TimeoutError) as err:
            self.is_online = False
            raise UpdateFailed(f"Connection error: {err}") from err
