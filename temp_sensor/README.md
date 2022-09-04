# Temperature/Humidity Sensor

Standalone temperature/humidity sensor that logs periodically

* `INTERVAL` is the interval in seconds between sensor readings
* `DEVELOPER_MODE` boolean to indicate
* `sensor.log` is the file that readings are logged to

## Development
When plugged into your computer only the USB exported filesystem is read-write. The
version running on the board is remounted as read-only by `boot.py`. You can use the 
`DEVELOPER_MODE` flag to change the behavior of your script
based on whether you have read-write access on the board or not.

## Issues
I don't have a way to keep track of time without power so it always resets to unix epoch time each
time it loses power. I will probably add an RTC with a battery backup in the future to
keep the times consistent. Currently you'll need to make note of the time it last booted when 
analyzing the sensor.log.