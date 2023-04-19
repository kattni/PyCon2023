# Copyright 2023 Kattni Rembor
# License: MIT
"""
PyCon 2023 Circuit Playground Bluefruit Demo

This demo plays a random one of three wav files on startup, and begins with the NeoPixel LED
rainbow comet demo.

Features:
* The slide-switch enables or disables audio playback in the touchpad demo. If the switch is to the
  right, audio playback is enabled. If the switch is to the left, audio playback is disabled.
* Pressing Button B turns on the little red LED.
* Pressing button A or B cycles between four different modes:
  Mode 0: NeoPixel LED rainbow comet.
  Mode 1: Touchpad, NeoPixel LED, and audio (based on the slide-switch) demo. The slide-switch
          should be to the right to enable audio playback on the touchpads. Touch each of the seven
          touchpads to light up the NeoPixels a different color, and if audio playback is enabled,
          play a different sound.
  Mode 2: NeoPixel light meter demo. Shine a light (such as from your mobile) on the CPB to see the
          number of LEDs lit up increase as the light gets brighter.
  Mode 3: NeoPixel LED and acceleration demo. Lights up the NeoPixel LEDs based on the acceleration
          values from the accelerometer. Rotate the board across the x, y and z axes to see the
          colors change. Shake the board vigorously to see the brightness increase.

Notes:
* The Circuit Playground Bluefruit is upright when the USB cable is towards the top! If you hold
  the board by the USB cable, it will be upside down, meaning buttons A and B and the slide-switch
  position will be swapped. Button B will be on the left, and button A will be on the right. The
  slide-switch will enable audio playback when to the left, and disable it when to the right. To
  avoid this, please hold the board with the USB pointing upwards. The documentation above and in
  the code assumes the board is upright.
* This demo was written with beginners in mind. There is a far more concise way to do much of what
  is done in this example. It is kept long-form in the interest of readability and ease of use.
* `auto_write` is a keyword argument associated with `pixels`. When enabled, you can simply write
  NeoPixel LED code, and the LEDs will update immediately. If `auto_write` is disabled, it means
  you must explicitly call `pixels.show()` after your LED code to get the LEDs to update.
"""
import time
import random
import board
import keypad
from adafruit_led_animation.color import RED, ORANGE, YELLOW, GREEN, CYAN, BLUE, PURPLE
from adafruit_led_animation.animation.rainbowcomet import RainbowComet
from adafruit_circuitplayground import cp

cp.pixels.brightness = 0.3  # Set the pixel brightness to 30%.

# Set up the buttons using the keypad module.
buttons = keypad.Keys((board.BUTTON_A, board.BUTTON_B), value_when_pressed=True, pull=True)

# Play a random wav file from the list on startup.
startup_sound = ("audio/ring.wav", "audio/space.wav", "audio/think.wav")
cp.play_file(startup_sound[random.randrange(3)])

# Set up the mode 0 rainbow comet.
rainbow_comet = RainbowComet(cp.pixels, speed=0.1, tail_length=10, ring=True)


def scale_range(value):
    """Scale a value from 0-320 (light range) to 0-9 (NeoPixel range, 10 total LEDs).
    Allows remapping light value to pixel position for light meter demo."""
    return round(value / 320 * 10)


# Set up colors and wav file for the touchpad demo.
touch_colors = (RED, ORANGE, YELLOW, GREEN, CYAN, BLUE, PURPLE)
touch_wav_files = ("audio/1.wav", "audio/2.wav", "audio/3.wav", "audio/4.wav",
                   "audio/5.wav", "audio/6.wav", "audio/7.wav")

MODE = 0
while True:
    # Press button A to cycle between four different modes (0-3).
    # Press button B to turn on the little red LED.
    button_event = buttons.events.get()  # Set up to get the button press and release events.
    if button_event:  # If there is a button event, continue onto the following code.
        # print(button_event)  # Uncomment this to print the button event.
        if button_event.pressed:  # When button A or B is pressed...
            MODE += 1  # ...increase the mode by 1.
            if MODE > 3:  # If the mode is greater than 3...
                MODE = 0  # ...set the mode back to 0.
            # print(mode)  # Uncomment this to print the mode number to the serial console.
        if button_event.pressed and button_event.key_number == 1:  # When button B is pressed...
            cp.red_led = True  # ...turn on the little red LED.
        else:  # Otherwise...
            cp.red_led = False  # ...turn off the little red LED.

    # The slide-switch controls whether wav audio playback in the touchpad mode is enabled.
    # The switch returns False when to the right, and True when to the left.
    # If the switch is to the right, enable wav playback in the touchpad demo.
    WAV_PLAYBACK = not cp.switch

    if MODE == 0:
        # Rainbow comet demo.
        rainbow_comet.animate()

    elif MODE == 1:
        # Touchpad demo.
        cp.pixels.auto_write = True  # Enable auto_write for the touchpad demo.
        # Read the state of the available touchpads.
        touch_pads = (cp.touch_A1, cp.touch_A2, cp.touch_A3, cp.touch_A4,
                      cp.touch_A5, cp.touch_A6, cp.touch_TX)
        for pad_index in range(7):  # There are seven options for each part of the demo.
            if touch_pads[pad_index]:  # If a pad is touched...
                cp.pixels.fill(touch_colors[pad_index])  # ...fill the LEDs with the proper color.
                if WAV_PLAYBACK:  # If audio playback is enabled...
                    cp.play_file(touch_wav_files[pad_index])  # ...play the proper wav file.
        if not any(touch_pads):  # If no pads are touched...
            cp.pixels.fill((0, 0, 0))  # ...turn off the LEDs.

    elif MODE == 2:
        # NeoPixel LED Light Meter demo.
        cp.pixels.auto_write = False  # Disable auto_write for the light meter demo.
        cp.pixels.fill((0, 0, 0))  # Turn off all the pixels.
        peak = scale_range(cp.light)  # Use scale_range to map the light values to LED numbers.
        for pixel in range(peak):  # Loop over integers from 0 to `peak`.
            cp.pixels[pixel] = (0, 255, 255)  # This sets pixel 0 through `peak` to cyan.
        cp.pixels.show()  # Called because auto_write is disabled.
        time.sleep(0.05)

    elif MODE == 3:
        # NeoPixel LED Acceleration demo.
        cp.pixels.auto_write = True  # Enable auto_write for the acceleration demo.
        acceleration = cp.acceleration  # To avoid reading the sensor data twice.
        # Red, green, blue values generated from the x, y, z acceleration values multiplied by 10.
        r, g, b = [abs(int(value * 10)) for value in acceleration]
        print(acceleration)  # Print the raw acceleration values.
        cp.pixels.fill((r, g, b))  # Light up the NeoPixels based on the acceleration values.
