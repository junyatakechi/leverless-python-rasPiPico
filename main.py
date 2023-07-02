import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import board
import digitalio

k = Keyboard(usb_hid.devices)

led = digitalio.DigitalInOut(board.GP15)
led.direction = digitalio.Direction.OUTPUT

button = digitalio.DigitalInOut(board.GP13)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

while True:
    if not button.value:
        led.value = True
        k.send(Keycode.F)
        time.sleep(0.1)
    else:
        led.value = False
        time.sleep(0.1)
