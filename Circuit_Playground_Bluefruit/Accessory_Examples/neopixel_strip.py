"""
This example requires a NeoPixel strip. Talk to the team to get one!

Connect the white clip on the NeoPixel strip to pad TX.
Connect the black clip on the NeoPixel strip to a GND pad.
Connect the red clip on the NeoPixel strip to the VOUT pad.
"""
import time
import board
import neopixel

strip = neopixel.NeoPixel(board.TX, 30)
strip.brightness = 0.3

while True:
    strip.fill((255, 0, 0))
    time.sleep(0.5)
    strip.fill((0, 255, 0))
    time.sleep(0.5)
    strip.fill((0, 0, 255))
    time.sleep(0.5)
