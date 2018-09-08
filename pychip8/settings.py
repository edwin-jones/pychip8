"""This module contains settings and configuration data for the main game"""

import math

from pygame.math import Vector2

from pychip8 import colors
from pychip8 import constants

FRAMES_PER_SECOND = 60
OPERATIONS_PER_SECOND = 500
OPERATIONS_PER_FRAME = int(OPERATIONS_PER_SECOND / FRAMES_PER_SECOND)

SCREEN_SCALE = 10
