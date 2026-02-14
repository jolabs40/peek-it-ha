"""Config flow for Peek-it [HA]."""
import logging
import aiohttp
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback
from .const import DOMAIN, CONF_IP_ADDRESS, CONF_NAME, CONF_PORT, CONF_API_KEY, CONF_ATV_ENTITY, DEFAULT_PORT

_LOGGER = logging.getLogger(__name__)


class PeekItConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle the configuration flow."""

    VERSION = 1

    async def async_step_zeroconf(self, discovery_info):
        """Device discovered automatically via zeroconf/NSD."""
        host = str(discovery_info.host)
        port = discovery_info.port or DEFAULT_PORT
        name = discovery_info.name.split(".")[0]

        # Avoid duplicates
        self._async_abort_entries_match({CONF_IP_ADDRESS: host})

        # Test connection
        result = await _test_connection(host, port)

        self._discovered_ip = host
        self._discovered_port = port
        self._discovered_name = name

        self.context["title_placeholders"] = {"name": name, "host": host}

        if result == "auth_required":
            return await self.async_step_zeroconf_confirm_auth()
        elif result == "ok":
            return await self.async_step_zeroconf_confirm()
        else:
            return self.async_abort(reason="cannot_connect")

    async def async_step_zeroconf_confirm(self, user_input=None):
        """Confirmation after automatic discovery."""
        if user_input is not None:
            name = user_input.get(CONF_NAME, self._discovered_name)
            data = {
                CONF_IP_ADDRESS: self._discovered_ip,
                CONF_PORT: self._discovered_port,
                CONF_NAME: name,
                CONF_API_KEY: "",
            }
            await _send_welcome_notification(
                self._discovered_ip, self._discovered_port, "", name
            )
            return self.async_create_entry(title=name, data=data)

        return self.async_show_form(
            step_id="zeroconf_confirm",
            data_schema=vol.Schema({
                vol.Optional(CONF_NAME, default=self._discovered_name): str,
            }),
            description_placeholders={
                "host": self._discovered_ip,
                "port": str(self._discovered_port),
            },
        )

    async def async_step_zeroconf_confirm_auth(self, user_input=None):
        """Confirmation with API key required."""
        errors = {}
        if user_input is not None:
            api_key = user_input.get(CONF_API_KEY, "")
            result = await _test_connection(
                self._discovered_ip, self._discovered_port, api_key
            )
            if result == "ok":
                name = user_input.get(CONF_NAME, self._discovered_name)
                data = {
                    CONF_IP_ADDRESS: self._discovered_ip,
                    CONF_PORT: self._discovered_port,
                    CONF_NAME: name,
                    CONF_API_KEY: api_key,
                }
                await _send_welcome_notification(
                    self._discovered_ip, self._discovered_port, api_key, name
                )
                return self.async_create_entry(title=name, data=data)
            else:
                errors["base"] = "auth_required"

        return self.async_show_form(
            step_id="zeroconf_confirm_auth",
            data_schema=vol.Schema({
                vol.Optional(CONF_NAME, default=self._discovered_name): str,
                vol.Required(CONF_API_KEY): str,
            }),
            description_placeholders={
                "host": self._discovered_ip,
                "port": str(self._discovered_port),
            },
            errors=errors,
        )

    async def async_step_user(self, user_input=None):
        """Handle the initial step (IP + port + API key)."""
        errors = {}

        if user_input is not None:
            ip = user_input[CONF_IP_ADDRESS]
            port = user_input.get(CONF_PORT, DEFAULT_PORT)
            api_key = user_input.get(CONF_API_KEY, "")
            result = await _test_connection(ip, port, api_key)
            if result == "ok":
                name = user_input.get(CONF_NAME, "Android TV")
                await _send_welcome_notification(ip, port, api_key, name)
                return self.async_create_entry(
                    title=name,
                    data=user_input
                )
            elif result == "auth_required":
                errors["base"] = "auth_required"
            else:
                errors["base"] = "cannot_connect"

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required(CONF_IP_ADDRESS): str,
                vol.Optional(CONF_PORT, default=DEFAULT_PORT): int,
                vol.Optional(CONF_NAME, default="Living Room TV"): str,
                vol.Optional(CONF_API_KEY, default=""): str,
                vol.Optional(CONF_ATV_ENTITY, default=""): str,
            }),
            errors=errors,
        )

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        """Return the options flow handler."""
        return PeekItOptionsFlow(config_entry)


class PeekItOptionsFlow(config_entries.OptionsFlow):
    """Handle the options flow (gear icon)."""

    def __init__(self, config_entry):
        """Initialize."""
        self._entry = config_entry

    async def async_step_init(self, user_input=None):
        """Main menu: Settings, Templates or Designer."""
        return self.async_show_menu(
            step_id="init",
            menu_options=["settings", "templates", "designer"],
        )

    async def async_step_settings(self, user_input=None):
        """Edit IP/port/name/API key."""
        errors = {}

        if user_input is not None:
            ip = user_input[CONF_IP_ADDRESS]
            port = user_input.get(CONF_PORT, DEFAULT_PORT)
            api_key = user_input.get(CONF_API_KEY, "")
            result = await _test_connection(ip, port, api_key)
            if result == "ok":
                name = user_input.get(CONF_NAME, "Living Room TV")
                await _send_welcome_notification(ip, port, api_key, name)
                self.hass.config_entries.async_update_entry(
                    self._entry, data=user_input
                )
                await self.hass.config_entries.async_reload(self._entry.entry_id)
                return self.async_create_entry(data={})
            elif result == "auth_required":
                errors["base"] = "auth_required"
            else:
                errors["base"] = "cannot_connect"

        current = self._entry.data
        return self.async_show_form(
            step_id="settings",
            data_schema=vol.Schema({
                vol.Required(CONF_IP_ADDRESS, default=current.get(CONF_IP_ADDRESS, "")): str,
                vol.Optional(CONF_PORT, default=current.get(CONF_PORT, DEFAULT_PORT)): int,
                vol.Optional(CONF_NAME, default=current.get(CONF_NAME, "Living Room TV")): str,
                vol.Optional(CONF_API_KEY, default=current.get(CONF_API_KEY, "")): str,
                vol.Optional(CONF_ATV_ENTITY, default=current.get(CONF_ATV_ENTITY, "")): str,
            }),
            errors=errors,
        )

    async def async_step_templates(self, user_input=None):
        """Display the template list from the TV."""
        if user_input is not None:
            return self.async_create_entry(data={})

        templates_info = await self._fetch_templates()

        return self.async_show_form(
            step_id="templates",
            data_schema=vol.Schema({}),
            description_placeholders={"templates_info": templates_info},
        )

    async def async_step_designer(self, user_input=None):
        """Show the link to the web Designer."""
        if user_input is not None:
            return self.async_create_entry(data={})

        ip = self._entry.data.get(CONF_IP_ADDRESS)
        port = self._entry.data.get(CONF_PORT, DEFAULT_PORT)
        designer_url = f"http://{ip}:{port}/"

        return self.async_show_form(
            step_id="designer",
            data_schema=vol.Schema({}),
            description_placeholders={"designer_url": designer_url},
        )

    async def _fetch_templates(self):
        """Fetch and format the template list from the TV."""
        ip = self._entry.data.get(CONF_IP_ADDRESS)
        port = self._entry.data.get(CONF_PORT, DEFAULT_PORT)
        api_key = self._entry.data.get(CONF_API_KEY, "")
        url = f"http://{ip}:{port}/api/templates/list"
        headers = {"X-API-Key": api_key} if api_key else {}

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, headers=headers, timeout=aiohttp.ClientTimeout(total=5)) as response:
                    if response.status != 200:
                        return f"HTTP Error {response.status}"
                    data = await response.json()
        except Exception as e:
            return f"Connection failed: {e}"

        sections = []

        official = data.get("official", [])
        if official:
            parts = ["**OFFICIAL**"]
            for t in official:
                parts.append(self._format_template(t))
            sections.append("\n\n".join(parts))

        custom = data.get("custom", [])
        if custom:
            parts = ["**CUSTOM**"]
            for t in custom:
                parts.append(self._format_template(t))
            sections.append("\n\n".join(parts))

        draft = data.get("draft", [])
        if draft:
            parts = ["**DRAFTS**"]
            for t in draft:
                name = t.get("filename", t) if isinstance(t, dict) else t
                name = name.rsplit(".", 1)[0] if "." in name else name
                parts.append(f"**{name}**")
            sections.append("\n\n".join(parts))

        if not sections:
            return "No templates available"

        return "\n\n---\n\n".join(sections)

    @staticmethod
    def _format_template(t):
        """Format a template: line 1 = name [params], line 2 = copyable ID."""
        if isinstance(t, str):
            name = t.rsplit(".", 1)[0] if "." in t else t
            return f"**{name}**"
        filename = t.get("filename", "?")
        name = filename.rsplit(".", 1)[0] if "." in filename else filename
        tid = t.get("id", "")
        params = t.get("params", [])
        if params:
            line1 = f"**{name}** [{'; '.join(params)}]"
        else:
            line1 = f"**{name}**"
        if tid:
            return f"{line1}  \n`{tid}`"
        return line1


async def _test_connection(ip, port, api_key=""):
    """Check if the app responds on the configured port.
    Returns: 'ok', 'auth_required' or 'failed'.
    Reads api_key_required and api_key_valid from /api/status.
    """
    url = f"http://{ip}:{port}/api/status"
    headers = {"X-API-Key": api_key} if api_key else {}
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, timeout=aiohttp.ClientTimeout(total=3)) as response:
                if response.status in (401, 403):
                    return "auth_required"
                if response.status == 200:
                    data = await response.json()
                    key_required = data.get("api_key_required", False)
                    key_valid = data.get("api_key_valid", True)
                    if key_required and not key_valid:
                        return "auth_required"
                    return "ok"
                return "failed"
    except Exception:
        return "failed"


async def _send_welcome_notification(ip, port, api_key="", name="TV"):
    """Send a welcome notification to the TV."""
    url = f"http://{ip}:{port}/api/notify"
    headers = {"X-API-Key": api_key} if api_key else {}

    payload = {
        "action": "DISPLAY",
        "duration": 8000,
        "source": "HA",
        "animationIn": "pop",
        "animationOut": "fade",
        "elements": [
            # Full-screen semi-transparent background
            {"type": "rect", "style": {
                "left": 0, "top": 0, "width": 100, "height": 100,
                "bgColor": "#DD000000", "radius": 0
            }},
            # Center rectangle with colored border
            {"type": "rect", "style": {
                "left": 20, "top": 15, "width": 60, "height": 70,
                "bgColor": "#F0141428", "radius": 20,
                "borderWidth": 3, "borderColor": "#18BCF2"
            }},
            # Decorative line (top)
            {"type": "rect", "style": {
                "left": 30, "top": 28, "width": 40, "height": 0.3,
                "bgColor": "#4018BCF2", "radius": 0
            }},
            # Decorative line (bottom)
            {"type": "rect", "style": {
                "left": 30, "top": 72, "width": 40, "height": 0.3,
                "bgColor": "#4018BCF2", "radius": 0
            }},
            # Home Assistant icon (large)
            {"type": "text", "content": "mdi:home-assistant", "style": {
                "left": 42, "top": 20, "width": 16, "height": 12,
                "size": 60, "color": "#18BCF2", "align": "center"
            }},
            # Check icon
            {"type": "text", "content": "mdi:check-circle", "style": {
                "left": 42, "top": 35, "width": 16, "height": 10,
                "size": 40, "color": "#00E676", "align": "center"
            }},
            # CONNECTION SUCCESSFUL text
            {"type": "text", "content": "CONNECTION SUCCESSFUL", "style": {
                "left": 25, "top": 47, "width": 50, "height": 7,
                "size": 28, "color": "#00E676", "align": "center", "weight": "bold"
            }},
            # Device name
            {"type": "text", "content": name, "style": {
                "left": 25, "top": 55, "width": 50, "height": 5,
                "size": 20, "color": "#FFFFFF", "align": "center"
            }},
            # TV icon (left)
            {"type": "text", "content": "mdi:television", "style": {
                "left": 30, "top": 63, "width": 10, "height": 8,
                "size": 28, "color": "#4CAF50", "align": "center"
            }},
            # Wi-Fi icon (center)
            {"type": "text", "content": "mdi:wifi", "style": {
                "left": 45, "top": 63, "width": 10, "height": 8,
                "size": 28, "color": "#18BCF2", "align": "center"
            }},
            # Shield-check icon (right)
            {"type": "text", "content": "mdi:shield-check", "style": {
                "left": 60, "top": 63, "width": 10, "height": 8,
                "size": 28, "color": "#FF9800", "align": "center"
            }},
            # Subtitle
            {"type": "text", "content": "Home Assistant \u00b7 Peek-it [HA]", "style": {
                "left": 25, "top": 74, "width": 50, "height": 5,
                "size": 14, "color": "#666666", "align": "center"
            }},
        ]
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload, headers=headers, timeout=5) as response:
                if response.status != 200:
                    _LOGGER.warning("Welcome notification: HTTP %s", response.status)
    except Exception as e:
        _LOGGER.warning("Welcome notification: %s", e)
