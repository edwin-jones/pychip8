"""This module contains settings and configuration data for the main game"""

import math

from pygame.math import Vector2

from pychip8 import colors
from pychip8 import constants

TARGET_FPS = 1 if __debug__ else 60
OPERATIONS_PER_SECOND = 1 if __debug__ else 500

SCREEN_SCALE = 10
