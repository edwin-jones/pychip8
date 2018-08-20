from numpy import uint8 as byte
from numpy import uint16

class Opcode:
    """This class represents the instructions and data of an opcode"""

    def __init__(self, word):
        """
        This class takes in a 4 byte value/word and parses the bytes 
        to store them in different attributes for later use

        Args:
            word: a 4 byte/16 bit value represent an opcode.
        """

        # We use bitwise-and with a mask to extract specific nibbles.
        self._word = word
        self._a = byte((word & 0xF000) >> 12)
        self._nnn = uint16(word & 0x0FFF)
        self._nn = byte(word & 0x00FF)
        self._n = byte(word & 0x000F)
        self._x = byte((word & 0x0F00) >> 8) # Where don't use the lower nibbles, bitshift right to get just the raw value
        self._y = byte((word & 0x00F0) >> 4) # Eg. we want 0x4 not 0x40

    @property
    def a(self):
        """this attribute represents the most significant 
        byte of the opcode word value"""
        return self._a

    @property
    def x(self):
        """this attribute represents the second most significant 
        byte of the opcode word value"""
        return self._x

    @property
    def y(self):
        """this attribute represents the third most significant 
        byte of the opcode word value"""
        return self._y

    @property
    def n(self):
        """this attribute represents the least significant 
        byte of the opcode word value"""
        return self._n

    @property
    def nn(self):
        """this attribute represents the third and fourth most 
        significant bit of the opcode word value"""
        return self._nn

    @property
    def nnn(self):
        """this attribute represents the second, third and fourth most 
        significant byte of the opcode word value"""
        return self._nnn

    @property
    def word(self):
        """This attribute represents the full word/4 bytes of the opcode"""
        return self.word

    def __str__(self):
        return hex(self._word)