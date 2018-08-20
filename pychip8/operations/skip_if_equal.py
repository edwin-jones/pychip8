class SkipIfEqual():
    def execute(self, opcode, cpu):
        if(cpu.general_purpose_registers[opcode.x] == opcode.nn):
            cpu.program_counter += 1