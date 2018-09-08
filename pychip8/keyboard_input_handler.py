"""This module contains the keyboard input handler type"""

import sys
import pygame


class KeyboardInputHandler:
    """A basic keyboard input handler class"""

    _keys = {}
    _keys[pygame.K_KP0] = 0x0
    _keys[pygame.K_KP1] = 0x1
    _keys[pygame.K_KP2] = 0x2
    _keys[pygame.K_KP3] = 0x3
    _keys[pygame.K_KP4] = 0x4
    _keys[pygame.K_KP5] = 0x5
    _keys[pygame.K_KP6] = 0x6
    _keys[pygame.K_KP7] = 0x7
    _keys[pygame.K_KP8] = 0x8
    _keys[pygame.K_KP9] = 0x9
    _keys[pygame.K_0] = 0x0
    _keys[pygame.K_1] = 0x1
    _keys[pygame.K_2] = 0x2
    _keys[pygame.K_3] = 0x3
    _keys[pygame.K_4] = 0x4
    _keys[pygame.K_5] = 0x5
    _keys[pygame.K_6] = 0x6
    _keys[pygame.K_7] = 0x7
    _keys[pygame.K_8] = 0x8
    _keys[pygame.K_9] = 0x9
    _keys[pygame.K_a] = 0xA
    _keys[pygame.K_b] = 0xB
    _keys[pygame.K_c] = 0xC
    _keys[pygame.K_d] = 0xD
    _keys[pygame.K_e] = 0xE
    _keys[pygame.K_f] = 0xF

    def handle_input(self, cpu):
        """
        This function handles control input for this program.
        It returns a sequence of bools for all currently pressed keys.
        """

         # quit if user presses exit or closes the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

                if event.key in self._keys:
                    cpu.key_down(self._keys[event.key])

            if event.type == pygame.KEYUP:
                if event.key in self._keys:
                    cpu.key_up(self._keys[event.key])

        pressed = pygame.key.get_pressed()

        return pressed
