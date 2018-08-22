class IncrementGeneralPurposeRegister():
    def execute(self, opcode, cpu):
        cpu.general_purpose_registers[int(opcode.x)] += opcode.nn