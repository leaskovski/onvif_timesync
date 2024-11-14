# ONVIF_TimeSync
A Home Assistant custom component that allows a ONVIF Time Sync service to be created and called through an automation.

## Installation
The service can be installed and used by carrying out the following steps:
1. Use HACS to add the custom repo, and then install the customer component into Home Assistant.
2. Once installed, edit your configuration.yaml file and add the following...

```
# configuration.yaml entry
onvif_timesync.timesync:
```

3. Reload Home Assistant for the customer component to be loaded up.
4. Use an automation to call the onvif_timesync.timesync service with the following data...

```
service: onvif_timesync.timesync
data:
  Address: 192.168.0.108
  Port: 2020
  Username: <user>
  Password: <password>
```
