"""This module defines the renderer object and related methods"""

import pygame

from cpu import Cpu
import colors


class Renderer:
    """The default renderer of the app"""

    def __init__(self):

        # The CHIP-8 display ran at only 64 * 32 pixels.
        # this value scales the framebuffer
        # so it's easier to view the emulator on modern displays
        self.scale = 10

        screen_size = (
            Cpu.FRAME_BUFFER_WIDTH * self.scale,
            Cpu.FRAME_BUFFER_HEIGHT * self.scale)

        self.screen = pygame.display.set_mode(screen_size)


    def render(self, frame_buffer):
        """This method draws everything to the screen"""

        self.screen.fill(colors.BLACK)

        for x in range(Cpu.FRAME_BUFFER_WIDTH):
            for y in range(Cpu.FRAME_BUFFER_HEIGHT):
                if frame_buffer[x][y]:
                    pygame.draw.rect(
                        self.screen,
                        colors.WHITE,
                        (x *  self.scale, y *  self.scale,  self.scale,  self.scale))

        # Go ahead and update the screen with what we've drawn.
        # This MUST happen after all the other drawing commands.
        pygame.display.update()
