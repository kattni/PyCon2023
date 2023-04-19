"""THIS EXAMPLE REQUIRES A WAV FILE FROM THE ADDITIONAL_CONTENT FOLDER IN THE PyCon2023 REPO!
Copy the "space.wav" file into a folder named "audio" on your CIRCUITPY drive.

Once the file is copied, this example plays a wav file using the speaker on the CP, the grey
square located next to the picture of musical notes on the board."""
import board
from audiocore import WaveFile
from audiopwmio import PWMAudioOut as AudioOut
import digitalio

speaker_enable = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
speaker_enable.switch_to_output(value=True)

data = open("audio/space.wav", "rb")
wav = WaveFile(data)
a = AudioOut(board.SPEAKER)

print("Playing file.")
a.play(wav)
while a.playing:
    pass
print("Playing file stopped.")
