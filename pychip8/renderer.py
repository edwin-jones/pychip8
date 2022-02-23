"""This module defines the renderer object and related methods"""


import pygame

from pychip8.cpu import Cpu
import pychip8.colors as colors
import pychip8.settings as settings


class Renderer:
    """The default renderer of the app"""

    def __init__(self, font=None, scale=settings.SCREEN_SCALE):
        self.font = font
        self.scale = scale
        self.foreground_color_index = 0
        self.background_color_index = 0

        screen_size = (
            Cpu.FRAME_BUFFER_WIDTH * self.scale,
            Cpu.FRAME_BUFFER_HEIGHT * self.scale)

        self.screen = pygame.display.set_mode(screen_size)


    def _draw_debug_text(self, debug_strings):
        if self.font:
            padding = self.font.get_linesize()
            current_y = 10
            current_x = 10

            for string in debug_strings:
                text_surface = self.font.render(string, False, colors.YELLOW)
                self.screen.blit(text_surface, (current_x, current_y))
                current_y += padding

                if current_y > (Cpu.FRAME_BUFFER_HEIGHT * self.scale) - padding:
                    current_y = 10
                    current_x = (Cpu.FRAME_BUFFER_WIDTH * self.scale) / 2 + padding


    def render(self, frame_buffer, debug_strings=None):
        """This method draws everything to the screen"""

        self.screen.fill(colors.BACKGROUND_COLORS[self.background_color_index])

        for x in range(Cpu.FRAME_BUFFER_WIDTH):
            for y in range(Cpu.FRAME_BUFFER_HEIGHT):
                if frame_buffer[x][y]:
                    pygame.draw.rect(
                        self.screen,
                        colors.FOREGROUND_COLORS[self.foreground_color_index],
                        (x *  self.scale, y *  self.scale,  self.scale,  self.scale))

        if debug_strings:
            self._draw_debug_text(debug_strings)

        # Go ahead and update the screen with what we've drawn.
        # This MUST happen after all the other drawing commands.
        pygame.display.update()
