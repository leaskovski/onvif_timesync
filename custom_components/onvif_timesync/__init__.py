import logging
from homeassistant.const import EVENT_HOMEASSISTANT_START, EVENT_HOMEASSISTANT_STOP
import homeassistant.helpers.config_validation as cv
from onvif import ONVIFCamera
import datetime

_LOGGER = logging.getLogger(__name__)

DOMAIN = "onvif_timesync"

ATTR_ADDRESS = "Address"
ATTR_PORT = "Port"
ATTR_USER = "Username"
ATTR_PWD = "Password"

DEFAULT_NAME = "TimeSync"


def setup(hass, config):
    """Set up is called when Home Assistant is loading our component."""

    def timeSync_handler(call):
        """Handle the service call."""

        # Get the details from the service call to use with the request
        address = call.data.get(ATTR_ADDRESS, '')
        port = call.data.get(ATTR_PORT, 2020)
        username = call.data.get(ATTR_USER, '')
        password = call.data.get(ATTR_PWD, '')

        # Create an ONVIF camera object using the service call parameters
        mycam = ONVIFCamera(address, port, username, password, '/usr/local/bin/onvif_timesync/python-onvif-zeep/wsdl')

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

    
    hass.services.register(DOMAIN, "timesync", timeSync_handler)

    # Return boolean to indicate that initialization was successful.
    return True
