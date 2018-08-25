from numpy import uint16

class GotoPlus():
    def execute(self, opcode, cpu):
        cpu._program_counter = uint16(cpu.general_purpose_registers[0] + opcode.nnn)