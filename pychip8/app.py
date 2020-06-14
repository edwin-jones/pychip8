"""This module defines the main application """

import pygame

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
        pygame.display.set_caption("pychip8")
        pygame.init()

        rom_bytes = self.rom_loader.get_rom_bytes()
        self.cpu.load_rom(rom_bytes)

    def _render(self):
        self.fps = round(self.clock.get_fps())
        self.renderer.render(self.cpu.frame_buffer)

    def _run_cycle(self):
        self.input_handler.handle_input(self.cpu)

        # The CHIP-8 is reported to run best at arround 500 hz
        # The update loop runs at 60 fps - 60 * 8 = 480, which is close enough.
        for _ in range(8):
            self.cpu.emulate_cycle()

        self.cpu.update_timers()

        self._render()

        # delay until next frame.
        self.clock.tick(60)