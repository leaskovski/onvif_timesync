from homeassistant import config_entries
from .const import DOMAIN


class onvifTimeSyncConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Example config flow."""
    # The schema version of the entries that it creates
    # Home Assistant will call your migrate method if the version changes
    VERSION = 1
    MINOR_VERSION = 0
  
    async def async_step_user(self, user_input=None):
        """Handle user step."""