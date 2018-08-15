from numpy import uint8 as byte
from numpy import uint16

class Opcode:
    """This class represents the instructions and data of an opcode"""

    def __init__(self, word):
        # We use bitwise-and with a mask to extract specific nibbles.

        self.word = word
        self.a = byte((word & 0xF000) >> 12)

        self.nnn = uint16(word & 0x0FFF)
        self.nn = byte(word & 0x00FF)
        self.n = byte(word & 0x000F)
        self.x = byte((word & 0x0F00) >> 8) # Where don't use the lower nibbles, bitshift right to get just the raw value
        self.y = byte((word & 0x00F0) >> 4) # Eg. we want 0x4 not 0x40