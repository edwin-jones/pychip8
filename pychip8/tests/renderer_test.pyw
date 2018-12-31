"""This module is a simple debug render test to confirm the renderer module is working as expected"""

from pychip8.renderer import Renderer
from pychip8.keyboard_input_handler import KeyboardInputHandler

import pychip8.settings as settings
import pygame


def _get_test_buffer():
    # test buffer with debug pattern
    # should draw an x with a 1 px thick
    # border that has 1 pixel of padding from the edges
    # there should be a square dot near the top left edge
    test_buffer = [[bool()] * 32 for x in range(64)]

    test_buffer[3][6] = True
    for x in range(64):
        y = int(x/2)
        test_buffer[1][y] = True
        test_buffer[62][y] = True
        test_buffer[x][1] = True
        test_buffer[x][30] = True
        test_buffer[x][y] = True
        test_buffer[x][31 - y] = True

    return test_buffer

def run():
    frame_buffer = _get_test_buffer()
    pygame.init()

    renderer = Renderer()
    input_handler = KeyboardInputHandler()
    clock = pygame.time.Clock()

    while True:
        input_handler.handle_input()
        renderer.render(frame_buffer)
        clock.tick(settings.FRAMES_PER_SECOND)

run()