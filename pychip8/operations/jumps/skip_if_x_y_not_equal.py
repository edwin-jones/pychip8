class SkipIfXyNotEqual():
    
    def execute(self, opcode, cpu):
        if(cpu.general_purpose_registers[opcode.x] != cpu.general_purpose_registers[opcode.y]):
            cpu.move_to_next_instruction()