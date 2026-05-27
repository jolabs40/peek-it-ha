"""Shared HTTP helpers for Peek-it [HA] services and notify entity.

All call sites use the HA-managed aiohttp ClientSession and a small retry
loop so a transient ``ClientError`` does not silently drop a service call.
"""
from __future__ import annotations

import asyncio
import logging
from typing import Any

import aiohttp
from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from .const import HTTP_TIMEOUT_SECONDS, RETRY_BACKOFFS

_LOGGER = logging.getLogger(__name__)


async def async_post_json(
    hass: HomeAssistant,
    url: str,
    payload: dict[str, Any],
    *,
    headers: dict[str, str] | None = None,
    timeout: float = HTTP_TIMEOUT_SECONDS,
    context: str = "request",
) -> tuple[bool, int | None, str]:
    """POST JSON with retry on transient ClientError.

    Returns (ok, status_code, body_text). ``ok`` is True iff a 2xx response
    was received within the retry budget.
    """
    session = async_get_clientsession(hass)
    last_err: str = ""
    attempt = 0
    backoffs = (0.0, *RETRY_BACKOFFS)  # immediate first try + 2 retries

    while attempt < len(backoffs):
        wait = backoffs[attempt]
        if wait:
            await asyncio.sleep(wait)
        attempt += 1
        try:
            async with session.post(
                url,
                json=payload,
                headers=headers or {},
                timeout=aiohttp.ClientTimeout(total=timeout),
            ) as response:
                body = await response.text()
                if 200 <= response.status < 300:
                    return True, response.status, body
                # Non-2xx: don't retry (the TV explicitly answered)
                _LOGGER.error(
                    "%s failed (HTTP %s) on %s: %s",
                    context,
                    response.status,
                    url,
                    body[:200],
                )
                return False, response.status, body
        except (TimeoutError, aiohttp.ClientError) as err:
            last_err = str(err)
            _LOGGER.debug(
                "%s attempt %d on %s failed: %s", context, attempt, url, err
            )
            continue

    _LOGGER.error("%s gave up after %d attempts on %s: %s",
                  context, attempt, url, last_err)
    return False, None, last_err
