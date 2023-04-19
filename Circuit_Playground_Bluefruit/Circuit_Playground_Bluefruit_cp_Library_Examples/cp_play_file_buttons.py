"""THIS EXAMPLE REQUIRES A WAV FILE FROM THE ADDITIONAL_CONTENT FOLDER IN THE PyCon2023 REPO!
Copy the "ring.wav" and "think.wav" files into a folder named "audio" on your CIRCUITPY drive.

Once the files are copied, this example plays a different wav file for each button pressed!"""
from adafruit_circuitplayground import cp

while True:
    if cp.button_a:
        cp.play_file("audio/ring.wav")
    if cp.button_b:
        cp.play_file("audio/think.wav")
