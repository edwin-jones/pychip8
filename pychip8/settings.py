"""
This module contains settings and configuration data for the application.
You can change values here to play different roms or to help you debug the application.
"""
from pychip8.cpu import Cpu

# The fps is also the default internal cycle speed of the emulator.
# The CHIP-8 timers expect to be run at this speed
# so be careful if you change this
FRAMES_PER_SECOND = 60

# The CHIP-8 is reported to run best at arround 500hz
OPERATIONS_PER_SECOND = 500

# This will evaluate to 480 by default - not quite 500hz but close enough
OPERATIONS_PER_FRAME = int(OPERATIONS_PER_SECOND / FRAMES_PER_SECOND)

# This is the string used for the window title
APP_NAME = "Pychip8"

# The CHIP-8 display ran at only 64 * 32 pixels.
# this value scales the framebuffer
# so it's easier to view the emulator on modern displays
SCREEN_SCALE = 10

# You can use this value to run the program to a specific point straight away
# rather than waiting normally. Useful for debugging
RUNTO = Cpu.PROGRAM_START_ADDRESS

# Change this to load up a different rom in the roms folder
ROM_NAME = "draw_chars.ch8"
