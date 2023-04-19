"""This example uses the light sensor on your CPB, located next to the picture of the eye. Try
shining a flashlight on your CPB, or covering the light sensor with your finger to see the values
increase and decrease."""
import time
import board
import analogio

light_sensor = analogio.AnalogIn(board.LIGHT)

while True:
    print(light_sensor.value)
    time.sleep(0.1)
