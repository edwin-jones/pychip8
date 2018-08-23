class BitwiseXor():
    def execute(self, opcode, cpu):
        cpu.general_purpose_registers[opcode.x] = cpu.general_purpose_registers[opcode.x] ^ cpu.general_purpose_registers[opcode.y] 