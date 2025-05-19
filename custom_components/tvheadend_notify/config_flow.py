# config_flow.py für TVHeadend Notify 
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.const import CONF_URL, CONF_USERNAME, CONF_PASSWORD
from .const import DOMAIN

class TVHeadendConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for TVHeadend Notify."""

    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_LOCAL_POLL

    async def async_step_user(self, user_input=None):
        errors = {}
        if user_input is not None:
            return self.async_create_entry(title="TVHeadend", data=user_input)

        data_schema = vol.Schema({
            vol.Required(CONF_URL): str,
            vol.Required(CONF_USERNAME): str,
            vol.Required(CONF_PASSWORD): str,
        })
        return self.async_show_form(
            step_id="user",
            data_schema=data_schema,
            errors=errors,
        ) 