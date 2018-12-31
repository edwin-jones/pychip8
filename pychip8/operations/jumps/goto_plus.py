class GotoPlus():
    
    def execute(self, opcode, cpu):
        cpu.program_counter = cpu.general_purpose_registers[0] + opcode.nnn
        cpu.program_counter &= 0xFFFF # restrict the PC value to two bytes or less
