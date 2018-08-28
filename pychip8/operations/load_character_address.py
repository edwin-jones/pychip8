from numpy import uint8 as byte

import pychip8.font as Font

class LoadCharacterAddress():
    def execute(self, opcode, cpu):
        cpu.index_register = byte(opcode.x * Font.CHAR_SIZE_IN_BYTES)