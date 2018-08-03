# inspiration lovingly taken from here http://lodev.org/cgtutor/raycasting.html
# and here https://www.essentialmath.com/GDC2012/GDC2012_JMV_Rotations.pdf (see 2D vec rotations)
# and here https://github.com/Mekire/pygame-raycasting-experiment

import math

import pygame
from pygame.math import Vector2

import settings

class App:
    """primary application class"""

    def __init__(self, renderer, input_handler):
        self._renderer = renderer
        #self._player = player
        self._input_handler = input_handler
        self._running = True

    def run(self):
        """Run the game with this method"""
        pygame.init()

        clock = pygame.time.Clock()

        fps = 0

        while self._running:

            self._running = self._input_handler.handle_input()
            self._renderer.render()

            # delay until next frame.
            clock.tick(settings.TARGET_FPS)
            fps = math.floor(clock.get_fps())

        pygame.quit()
