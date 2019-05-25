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
    parser.add_argument("-r", "--rom", type=str, help=" the name of the rom to run in the emulator")
    args = parser.parse_args()

    rom_loader = RomLoader(args.rom if args.rom else settings.DEFAULT_ROM_NAME)
    operation_mapper = OperationMapper()
    cpu = Cpu(operation_mapper)
    input_handler = KeyboardInputHandler()
    beeper = Beeper()
    clock = pygame.time.Clock()

    pygame.font.init()
    font = pygame.font.SysFont("Arial", int(settings.SCREEN_SCALE * 2))
    renderer = Renderer(font)

    app = App(cpu, rom_loader, renderer, input_handler, beeper, clock)

    app.run()
