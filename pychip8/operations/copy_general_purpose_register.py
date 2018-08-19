class CopyGeneralPurposeRegister():
    def execute(self, opcode, cpu):
        cpu.general_purpose_registers[int(opcode.x)] = cpu.general_purpose_registers[int(opcode.y)]