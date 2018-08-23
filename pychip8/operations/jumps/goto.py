from numpy import uint16

class Goto():
    def execute(self, opcode, cpu):
        cpu._program_counter = uint16(opcode.nnn)