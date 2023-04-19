"""This example requires a potentiometer and a NeoPixel strip. Talk to the team to get one of each!

Connect the blue clip on the potentiometer to pad A2.
Connect the black clip to a GND pad.
Connect the red clip to a 3.3v pad.

Connect the white clip on the NeoPixel strip to pad TX.
Connect the black clip on the NeoPixel strip to a GND pad.
Connect the red clip on the NeoPixel strip to the VOUT pad.

Rotate the potentiometer knob to watch the number of pixels lit up on the strip change!"""
import time
import board
import analogio
import neopixel

strip = neopixel.NeoPixel(board.TX, 30, auto_write=False)
strip.brightness = 0.3
potentiometer = analogio.AnalogIn(board.A2)


def get_voltage(pin):
    return (pin.value * 3.3) / 65536


def scale_range(value):
    """Scale a value from 0-320 (light range) to 0-9 (NeoPixel range, 10 total LEDs).
    Allows remapping light value to pixel position for light meter demo."""
    return round(value / 3.3 * 30)


while True:
    # Potentiometer voltage value remapped to pixel position
    strip_peak = scale_range(get_voltage(potentiometer))

    for j in range(0, 30, 1):
        if j <= strip_peak:
            strip[j] = (0, 255, 255)
        else:
            strip[j] = (0, 0, 0)

    strip.show()
    time.sleep(0.05)
