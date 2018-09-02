# inspiration lovingly taken from here http://lodev.org/cgtutor/raycasting.html
# and here https://www.essentialmath.com/GDC2012/GDC2012_JMV_Rotations.pdf (see 2D vec rotations)
# and here https://github.com/Mekire/pygame-raycasting-experiment

import math

import pygame
from pygame.math import Vector2

from pychip8 import settings

from pychip8.cpu import Cpu
from pychip8.rom_loader import RomLoader
from pychip8.operation_mapper import OperationMapper

from numpy import uint8 as byte
import numpy


class App:
    """primary application class"""

    def __init__(self, cpu, rom_loader, renderer, input_handler):
        self.rom_loader = rom_loader
        self.cpu = cpu
        self.renderer = renderer
        self.input_handler = input_handler
        self._running = True

    def run(self):
        """Run the game with this method"""
        pygame.init()

        clock = pygame.time.Clock()

        fps = 0

        self.cpu.load_rom(self.rom_loader.get_rom())

        pygame.font.init()

        font = pygame.font.SysFont("Arial", 24)

        while self._running:

            self.input_handler.handle_input()
            self.cpu.emulate_cycle()
            self.renderer.render(self.cpu.frame_buffer, self.cpu.get_debug_strings(), font)

            # delay until next frame.
            clock.tick(settings.TARGET_FPS)
            fps = math.floor(clock.get_fps())

        pygame.quit()
