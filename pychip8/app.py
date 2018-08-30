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

        test_buffer = [byte(0)] * (8 * 32)

        for i in range(8 * 32):
            test_buffer[0] = byte(0xFF)
            test_buffer[9] = byte(0xFF)
            test_buffer[18] = byte(0xFF)

        while self._running:

            self.input_handler.handle_input()
            self.cpu.emulate_cycle()
            self.renderer.render(test_buffer)

            # delay until next frame.
            clock.tick(settings.TARGET_FPS)
            fps = math.floor(clock.get_fps())

        pygame.quit()
