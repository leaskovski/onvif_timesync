# ONVIF_TimeSync
A Home Assistant custom component that allows a ONVIF Time Sync service to be created and called through an automation.

## Installation
The service can be installed and used by carrying out the following steps:
1. Use HACS to add the custom repo, and then install the customer component into Home Assistant.
2. Restart Home Assistant so that the loaded HACS custom component is loaded in to HASS.
3. Go to the Settings then Devices & Services, and add the new service into HASS.
4. Use an automation to call the onvif_timesync.timesync service with the following data...

```
service: onvif_timesync.timesync
data:
  address: 192.168.0.108
  port: 2020
  username: <user>
  password: <password>
```
