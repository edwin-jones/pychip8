"""This module contains the keyboard input handler type"""

import math
import pygame
import pychip8.settings
import sys


class KeyboardInputHandler:
    """A basic keyboard input handler class"""

    def handle_input(self):
        """This function handles control input for this program. Returns false if exit button is pressed"""

         # quit if user presses exit
        for event in pygame.event.get():
           
            if event.type == pygame.QUIT:
                sys.exit()

        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_ESCAPE]:
            sys.exit()

        return pressed
