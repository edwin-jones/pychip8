class SkipIfXyEqual():
    def execute(self, opcode, cpu):
        if(cpu.general_purpose_registers[opcode.x] == cpu.general_purpose_registers[opcode.y]):
            cpu.program_counter += 2