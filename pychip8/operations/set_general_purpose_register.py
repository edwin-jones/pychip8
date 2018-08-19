class SetGeneralPurposeRegister():
    def execute(self, opcode, cpu):
        cpu.main_registers[int(opcode.x)] = opcode.nn