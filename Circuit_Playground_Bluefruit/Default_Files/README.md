# PyCon 2023 Circuit Playground Bluefruit Demo Files

**These are the default demo files included on the Circuit Playground Bluefruits provided for the 
2023 Education Summit _Welcome to CircuitPython_ workshop, and the PyCon 2023 conference
CircuitPython Open Spaces.**

If you wish to return the board to its default state, simply copy the following file and folders
(including all of their contents) to your CIRCUITPY drive, overwriting the existing files. **This
will erase any changes you've made so if you wish to keep your changes, please back up your
existing code.py file first!**
* code.py
* audio/
* lib/

### The Circuit Playground Bluefruit Demo Details
The demo plays a random one of three wav files on startup, and begins with the NeoPixel LED
rainbow comet demo.

#### Features:
* The slide-switch enables or disables audio playback in the touchpad demo. If the switch is to the
  right, audio playback is enabled. If the switch is to the left, audio playback is disabled.
* Pressing Button B turns on the little red LED.
* Pressing button A or B cycles between four different modes:
    * Mode 0: NeoPixel LED rainbow comet.
    * Mode 1: Touchpad, NeoPixel LED, and audio (based on the slide-switch) demo. The slide-switch
      should be to the right to enable audio playback on the touchpads. Touch each of the seven
      touchpads to light up the NeoPixels a different color, and if audio playback is enabled,
      play a different sound.
    * Mode 2: NeoPixel light meter demo. Shine a light (such as from your mobile) on the CPB to see
      the number of LEDs lit up increase as the light gets brighter.
    * Mode 3: NeoPixel LED and acceleration demo. Lights up the NeoPixel LEDs based on the
      acceleration values from the accelerometer. Rotate the board across the x, y and z axes to
      see the colors change. Shake the board vigorously to see the brightness increase.

#### Notes:
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

### Thank you!
Thank you to [John Park](https://jpixl.net/) for the amazing audio files used in
this demo!