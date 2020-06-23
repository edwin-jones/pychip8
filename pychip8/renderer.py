"""This module defines the renderer object and related methods"""

import pygame
from cpu import Cpu

WHITE = pygame.Color(255, 255, 255)
BLACK = pygame.Color(0, 0, 0)

SCALE = 10

# The CHIP-8 display ran at only 64 * 32 pixels.
# this value scales the framebuffer
# so it's easier to view the emulator on modern displays
SCREEN = pygame.display.set_mode((640, 320))

def render(frame_buffer):
    """This method draws everything to the screen"""

    SCREEN.fill(BLACK)

    for x in range(64):
        for y in range(32):
            if frame_buffer[x][y]:
                pygame.draw.rect(
                    SCREEN,
                    WHITE,
                    (x *  SCALE, y * SCALE, SCALE, SCALE))

    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.update()