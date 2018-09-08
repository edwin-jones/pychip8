"""This module defines the main application """

import pygame

import pychip8.settings as settings

class App:
    """primary application class"""

    def __init__(self, cpu, rom_loader, renderer, input_handler, beeper):
        self.rom_loader = rom_loader
        self.cpu = cpu
        self.renderer = renderer
        self.input_handler = input_handler
        self.beeper = beeper
        self.fps = 0
        self.clock = pygame.time.Clock()
        self.font = None

    def run(self):
        """Run the app with this method"""
        self._setup()

        # main app loop
        while True:

            keys = self.input_handler.handle_input(self.cpu)

            # allow super basic debugging by holding down return
            if not __debug__ or keys[pygame.K_RETURN]:
                for i in range(settings.OPERATIONS_PER_FRAME):
                    self.cpu.emulate_cycle()

            debug_strings = self.cpu.get_debug_strings()
            debug_strings.append(f'FPS: {self.fps:02}')

            self.renderer.render(self.cpu.frame_buffer, debug_strings, self.font)

            if self.cpu.sound_timer > 0:
                self.beeper.beep()

            self.cpu.update_timers()

            # delay until next frame.
            self.clock.tick(settings.FRAMES_PER_SECOND)
            self.fps = round(self.clock.get_fps())

        pygame.quit()

    def _setup(self):
        pygame.display.set_caption(settings.APP_NAME)
        pygame.init()

        self.cpu.load_rom(self.rom_loader.get_rom_bytes(settings.ROM_NAME))

        # we cannot inject the font as pygame init takes place inside
        # this function
        pygame.font.init()

        self.font = pygame.font.SysFont("Arial", int(settings.SCREEN_SCALE * 2))

        # allow us to run to line n while debugging
        self._runto()

    def _runto(self):
        if __debug__:
            target_address = settings.RUNTO
            while self.cpu.program_counter < target_address:
                self.cpu.emulate_cycle()
