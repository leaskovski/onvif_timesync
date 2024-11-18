"""Constants for onvif_timesync"""
from homeassistant.const import Platform

NAME = "ONVIF Time Synchroniser"
DOMAIN = "onvif_timesync"

PLATFORMS = [Platform.SENSOR]

SERVICE_NAME = "timesync"

ATTR_ADDRESS = "Address"
ATTR_PORT = "Port"
ATTR_USER = "Username"
ATTR_PWD = "Password"