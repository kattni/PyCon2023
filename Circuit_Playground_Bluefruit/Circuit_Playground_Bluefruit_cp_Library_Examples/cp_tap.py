"""This example prints to the serial console when you double-tap the CP!"""
from adafruit_circuitplayground import cp

# Set this to 1 to detect a single-tap!
cp.detect_taps = 2

while True:
    if cp.tapped:
        print("Tapped!")
