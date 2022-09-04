# Temperature/Humidity Sensor

Standalone temperature/humidity sensor that logs periodically

* `INTERVAL` is the interval in seconds between sensor readings
* `DEVELOPER_MODE` boolean to indicate if this being updated over the USB connection
* `sensor.log` is the file that readings are logged to

## Development
`DEVELOPER_MODE` is enabled by putting a jumper between D2 and Ground.

When plugged into your computer only the USB exported filesystem is read-write. The
version running on the board is remounted as read-only by `boot.py`. You can use the 
`DEVELOPER_MODE` flag to change the behavior of your script
based on whether you have read-write access on the board or not.
