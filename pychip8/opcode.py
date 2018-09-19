"This modules defines an opcode class for parsing raw words into instructions and data"

from numpy import uint8 as byte
from numpy import uint16

class Opcode:
    """This class represents the instructions and data of an opcode"""

    def __init__(self, word):
        """
        This class takes in a 2 byte value/word and parses the bytes 
        to store them in different attributes for later use

        Args:
            word: a 2 byte/16 bit value represent an opcode.
        """

        # We use bitwise-and with a mask to extract specific nibbles.
        self.word = uint16(word)
        self.a = byte((word & 0xF000) >> 12) # we just want the most significant bits/nibble here so we bitshift right
        self.nnn = uint16(word & 0x0FFF)
        self.nn = byte(word & 0x00FF)
        self.n = byte(word & 0x000F)
        self.x = byte((word & 0x0F00) >> 8) # Where don't use the lower nibbles, bitshift right to get just the raw value
        self.y = byte((word & 0x00F0) >> 4) # Eg. we want 0x4 not 0x40

    def __str__(self):
        return hex(self.word)
