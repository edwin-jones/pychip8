class ReturnFromFunction():
    
    def execute(self, opcode, cpu):
        address = cpu.stack.pop()
        cpu.program_counter = address