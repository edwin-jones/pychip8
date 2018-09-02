"""This module contains the keyboard input handler type"""

import math
import pygame
import pychip8.settings
import sys


class KeyboardInputHandler:
    """A basic keyboard input handler class"""

    def handle_input(self):
        """This function handles control input for this program. Returns false if exit button is pressed"""

        for event in pygame.event.get():
            # quit if user presses exit
            if event.type == pygame.QUIT:
                sys.exit()

        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_ESCAPE]:
            pygame.exit()
            sys.exit()
