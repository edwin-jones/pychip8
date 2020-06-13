"""This module defines the main application """

import pygame
import settings

class App:
    """primary application class"""

    def __init__(self, cpu, rom_loader, renderer, input_handler, clock):
        self.rom_loader = rom_loader
        self.cpu = cpu
        self.renderer = renderer
        self.input_handler = input_handler
        self.fps = 0
        self.clock = clock

    def run(self):
        """Run the app with this method"""
        self._setup()

        # main loop
        while True:
            self._run_cycle()

    def _setup(self):
        pygame.display.set_caption(settings.APP_NAME)
        pygame.init()

        rom_bytes = self.rom_loader.get_rom_bytes()
        self.cpu.load_rom(rom_bytes)

    def _render(self):
        self.fps = round(self.clock.get_fps())
        self.renderer.render(self.cpu.frame_buffer)

    def _run_cycle(self):
        self.input_handler.handle_input(self.cpu)
        for _ in range(settings.OPERATIONS_PER_FRAME):
            self.cpu.emulate_cycle()

        # the CHIP-8 timers were locked at 60 hz.
        # we should try to keep this rate no matter the actual fps/update speed
        for _ in range(settings.TIMER_UPDATES_PER_SECOND):
            self.cpu.update_timers()

        self._render()

        # delay until next frame.
        self.clock.tick(settings.FRAMES_PER_SECOND)