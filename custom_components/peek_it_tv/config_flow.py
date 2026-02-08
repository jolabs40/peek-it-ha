"""Config flow pour peek-it TV."""
import logging
import aiohttp
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback
from .const import DOMAIN, CONF_IP_ADDRESS, CONF_NAME, CONF_PORT, DEFAULT_PORT

_LOGGER = logging.getLogger(__name__)


class PeekItConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Gère le flux de configuration."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Gestion de l'étape initiale (saisie IP + port)."""
        errors = {}

        if user_input is not None:
            ip = user_input[CONF_IP_ADDRESS]
            port = user_input.get(CONF_PORT, DEFAULT_PORT)
            valid = await _test_connection(ip, port)
            if valid:
                return self.async_create_entry(
                    title=user_input.get(CONF_NAME, "Android TV"),
                    data=user_input
                )
            else:
                errors["base"] = "cannot_connect"

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required(CONF_IP_ADDRESS): str,
                vol.Optional(CONF_PORT, default=DEFAULT_PORT): int,
                vol.Optional(CONF_NAME, default="TV Salon"): str,
            }),
            errors=errors,
        )

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        """Retourne le flux d'options."""
        return PeekItOptionsFlow(config_entry)


class PeekItOptionsFlow(config_entries.OptionsFlow):
    """Gère le flux d'options (engrenage)."""

    def __init__(self, config_entry):
        """Initialisation."""
        self._entry = config_entry

    async def async_step_init(self, user_input=None):
        """Menu principal : Paramètres, Templates ou Designer."""
        return self.async_show_menu(
            step_id="init",
            menu_options=["settings", "templates", "designer"],
        )

    async def async_step_settings(self, user_input=None):
        """Formulaire de modification IP/port/nom."""
        errors = {}

        if user_input is not None:
            ip = user_input[CONF_IP_ADDRESS]
            port = user_input.get(CONF_PORT, DEFAULT_PORT)
            valid = await _test_connection(ip, port)
            if valid:
                self.hass.config_entries.async_update_entry(
                    self._entry, data=user_input
                )
                await self.hass.config_entries.async_reload(self._entry.entry_id)
                return self.async_create_entry(data={})
            else:
                errors["base"] = "cannot_connect"

        current = self._entry.data
        return self.async_show_form(
            step_id="settings",
            data_schema=vol.Schema({
                vol.Required(CONF_IP_ADDRESS, default=current.get(CONF_IP_ADDRESS, "")): str,
                vol.Optional(CONF_PORT, default=current.get(CONF_PORT, DEFAULT_PORT)): int,
                vol.Optional(CONF_NAME, default=current.get(CONF_NAME, "TV Salon")): str,
            }),
            errors=errors,
        )

    async def async_step_templates(self, user_input=None):
        """Affiche la liste des templates de la Box."""
        if user_input is not None:
            return self.async_create_entry(data={})

        templates_info = await self._fetch_templates()

        return self.async_show_form(
            step_id="templates",
            data_schema=vol.Schema({}),
            description_placeholders={"templates_info": templates_info},
        )

    async def async_step_designer(self, user_input=None):
        """Affiche le lien vers le Designer web."""
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
        """Récupère et formate la liste des templates depuis la Box."""
        ip = self._entry.data.get(CONF_IP_ADDRESS)
        port = self._entry.data.get(CONF_PORT, DEFAULT_PORT)
        url = f"http://{ip}:{port}/api/templates/list"

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, timeout=aiohttp.ClientTimeout(total=5)) as response:
                    if response.status != 200:
                        return f"Erreur HTTP {response.status}"
                    data = await response.json()
        except Exception as e:
            return f"Connexion impossible : {e}"

        sections = []

        # Officiels
        official = data.get("official", [])
        if official:
            parts = ["**OFFICIELS**"]
            for t in official:
                parts.append(self._format_template(t))
            sections.append("\n\n".join(parts))

        # Custom
        custom = data.get("custom", [])
        if custom:
            parts = ["**CUSTOM**"]
            for t in custom:
                parts.append(self._format_template(t))
            sections.append("\n\n".join(parts))

        # Brouillons
        draft = data.get("draft", [])
        if draft:
            parts = ["**BROUILLONS**"]
            for t in draft:
                name = t.get("filename", t) if isinstance(t, dict) else t
                name = name.rsplit(".", 1)[0] if "." in name else name
                parts.append(f"**{name}**")
            sections.append("\n\n".join(parts))

        if not sections:
            return "Aucun template disponible"

        return "\n\n---\n\n".join(sections)

    @staticmethod
    def _format_template(t):
        """Formate un template : ligne 1 = nom [params], ligne 2 = ID copiable."""
        if isinstance(t, str):
            name = t.rsplit(".", 1)[0] if "." in t else t
            return f"**{name}**"
        filename = t.get("filename", "?")
        name = filename.rsplit(".", 1)[0] if "." in filename else filename
        tid = t.get("id", "")
        params = t.get("params", [])
        # Ligne 1 : nom + [params]
        if params:
            line1 = f"**{name}** [{'; '.join(params)}]"
        else:
            line1 = f"**{name}**"
        # Ligne 2 : ID en code block pour copie facile
        if tid:
            return f"{line1}  \n`{tid}`"
        return line1


async def _test_connection(ip, port):
    """Vérifie si l'app répond sur le port configuré."""
    url = f"http://{ip}:{port}/api/status"
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=aiohttp.ClientTimeout(total=3)) as response:
                return response.status == 200
    except Exception:
        return False
