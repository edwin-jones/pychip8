"""This module defines the main application """

import pygame

import pychip8.settings as settings

class App:
    """primary application class"""

    def __init__(self, cpu, rom_loader, renderer, input_handler, beeper, clock):
        self.rom_loader = rom_loader
        self.cpu = cpu
        self.renderer = renderer
        self.input_handler = input_handler
        self.beeper = beeper
        self.fps = 0
        self.clock = clock

    def run(self):
        """Run the app with this method"""
        self._setup()

        # main loop
        while True:
            self._run_cycle()

    def _runto(self):
        if __debug__:
            target_address = settings.RUNTO
            while self.cpu.program_counter < target_address:
                self.cpu.emulate_cycle()

    def _setup(self):
        pygame.display.set_caption(settings.APP_NAME)
        pygame.init()

        rom_bytes = self.rom_loader.get_rom_bytes(settings.ROM_NAME)
        self.cpu.load_rom(rom_bytes)

        # allow us to run to line n while debugging
        self._runto()

    def _render(self):
        self.fps = round(self.clock.get_fps())
        debug_strings = None

        if __debug__:
            debug_strings = self.cpu.get_debug_strings()
            debug_strings.append(f'FPS: {self.fps:02}')

        self.renderer.render(self.cpu.frame_buffer, debug_strings)

    def _run_cycle(self):
        keys = self.input_handler.handle_input(self.cpu)

        # allow basic debugging by holding down return
        if not __debug__ or keys[pygame.K_RETURN]:
            for i in range(settings.OPERATIONS_PER_FRAME):
                self.cpu.emulate_cycle()
        if self.cpu.sound_timer > 0:
            self.beeper.beep()

        # the CHIP-8 timers were locked at 60 hz.
        # we should try to keep this rate no matter the actual fps/update speed
        for i in range(settings.TIMER_UPDATES_PER_SECOND):
            self.cpu.update_timers()

        self._render()

        # delay until next frame.
        self.clock.tick(settings.FRAMES_PER_SECOND)
