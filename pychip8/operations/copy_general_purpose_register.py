class CopyGeneralPurposeRegister():
    def execute(self, opcode, cpu):
        cpu.main_registers[int(opcode.x)] = cpu.main_registers[int(opcode.y)]