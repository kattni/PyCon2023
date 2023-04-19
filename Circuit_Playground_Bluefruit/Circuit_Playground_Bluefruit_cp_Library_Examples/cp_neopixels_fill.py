"""This example turns on, or "fills", all the NeoPixels red!"""
from adafruit_circuitplayground import cp

while True:
    cp.pixels.fill((50, 0, 0))
