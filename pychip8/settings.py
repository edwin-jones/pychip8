"""
This module contains settings and configuration data for the application.
You can change values here to play different roms or to help you debug the application.
"""
from pychip8.cpu import Cpu

FRAMES_PER_SECOND = 60
OPERATIONS_PER_SECOND = 500
OPERATIONS_PER_FRAME = int(OPERATIONS_PER_SECOND / FRAMES_PER_SECOND)
APP_NAME = "Pychip8"
SCREEN_SCALE = 10
RUNTO = Cpu.PROGRAM_START_ADDRESS
ROM_NAME = "draw_chars.ch8"
