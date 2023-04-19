"""This example uses the capacitive touchpads on the CPB. They are located around the outer edge
of the board and are labeled A1-A6 and TX. (Audio is not a touchpad.) This example prints
"Touched (pad)" to the serial console. Touch the touchpads to see the prints!"""
import time
from adafruit_circuitplayground import cp

while True:
    if cp.touch_A1:
        print("Touched A1!")
    if cp.touch_A2:
        print("Touched A2!")
    if cp.touch_A3:
        print("Touched A3!")
    if cp.touch_A4:
        print("Touched A4!")
    if cp.touch_A5:
        print("Touched A5!")
    if cp.touch_A6:
        print("Touched A6!")
    if cp.touch_TX:
        print("Touched TX!")
    time.sleep(0.1)
