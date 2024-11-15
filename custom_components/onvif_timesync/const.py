"""Constants for onvif_timesync"""
from logging import Logger, getLogger

from homeassistant.components.sensor import SensorDeviceClass

LOGGER: Logger = getLogger(__package__)

NAME = "ONVIF Time Synchroniser"
DOMAIN = "onvif_timesync"

ATTR_ADDRESS = "Address"
ATTR_PORT = "Port"
ATTR_USER = "Username"
ATTR_PWD = "Password"