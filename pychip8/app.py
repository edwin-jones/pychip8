# inspiration lovingly taken from here http://lodev.org/cgtutor/raycasting.html
# and here https://www.essentialmath.com/GDC2012/GDC2012_JMV_Rotations.pdf (see 2D vec rotations)
# and here https://github.com/Mekire/pygame-raycasting-experiment

import math
import time

import pygame
from pygame.math import Vector2

from pychip8 import settings

from pychip8.cpu import Cpu
from pychip8.rom_loader import RomLoader
from pychip8.operation_mapper import OperationMapper

from numpy import uint8 as byte
import numpy

import argparse


class App:
    """primary application class"""

    def __init__(self, cpu, rom_loader, renderer, input_handler):
        self.rom_loader = rom_loader
        self.cpu = cpu
        self.renderer = renderer
        self.input_handler = input_handler
        self._running = True
        self._parser = argparse.ArgumentParser()
        self._parser.add_argument('--runto', dest='runto', help='this is a address for the program counter to run to in hex (debug mode only)')
        self.debug = __debug__

    def run(self):
        """Run the game with this method"""
        pygame.init()

        clock = pygame.time.Clock()
      
        fps = 0

        self.cpu.load_rom(self.rom_loader.get_rom())

        pygame.font.init()

        font = pygame.font.SysFont("Arial", 24)

        # allow us to run to line n while debugging
        if self.debug:
            runto = self._parser.parse_args().runto
            if runto is not None:
                target_address = int(runto, 0)
                while self.cpu.program_counter < target_address:
                    self.cpu.emulate_cycle()

        while self._running:

            input = self.input_handler.handle_input()

            run_cycle = True

            # allow super basic debugging by holding down return
            # to advance cycles (FPS will be dropped to 1 in debug mode)
            
            if self.debug:
                settings.FRAMES_PER_SECOND = 1
                run_cycle = False
                if input[pygame.K_RETURN]:
                    run_cycle = True

            if input[pygame.K_RETURN]:
                self.debug = True
                settings.FRAMES_PER_SECOND = 1

            if run_cycle:
                if self.debug:
                    self.cpu.emulate_cycle()
                else:
                    for i in range(int(settings.OPERATIONS_PER_SECOND / settings.FRAMES_PER_SECOND)): # hack to make sim speed ~500hz. TODO fix this
                        self.cpu.emulate_cycle()
                
            self.cpu.update_timers()
            
            if True:
                self.cpu.should_draw = False
                self.renderer.render(self.cpu.frame_buffer, self.cpu.get_debug_strings(), font, self.debug)

            # delay until next frame.
            clock.tick(settings.FRAMES_PER_SECOND)
            fps = math.floor(clock.get_fps())

            # allow a rudimentary step by step debugger
           

        pygame.quit()
