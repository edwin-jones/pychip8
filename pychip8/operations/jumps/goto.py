class Goto():
    
    def execute(self, opcode, cpu):
        cpu.program_counter = opcode.nnn
        cpu.program_counter &= 0xFFFF # restrict the PC value to two bytes or less
