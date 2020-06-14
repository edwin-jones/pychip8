"""
This module contains settings and configuration data for the application.
You can change values here to play different roms or to help you debug the application.
"""
from pychip8.cpu import Cpu

# The fps is also the internal cycle speed of the emulator.
FRAMES_PER_SECOND = 30

# The CHIP-8 is reported to run best at arround 500 hz
# 480 is close enough, and easier to divide.
OPERATIONS_PER_SECOND = 480

# The CHIP-8 timers expect to be run at
# 60 fps, we should keep to this as much as possible
TIMER_UPDATES_PER_SECOND = int(60 / FRAMES_PER_SECOND)

OPERATIONS_PER_FRAME = int(OPERATIONS_PER_SECOND / FRAMES_PER_SECOND)

# This is the string used for the window title
APP_NAME = "Pychip8"

# The CHIP-8 display ran at only 64 * 32 pixels.
# this value scales the framebuffer
# so it's easier to view the emulator on modern displays
SCREEN_SCALE = 10

# You can use this value to run the program to a specific point straight away
# rather than waiting normally. Useful for debugging.
RUNTO = Cpu.PROGRAM_START_ADDRESS

# the default rom the emulator will load
DEFAULT_ROM_NAME = "draw chars.ch8"
