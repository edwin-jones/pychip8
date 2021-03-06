class SkipIfKeyNotPressed():
    
    def execute(self, opcode, cpu):
        key = cpu.general_purpose_registers[opcode.x]
        if key not in cpu.keys:
            cpu.move_to_next_instruction()