"""THIS EXAMPLE REQUIRES A WAV FILE FROM THE ADDITIONAL_CONTENT FOLDER IN THE PyCon2023 REPO!
Copy the "space.wav" file into a folder named "audio" on your CIRCUITPY drive.

Once the file is copied, this example plays a wav file!"""
from adafruit_circuitplayground import cp

cp.play_file("audio/space.wav")
