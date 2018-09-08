# inspiration lovingly taken from here http://lodev.org/cgtutor/raycasting.html
# and here https://www.essentialmath.com/GDC2012/GDC2012_JMV_Rotations.pdf (see 2D vec rotations)
# and here https://github.com/Mekire/pygame-raycasting-experiment

import math
import time

import pygame

from pychip8.cpu import Cpu
from pychip8.rom_loader import RomLoader
from pychip8.operation_mapper import OperationMapper
from numpy import uint8 as byte
import numpy




class App:
    """primary application class"""

    def __init__(self, settings, cpu, rom_loader, renderer, input_handler, beeper):
        self.settings = settings
        self.rom_loader = rom_loader
        self.cpu = cpu
        self.renderer = renderer
        self.input_handler = input_handler
        self.beeper = beeper

    def run(self):
        """Run the app with this method"""
        pygame.display.set_caption(self.settings.APP_NAME)
        pygame.init()

        clock = pygame.time.Clock()
      
        fps = 0

        self.cpu.load_rom(self.rom_loader.get_rom_bytes(self.settings.ROM_NAME))

        pygame.font.init()

        font = pygame.font.SysFont("Arial", int(self.settings.SCREEN_SCALE * 2))

        # allow us to run to line n while debugging
        self._runto()

        while True:

            input = self.input_handler.handle_input(self.cpu)

            # allow super basic debugging by holding down return
            if not __debug__ or input[pygame.K_RETURN]:
                for i in range(self.settings.OPERATIONS_PER_FRAME):
                    self.cpu.emulate_cycle()

            debug_strings = self.cpu.get_debug_strings()
            debug_strings.append(f'FPS: {fps:02}')

            self.renderer.render(self.cpu.frame_buffer, debug_strings, font)

            if self.cpu.sound_timer > 0:
                self.beeper.beep()

            self.cpu.update_timers()

            # delay until next frame.
            clock.tick(self.settings.FRAMES_PER_SECOND)
            fps = math.ceil(clock.get_fps())

        pygame.quit()

    def _runto(self):
        if __debug__:
            target_address = int(self.settings.RUNTO, 0)
            while self.cpu.program_counter < target_address:
                self.cpu.emulate_cycle()
