"""This example requires a potentiometer. Talk to the team to get one!

Connect the blue clip on the potentiometer to pad A2.
Connect the black clip to a GND pad.
Connect the red clip to a 3.3v pad.

Rotate the potentiometer knob to see the number of NeoPixels lit up on your CP change!"""
import time
import board
import analogio
from adafruit_circuitplayground import cp

cp.pixels.auto_write = False
cp.pixels.brightness = 0.3
potentiometer = analogio.AnalogIn(board.A2)


def get_voltage(pin):
    return (pin.value * 3.3) / 65536


def scale_range(value):
    """Scale a value from 0-320 (light range) to 0-9 (NeoPixel range, 10 total LEDs).
    Allows remapping light value to pixel position for light meter demo."""
    return round(value / 3.3 * 10)


while True:
    # Potentiometer voltage value remapped to pixel position
    cp_peak = scale_range(get_voltage(potentiometer))

    for i in range(0, 10, 1):
        if i <= cp_peak:
            cp.pixels[i] = (0, 255, 255)
        else:
            cp.pixels[i] = (0, 0, 0)
    cp.pixels.show()
    time.sleep(0.05)
