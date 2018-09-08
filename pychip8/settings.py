"""This module contains settings and configuration data for the application"""

import argparse

from pychip8.cpu import Cpu

class Settings:

    FRAMES_PER_SECOND = 60
    OPERATIONS_PER_SECOND = 500
    OPERATIONS_PER_FRAME = int(OPERATIONS_PER_SECOND / FRAMES_PER_SECOND)
    APP_NAME = "Pychip8"
    SCREEN_SCALE = 10

    @classmethod
    def parse_arguments(cls):
        "this function parses command line args into the settings module"
        parser = argparse.ArgumentParser()
        parser.add_argument(
            '--runto',
            dest='runto',
            default=str(Cpu.PROGRAM_START_ADDRESS),
            help='this is a address for the program counter to run to in hex before startup')

        parser.add_argument(
            '--rom',
            dest='rom',
            default="draw_chars.ch8",
            help='this is the name of the rom to run in the roms folder')

        args = parser.parse_args()

        cls.RUNTO = args.runto
        cls.ROM_NAME = args.rom
