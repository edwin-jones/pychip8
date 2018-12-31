class CallFunction():
    
    def execute(self, opcode, cpu):
        cpu.stack.append(cpu.program_counter)
        cpu.program_counter = opcode.nnn