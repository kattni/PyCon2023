# PyCon 2023
![Code + Community = CircuitPython!](/.assets/Blinka_Code_Community.png "Code + Community = CircuitPython")

This repo contains the CircuitPython Quickstart worksheets and example code for the PyCon 2023
CircuitPython Open Spaces! It also contains various additional content including slides for
Kattni's Education Summit talk.

We'll be providing Circuit Playground Express boards for use during the CircuitPython Open
Spaces. Getting started with it requires a micro USB to USB type A or C cable. We will have a
number for use during the CircuitPython Open Spaces. Feel free to bring your own as well! Beware
of charge-only cables, they will not work for programming a Circuit Playground Express!

We will be hosting Open Spaces every day at PyCon, April 21 - 23, 2023. We'll have this
Quickstart available as a worksheet, including some examples on the back to get you started. This
repo will have those examples and more available for you to try, play with, and modify. We'll also
have some extras (servos, potentiometers and external NeoPixel strips) available for you to
connect to the Circuit Playground Express.

**The Adafruit Circuit Playground Express (CPX) has CircuitPython on board!** It’s a Microchip SAMD21 microcontroller running at 48 MHz, with 256kb flash, plus a 2MB external flash chip for the CIRCUITPY USB drive. It’s loaded with sensors, LEDs, touch pads, buttons and more!

#### Check out these Adafruit Learn Guide Links!
* Welcome to CircuitPython: http://adafru.it/cpy-welcome
* CPB Guide: https://adafru.it/adafruit-cpx
* CP Made Easy on CPB: https://adafru.it/cp-made-easy

#### Download the latest CircuitPython for Circuit Playground Express!
* CircuitPython for CPX: https://circuitpython.org/board/circuitplayground_express/

#### Plug It In!
Use a micro-USB cable with data (beware charge/power-only cables). A USB drive called **CIRCUITPY**
will appear. If there’s a **code.py** on **CIRCUITPY**, it will run automatically.

#### Auto-Reload
Every time you write a file, **code.py** will be re-run, unless you are in the REPL. Just edit
**code.py** and see it run right away. This makes for a fast workflow.

#### Editing Code (Recommended Editors)
If you already have a favorite code editor, you can use it. Be sure you’re using one that writes
back immediately: VS Code, Atom (install the fsync-on-save package), Sublime, gedit, vim with `-n`
option, emacs, PyCharm with Safe Write. **_Don’t_ use** Notepad, nano, IDLE. See [Welcome->Advanced
Setup->Recommended Editors](https://learn.adafruit.com/welcome-to-circuitpython/recommended-editors)
for more details.

#### Another Editor Option
Mu is the easiest editor to use: it includes a Python editor and easy serial REPL access. See [Welcome
->Installing Mu Editor](https://learn.adafruit.com/welcome-to-circuitpython/installing-mu-editor).
The latest version for Windows and Mac are available at https://codewith.mu. For Linux, or any OS,
you can create a `venv` and use `pip3` to install Mu: `pip3 install --user mu-editor`

#### Avoiding Filesystem Corruption
Windows and Linux don’t write back data to **CIRCUITPY** immediately: they can delay for 10s of
seconds. (Not an issue on MacOS.) **Eject or sync after you copy files, and always before you
unplug or press the Reset button.** Otherwise **CIRCUITPY** may become corrupted. See **_Editing
Code (Recommended Editors)_** above, so you don’t need to Eject or sync every time you edit.
If **CIRCUITPY** does get corrupted, see **_Restoring or Installing CircuitPython_** in this
Quickstart.

#### Libraries
CircuitPython has built in native modules, but also has libraries written in Python (which are
compiled into **.mpy** files to save space). The board has a **lib** folder containing all the
necessary libraries for the provided examples. If you want to try more complex examples or use
external accessories, you may need to download more libraries. If you try to run a program
that requires a library not present on your board, the program will not complete - but you can
check the serial console (see below) for more information. For details on getting libraries loaded
on your CPB, see
[Welcome->CircuitPython
Libraries](https://learn.adafruit.com/welcome-to-circuitpython/circuitpython-libraries).

#### Restoring or Installing CircuitPython
[CircuitPython.org](https://adafru.it/cp-cpx) has the current version of the CircuitPython UF2 for
the Circuit Playground Express. **WARNING: In rare cases, this process can result in the loss of
any files on the board - backup your files if possible first!** To restore or update your board,
double-tap the reset button found in the center of the board. The LEDs will flash red and then turn
green, and you’ll see a **CPLAYBOOT** drive show up on your computer. Copy the .uf2 file to
**CPLAYBOOT**. It will disconnect and the drive will disappear. A few seconds later, **CIRCUITPY**
will reappear. If this does not resolve your issue, check out [Welcome->Troubleshooting->To erase
CIRCUITPY](https://learn.adafruit.com/welcome-to-circuitpython/troubleshooting#to-erase-circuitpy-storage-dot-erase-filesystem-2987288-34)
for instructions to fully erase the filesystem. **The steps found here WILL erase everything on the
board.**

#### Connecting to the Serial Console
When your code produces an error, or you add a `print` statement to your code, the results are
printed to the serial console. If you're looking for your `print`ed data, or you're not getting the
results you expect, try connecting to the serial console. It's great for debugging code!

The serial console and REPL are built into Mu - simply click the icon labeled “Serial”.

If not using Mu, you have a number of options.

On Windows, try **Putty** or **Tera Term**. See [Welcome->Advanced Setup->Advanced
Serial Console On
Windows](https://learn.adafruit.com/welcome-to-circuitpython/advanced-serial-console-on-windows)
for more details.

On Mac and Linux, try **`screen`**, **`tio`**, or **picocom**, or any other
terminal emulator you may already be using. Use tab completion for the paths on Mac
`/dev/tty.usbmodem*` or Linux `/dev/ttyACM*` while entering `screen` commands. See
[Welcome->Advanced Setup->Advanced Serial Console on Mac](https://learn.adafruit.com/welcome-to-circuitpython/advanced-serial-console-on-mac-and-linux) and
[Welcome->Advanced Setup->Advanced Serial Console on Linux](https://learn.adafruit.com/welcome-to-circuitpython/advanced-serial-console-on-linux)
for more details.

* To connect using `screen` on Mac:
    * `screen /dev/tty.usbmodem* 115200`
* To connect using `screen` on Linux:
    * `screen /dev/ttyACM0 115200`

#### Interact with the REPL!
Once connected to the serial console, type Enter if necessary to start the REPL. If **code.py** is
running, type ctrl-C, then press enter. Type ctrl-D to soft-restart and reload the serial console.
The REPL works like a standard Python prompt. Try the following:
```
>>> 1+2
3
```

#### Beyond the Circuit Playground Express
There are currently [72 CircuitPython-compatible Adafruit boards](https://adafru.it/cp-boards).
There are also a multitude of sensor breakouts, accessories, and more with CircuitPython support.
If you’re interested in continuing your exploration, check out the Adafruit shop at
[adafruit.com](https://adafruit.com). Use code PYCON2023 to get 10% off!