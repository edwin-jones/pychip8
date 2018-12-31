class WaitForKeyPress():
    
    def execute(self, opcode, cpu):
        if not cpu.keys:
            cpu.move_to_previous_instruction()
        else:
            cpu.general_purpose_registers[opcode.x] = sorted(cpu.keys)[0]
