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


class App:
    """primary application class"""

    def __init__(self, cpu, rom_loader):
        self.rom_loader = rom_loader
        self.cpu = cpu
        self._running = True

    def run(self):
        """Run the game with this method"""
        pygame.init()

        clock = pygame.time.Clock()

        fps = 0

        self.cpu.load_rom(self.rom_loader.get_rom())

        while self._running:

            self.cpu.emulate_cycle()

            # delay until next frame.
            clock.tick(settings.TARGET_FPS)
            fps = math.floor(clock.get_fps())

        pygame.quit()
