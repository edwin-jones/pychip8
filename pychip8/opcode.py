from numpy import uint8 as byte
from numpy import uint16

class Opcode:
    """This class represents the instructions and data of an opcode"""

    def __init__(self, word):
        # We use bitwise-and with a mask to extract specific nibbles.

        self._word = word

        """this attribute represents the most significant bit of the opcode word value"""
        self._a = byte((word & 0xF000) >> 12)

        self._nnn = uint16(word & 0x0FFF)
        self._nn = byte(word & 0x00FF)
        self._n = byte(word & 0x000F)
        self._x = byte((word & 0x0F00) >> 8) # Where don't use the lower nibbles, bitshift right to get just the raw value
        self._y = byte((word & 0x00F0) >> 4) # Eg. we want 0x4 not 0x40

    @property
    def a(self):
        return self._a

    @property
    def x(self):
        return self._x
    @property
    def y(self):
        return self._y

    @property
    def n(self):
        return self._n

    @property
    def nn(self):
        return self._nn

    @property
    def nnn(self):
        return self._nnn

    @property
    def word(self):
        return self.word

    def __str__(self):
        return hex(self._word)