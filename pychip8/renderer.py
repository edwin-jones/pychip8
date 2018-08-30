"""This module defines the renderer object and related methods"""

import math
import os

import pygame
from pygame.math import Vector2

#import asset_loader
import pychip8.colors as colors
import pychip8.constants as constants
import pychip8.settings as settings

from numpy import uint8 as byte

class Renderer:
    """The default renderer of the app"""

    def __init__(self):
        screen_size = (64 * 1, 32 * 1)
        self.SCREEN = pygame.display.set_mode(screen_size)
        #self.FONT = pygame.font.SysFont(None, 48)


    #def _draw_debug_text(self, text, position):

        #text = self.FONT.render(text, True, colors.YELLOW)
        #self.SCREEN.blit(text, (position.x, position.y))


    def render(self, frame_buffer):
        """This method draws everything to the screen"""
        self.SCREEN.fill(colors.BLACK)

        for x in range(64):
            for y in range(32):
                if frame_buffer[x][y]:
                    self.SCREEN.set_at((x,y), colors.WHITE)

        #self._draw_debug_text("testing", Vector2(10, 10))

        # Go ahead and update the screen with what we've drawn.
        # This MUST happen after all the other drawing commands.
        pygame.display.update()