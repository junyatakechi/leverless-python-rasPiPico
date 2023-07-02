import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import board
import digitalio

k = Keyboard(usb_hid.devices)

button_w = digitalio.DigitalInOut(board.GP0)
button_w.direction = digitalio.Direction.INPUT
button_w.pull = digitalio.Pull.UP

button_a = digitalio.DigitalInOut(board.GP1)
button_a.direction = digitalio.Direction.INPUT
button_a.pull = digitalio.Pull.UP

button_s = digitalio.DigitalInOut(board.GP2)
button_s.direction = digitalio.Direction.INPUT
button_s.pull = digitalio.Pull.UP

button_d = digitalio.DigitalInOut(board.GP3)
button_d.direction = digitalio.Direction.INPUT
button_d.pull = digitalio.Pull.UP

repeat_delay = 1 / 60  # 60fpsに基づく1フレームの時間

while True:
    if not button_w.value:
        k.send(Keycode.W)
        time.sleep(repeat_delay)
    if not button_a.value:
        k.send(Keycode.A)
        time.sleep(repeat_delay)
    if not button_s.value:
        k.send(Keycode.S)
        time.sleep(repeat_delay)
    if not button_d.value:
        k.send(Keycode.D)
        time.sleep(repeat_delay)