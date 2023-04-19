"""This example turns on the little red LED and prints to the serial console when a shake is
detected."""
import time
from adafruit_circuitplayground import cp

while True:
    # Lower shake_threshold means shake detection will trigger more easily!
    if cp.shake(shake_threshold=20):
        print("Shake detected!")
        cp.red_led = True
        time.sleep(0.1)
    else:
        cp.red_led = False
