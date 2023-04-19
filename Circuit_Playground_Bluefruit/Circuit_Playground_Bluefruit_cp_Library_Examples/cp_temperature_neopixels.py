"""
This example use the temperature sensor on the CPB, located next to the picture of the thermometer
on the board. Try warming up the board to watch the number of NeoPixels lit up increase, or cooling
it down to see the number decrease. You can set the min and max temperatures to make it more or
less sensitive to temperature changes.
"""
import time
from adafruit_circuitplayground import cp

cp.pixels.auto_write = False
cp.pixels.brightness = 0.3

# Set these based on your ambient temperature in Celsius for best results!
minimum_temp = 24
maximum_temp = 30


def scale_range(value):
    """Scale a value from 0-320 (light range) to 0-9 (NeoPixel range, 10 total LEDs).
    Allows remapping light value to pixel position for light meter demo."""
    return round(value / (maximum_temp - minimum_temp) * 10)


while True:
    # temperature value remapped to pixel position
    peak = scale_range(cp.temperature)
    print(cp.temperature)
    print(int(peak))

    for i in range(0, 10, 1):
        if i <= peak:
            cp.pixels[i] = (0, 255, 255)
        else:
            cp.pixels[i] = (0, 0, 0)
    cp.pixels.show()
    time.sleep(0.05)
