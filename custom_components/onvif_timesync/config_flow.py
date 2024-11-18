from homeassistant.config_entries import ConfigFlow, ConfigFlowResult
from .const import DOMAIN


class onvifTimeSyncConfigFlow(ConfigFlow, domain=DOMAIN):
    """Config flow for ONVIF Time Sync Service."""
 
    VERSION = 1
  
    async def async_step_user(self, user_input=None):
        """Handle user step."""