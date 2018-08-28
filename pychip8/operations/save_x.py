class SaveX():
    def execute(self, opcode, cpu):
        for i in range(opcode.x + 1):
            cpu.ram[cpu.index_register + i] = cpu.general_purpose_registers[i]