import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from onvif import ONVIFCamera
import datetime

_LOGGER = logging.getLogger(__name__)

from .const import (
    DOMAIN,
    SERVICE_NAME,
    ATTR_ADDRESS,
    ATTR_PORT,
    ATTR_USER,
    ATTR_PWD
)


def setup(hass: HomeAssistant, config: ConfigEntry) -> bool:
    """Set up is called when Home Assistant is loading our component."""

    def timeSync_handler(call):
        """Handle the service call."""

        # Get the details from the service call to use with the request
        address = call.data.get(ATTR_ADDRESS, '')
        port = call.data.get(ATTR_PORT, 2020)
        username = call.data.get(ATTR_USER, '')
        password = call.data.get(ATTR_PWD, '')

        if (address != "" and username != "" and password != ""): 

            path = hass.config.path("custom_components/onvif_timesync/wsdl")

            # Create an ONVIF camera object using the service call parameters
            mycam = ONVIFCamera(address, port, username, password, path)
    
            # Create a time object to use to set the time with
            time_params = mycam.devicemgmt.create_type('SetSystemDateAndTime')
            time_params.DateTimeType = 'Manual'
            time_params.DaylightSavings = True
    
            # Set the Timezone and the current time
            TZ = {'TZ':datetime.datetime.now().astimezone().tzname()}
            time_params.TimeZone = TZ
            today = datetime.datetime.now()
    
            # Load the time object up with all the details for the date, time and timezone
            Date = {'Year':today.year,'Month':today.month,'Day':today.day}
            Time = {'Hour':today.hour,'Minute':today.minute,'Second':today.second}
            UTC = {'Date':Date,'Time':Time}
            time_params.UTCDateTime = UTC
    
            # Set the cameras date and time
            mycam.devicemgmt.SetSystemDateAndTime(time_params)

    
    hass.services.register(DOMAIN, SERVICE_NAME, timeSync_handler)

    # Return boolean to indicate that initialization was successful.
    return True
