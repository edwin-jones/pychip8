from numpy import uint8 as byte
from numpy import uint16

class Opcode:
    """This class represents the instructions and data of an opcode"""

    def __init__(self, word):
        # We use bitwise-and with a mask to extract specific nibbles.

        self.word = word
        self.A = byte(opcode & 0xF000)

        self.NNN = uint16(opcode & 0x0FFF),
        self.NN = byte(opCode & 0x00FF),
        self.N = byte(opCode & 0x000F),
        self.X = byte((opCode & 0x0F00) >> 8), # Where don't use the lower nibbles, bitshift right to get just the raw value
        self.Y = byte((opCode & 0x00F0) >> 4), # Eg. we want 0x4 not 0x40