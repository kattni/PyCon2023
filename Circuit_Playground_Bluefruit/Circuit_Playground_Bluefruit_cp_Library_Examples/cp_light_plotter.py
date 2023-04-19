"""If you're using Mu, this example will plot the light levels from the light sensor (located next
to the eye) on your cp. Try shining a flashlight on your CPB, or covering the light sensor to see
the plot increase and decrease."""
import time
from adafruit_circuitplayground import cp

while True:
    print("Light:", cp.light)
    print((cp.light,))
    time.sleep(0.1)
