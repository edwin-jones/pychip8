"""This is the main entry point for the program"""

import argparse

import pygame
import settings

from rom_loader import RomLoader
from operation_mapper import OperationMapper
from cpu import Cpu
from app import App
from renderer import Renderer
from keyboard_input_handler import KeyboardInputHandler

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--rom", type=str, help="the name of the rom to run in the emulator")
    args = parser.parse_args()

    rom_loader = RomLoader(args.rom if args.rom else settings.DEFAULT_ROM_NAME)
    operation_mapper = OperationMapper()
    cpu = Cpu(operation_mapper)
    input_handler = KeyboardInputHandler()
    clock = pygame.time.Clock()
    scale = max(min(settings.SCREEN_SCALE, 100), 1)

    pygame.font.init()
    font = pygame.font.SysFont("Arial", int(scale * 2))

    renderer = Renderer(font, scale)

    app = App(cpu, rom_loader, renderer, input_handler, clock)

    app.run()