"""This is the main entry point for the program"""

import argparse

import pygame
import pychip8.settings as settings

from pychip8.rom_loader import RomLoader
from pychip8.operation_mapper import OperationMapper
from pychip8.cpu import Cpu
from pychip8.app import App
from pychip8.renderer import Renderer
from pychip8.keyboard_input_handler import KeyboardInputHandler
from pychip8.beeper import Beeper

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--mute", action='store_true', help="pass this flag to turn audio off")
    parser.add_argument("-r", "--rom", type=str, help="the name of the rom to run in the emulator")
    parser.add_argument("-s", "--scale", type=int, help="the scale to apply to the CHIP-8's 64x32 video output defaults to 10 for 640x320 pixels")
    args = parser.parse_args()

    rom_loader = RomLoader(args.rom if args.rom else settings.DEFAULT_ROM_NAME)
    operation_mapper = OperationMapper()
    cpu = Cpu(operation_mapper)
    input_handler = KeyboardInputHandler()
    beeper = Beeper(args.mute)
    clock = pygame.time.Clock()

    scale = args.scale if args.scale else settings.SCREEN_SCALE
    scale = max(min(scale, 100), 1)

    pygame.font.init()
    font = pygame.font.SysFont("Arial", int(scale * 2))

    renderer = Renderer(font, scale)

    app = App(cpu, rom_loader, renderer, input_handler, beeper, clock)

    app.run()
