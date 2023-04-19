"""
This example uses the light sensor on the CPB, located net to the picture of the eye on the board.
Once you have the library loaded, try shining a flashlight on your CP to watch the number of
NeoPixels lit up increase, or try covering up the light sensor to watch the number decrease.
"""
import time
from adafruit_circuitplayground import cp

cp.pixels.auto_write = False
cp.pixels.brightness = 0.3


def scale_range(value):
    """Scale a value from 0-320 (light range) to 0-9 (NeoPixel range, 10 total LEDs).
    Allows remapping light value to pixel position for light meter demo."""
    return round(value / 320 * 10)


while True:
    # light value remapped to pixel position
    peak = scale_range(cp.light)
    print(cp.light)
    print(int(peak))

    for i in range(0, 10, 1):
        if i <= peak:
            cp.pixels[i] = (0, 255, 255)
        else:
            cp.pixels[i] = (0, 0, 0)
    cp.pixels.show()
    time.sleep(0.05)
