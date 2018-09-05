from numpy import uint16

import pychip8.font as Font

class LoadCharacterAddress():
    def execute(self, opcode, cpu):
        cpu.index_register = uint16(cpu.general_purpose_registers[opcode.x] * Font.CHAR_SIZE_IN_BYTES)