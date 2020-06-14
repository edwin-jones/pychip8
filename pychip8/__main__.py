"""This is the main entry point for the program"""

import argparse
import rom_loader
import pygame

from cpu import Cpu
from keyboard_input_handler import KeyboardInputHandler
from renderer import Renderer

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--rom", type=str, help="the name of the rom to run in the emulator")
    args = parser.parse_args()

    cpu = Cpu()
    renderer = Renderer()
    input_handler = KeyboardInputHandler()
    clock = pygame.time.Clock()
    rom_bytes = rom_loader.get_rom_bytes(args.rom if args.rom else "draw chars.ch8")
    cpu.load_rom(rom_bytes)

    pygame.display.set_caption("pychip8")
    pygame.init()

    # main loop
    while True:
        input_handler.handle_input(cpu)

        # The CHIP-8 is reported to run best at around 500 hz
        # The update loop runs at 60 fps. 60 * 8 = 480, which is close enough.
        for _ in range(8):
            cpu.emulate_cycle()

        cpu.update_timers()
        renderer.render(cpu.frame_buffer)

        # delay until next frame.
        clock.tick(60)