"This module defines an opcode class for parsing raw words into instructions and data"

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
<<<<<<< HEAD
        self.word = word & 0xFFFF # A word should be no larger than 16 bits.
=======
        self.word = word & 0xFFFF # we only care about 16 bit values
>>>>>>> master
        self.a = (word & 0xF000) >> 12 # we just want the most significant bits/nibble here so we bitshift right
        self.nnn = word & 0x0FFF
        self.nn = word & 0x00FF
        self.n = word & 0x000F
        self.x = (word & 0x0F00) >> 8 # Where don't use the lower nibbles, bitshift right to get just the raw value
        self.y = (word & 0x00F0) >> 4 # Eg. we want 0x4 not 0x40

    def __str__(self):
        return hex(self.word)
