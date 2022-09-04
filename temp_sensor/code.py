import time
import board
import digitalio

import adafruit_ahtx0

# Seconds between sensor readings
INTERVAL = 300

switch = digitalio.DigitalInOut(board.D2)
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.UP

DEVELOPER_MODE = not switch.value

print(f"Developer mode is {DEVELOPER_MODE}")


def log_readings(_temp, _humidity):
    f = open("sensor.log", "a", encoding="utf-8")
    f.write(f"{time.time()} {_temp} {_humidity}\n")
    f.close()


# Create sensor object, communicating over the board's default I2C bus
i2c = board.I2C()  # uses board.SCL and board.SDA
sensor = adafruit_ahtx0.AHTx0(i2c)

while True:
    temp = (sensor.temperature * 1.8 + 32)
    humidity = sensor.relative_humidity
    if DEVELOPER_MODE:
        print("\nTemperature: %0.1f°F" % temp)
        print("Humidity: %0.1f%%" % humidity)
    else:
        log_readings(temp, humidity)

    time.sleep(INTERVAL)
