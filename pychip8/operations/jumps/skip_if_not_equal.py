class SkipIfNotEqual():
    def execute(self, opcode, cpu):
        if(cpu.general_purpose_registers[opcode.x] != opcode.nn):
            cpu.move_to_next_instruction()