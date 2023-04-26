# SPDX-FileCopyrightText: 2023 Kattni Rembor for Adafruit Industries
# SPDX-License-Identifier: MIT
"""
CircuitPython Essentials Storage CP Filesystem code.py file
"""
import time
import board
import digitalio
import microcontroller
import busio
import adafruit_lis3dh

i2c = busio.I2C(board.ACCELEROMETER_SCL, board.ACCELEROMETER_SDA)
int1 = digitalio.DigitalInOut(board.ACCELEROMETER_INTERRUPT)
lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c, address=0x19, int1=int1)

led = digitalio.DigitalInOut(board.LED)
led.switch_to_output()

# Setup sampling period and duration
sampling_period = 0.1
sampling_time = 10
num_samples = int(sampling_time / sampling_period)

try:
    with open("/acceleration.txt", "w") as log:
        time.sleep(5)
        log.write("t, x, y, z\n")
        log.flush()

        t0 = time.monotonic()  # Used so t=0 is when the device booted
        while True:
            # Log acceleration data for the given duration
            data = [None]*num_samples
            for i in range(num_samples):
                t1 = time.monotonic()
                x, y, z = lis3dh.acceleration

                # Add the time and acceleration to the log
                data[i] = t1 - t0, x, y, z
                t2 = time.monotonic()

                # Sleep however long there is left of the sampling period
                time.sleep(max(0, sampling_period - (t2 - t1)))

            # Write the acceleration data to the device
            for (t, x, y, z) in data:
                log.write('{t:.3f}, {x:.3f}, {y:.3f}, {z:.3f}\n'.format(t=t, x=x, y=y, z=z))

            # Add a blank line to separate each contiguous log
            log.write('\n')
            log.flush()

            # Blink the LED on every write...
            led.value = True

            # Add a slight delay between each write
            time.sleep(1)

            led.value = False

except OSError as e:  # When the filesystem is NOT writable by CircuitPython...
    delay = 0.5  # ...blink the LED every half second.
    if e.args[0] == 28:  # If the file system is full...
        delay = 0.15  # ...blink the LED every 0.15 seconds!
    while True:
        led.value = not led.value
        time.sleep(delay)
