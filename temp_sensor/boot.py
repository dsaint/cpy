import board
import digitalio
import storage

switch = digitalio.DigitalInOut(board.D2)
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.UP

print(f"Developer mode {not switch.value}")

# True  = No GND/D2 jumper in place
# False = GND/D2 jumper in place

# On boot don't remount as read-only at the end so that we can
# do logging locally. When developing the GND/D2 jumper needs to be
# in place so that
storage.remount("/", not switch.value)