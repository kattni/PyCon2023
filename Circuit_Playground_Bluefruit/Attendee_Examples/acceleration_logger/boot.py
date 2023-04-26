# SPDX-FileCopyrightText: 2023 Kattni Rembor for Adafruit Industries
# SPDX-License-Identifier: MIT
"""
CircuitPython Essentials Storage CP Filesystem boot.py file

The Bluefruit is set up so either the computer can write to it, or the
device itself can write to it. Since we want to log data, we need a way
to switch between the two.

The following code makes it so that the Bluefruit can write to itself
if button A is held down while it is booting.
"""
import board
import digitalio
import storage

button_a = digitalio.DigitalInOut(board.BUTTON_A)
button_a.direction = digitalio.Direction.INPUT
button_a.pull = digitalio.Pull.DOWN

# If the OBJECT_NAME is connected to ground, the filesystem is writable by CircuitPython
storage.remount("/", readonly=not button_a.value)# Write your code here :-)
