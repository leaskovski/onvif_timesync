import voluptuous as vol
from typing import Any
from homeassistant.config_entries import ConfigFlow, ConfigFlowResult
from .const import DOMAIN


class onvifTimeSyncConfigFlow(ConfigFlow, domain=DOMAIN):
    """Config flow for ONVIF Time Sync Service."""
 
    VERSION = 1
  
    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Handle a flow initialized by the user."""
        if user_input is not None:
            return self.async_create_entry(
                title=DOMAIN,
                data={},
            )

        return self.async_show_form(step_id="user", data_schema=vol.Schema({}))
