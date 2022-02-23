"""This module defines color constants."""

from collections import namedtuple

Color = namedtuple('Color', 'r g b')

#bespoke colors
SKY_BLUE = Color(100, 149, 237)
CEILING_GRAY = Color(51, 51, 51)
FLOOR_GRAY = Color(102, 102, 102)

#standard colors
WHITE = Color(255, 255, 255)
GRAY = Color(128, 128, 128)
BLACK = Color(0, 0, 0)
YELLOW = Color(255, 255, 0)
RED = Color(255, 0, 0)
DARK_RED = Color(128, 0, 0)
GREEN = Color(0, 255, 0)
BLUE = Color(0, 0, 255)
PURPLE = Color(255, 0, 255)
ORANGE = Color(255, 128, 0)

FOREGROUND_COLORS = [WHITE, RED, GREEN, BLUE]
BACKGROUND_COLORS = [BLACK, RED, GREEN, BLUE]

