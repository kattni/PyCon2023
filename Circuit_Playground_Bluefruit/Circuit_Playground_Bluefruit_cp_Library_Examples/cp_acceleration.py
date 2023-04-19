"""This example uses the accelerometer in the center of the CPB. Try moving the board around to see
the values change!"""
import time
from adafruit_circuitplayground import cp

while True:
    x, y, z = cp.acceleration
    print((x, y, z))
    time.sleep(0.5)
