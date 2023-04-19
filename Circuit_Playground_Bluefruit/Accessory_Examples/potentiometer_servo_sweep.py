"""This example requires a potentiometer and a servo. Talk to the team to get one of each!

Connect the blue clip on the potentiometer to pad A2.
Connect the red clip on the potentiometer to a 3.3v pad.
Connect the black clip on the potentiometer to a GND pad.

Connect the blue clip (on the yellow wire) on the servo to pad A1.
Connect the black clip (on the brown wire) on the servo to a GND pad.
Connect the red clip (on the red wire) on the servo to a 3.3v pad.

THIS EXAMPLE REQUIRES A SEPARATE LIBRARY BE LOADED ONTO YOUR CIRCUITPY DRIVE.
This example requires the adafruit_motor library.

Rotate the potentiometer knob to watch the servo rotate!"""
import board
import analogio
import pwmio
from adafruit_motor import servo

potentiometer = analogio.AnalogIn(board.A2)
pwm = pwmio.PWMOut(board.A1, duty_cycle=2 ** 15, frequency=50)
servo = servo.Servo(pwm)


def get_voltage(pin):
    return (pin.value * 3.3) / 65536


def scale_range(value):
    """Scale a value from 0-320 (light range) to 0-9 (NeoPixel range, 10 total LEDs).
    Allows remapping light value to pixel position for light meter demo."""
    return round(value / 3.3 * 180)


while True:
    # Potentiometer voltage value remapped to servo angle
    servo_sweep = scale_range(get_voltage(potentiometer))
    servo.angle = servo_sweep
