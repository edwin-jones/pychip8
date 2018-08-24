class AddNnToX():
    def execute(self, opcode, cpu):
        cpu.general_purpose_registers[opcode.x] += opcode.nn