import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import board
import digitalio

k = Keyboard(usb_hid.devices)

button_pins = {
    Keycode.W: board.GP0,
    Keycode.A: board.GP1,
    Keycode.S: board.GP2,
    Keycode.D: board.GP3,
    Keycode.U: board.GP4,
    Keycode.I: board.GP5,
    Keycode.O: board.GP6,
    Keycode.J: board.GP7,
    Keycode.K: board.GP8,
    Keycode.L: board.GP9,
    Keycode.Q: board.GP10,
    Keycode.E: board.GP11,
    Keycode.F: board.GP12,
    Keycode.SPACE: board.GP13,
    Keycode.ENTER: board.GP14,
    27: board.GP15, # Esc
}

buttons = {}
for keycode, pin in button_pins.items():
    button = digitalio.DigitalInOut(pin)
    button.direction = digitalio.Direction.INPUT
    button.pull = digitalio.Pull.UP
    buttons[keycode] = {
        'button': button,
        'state': False,
    }

while True:
    for keycode, button_data in buttons.items():
        button = button_data['button']
        if not button.value and not button_data['state']:
            k.press(keycode)
            button_data['state'] = True
        elif button.value and button_data['state']:
            k.release(keycode)
            button_data['state'] = False
