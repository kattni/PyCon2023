"""This example plays a tone while you're pressing a button! It is a different tone for each button
pressed, and it plays for the duration of the button press."""
from adafruit_circuitplayground import cp

while True:
    if cp.button_a:
        cp.start_tone(262)
    elif cp.button_b:
        cp.start_tone(294)
    else:
        cp.stop_tone()
