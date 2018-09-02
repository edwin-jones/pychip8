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
        screen_size = (64 * settings.SCREEN_SCALE, 32 * settings.SCREEN_SCALE)
        self.SCREEN = pygame.display.set_mode(screen_size)
        #self.FONT = pygame.font.SysFont(None, 48)


    def _draw_debug_text(self, debug_strings=[], font=None): 
        if __debug__:
            padding = font.get_linesize()
            current_y = 10
            current_x = 10
            for string in debug_strings:
                text_surface = font.render(string, False, colors.YELLOW)
                self.SCREEN.blit(text_surface, (current_x, current_y))
                current_y += padding

                if current_y > (32 * settings.SCREEN_SCALE) - padding:
                    current_y = 10
                    current_x = (64 * settings.SCREEN_SCALE) / 2 + padding


    def render(self, frame_buffer, debug_strings=[], font=None):
        """This method draws everything to the screen"""
        self.SCREEN.fill(colors.BLACK)
        scale = settings.SCREEN_SCALE

        for x in range(64):
            for y in range(32):
                if frame_buffer[x][y]:
                    pygame.draw.rect(
                        self.SCREEN,
                        colors.WHITE,
                        (x * scale, y * scale, scale, scale))

        self._draw_debug_text(debug_strings, font)

        # Go ahead and update the screen with what we've drawn.
        # This MUST happen after all the other drawing commands.
        pygame.display.update()