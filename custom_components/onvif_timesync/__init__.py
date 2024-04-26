DOMAIN = "onvif_timesync"

ATTR_NAME = "name"
DEFAULT_NAME = "TimeSync"

from onvif import ONVIFCamera
import datetime

def setup(hass, config):
    """Set up is called when Home Assistant is loading our component."""

    def timeSync_handler(call):
        """Handle the service call."""
        name = call.data.get(ATTR_NAME, DEFAULT_NAME)
        hass.states.set("onvif_timesync_service.timesync", name)
        
        mycam = ONVIFCamera('192.168.0.108', 2020, 'CamViewer', 'TylersCam', '/usr/local/bin/onvif_timesync/python-onvif-zeep/wsdl')
        
        time_params = mycam.devicemgmt.create_type('SetSystemDateAndTime')
        time_params.DateTimeType = 'Manual'
        time_params.DaylightSavings = True
        
        TZ = {'TZ':datetime.datetime.now().astimezone().tzname()}
        time_params.TimeZone = TZ
        
        today = datetime.datetime.now()
        
        Date = {'Year':today.year,'Month':today.month,'Day':today.day}
        Time = {'Hour':today.hour,'Minute':today.minute,'Second':today.second}
        
        UTC = {'Date':Date,'Time':Time}
        time_params.UTCDateTime = UTC
        
        mycam.devicemgmt.SetSystemDateAndTime(time_params)

    
    hass.services.register(DOMAIN, "timesync", timeSync_handler)

    # Return boolean to indicate that initialization was successful.
    return True
