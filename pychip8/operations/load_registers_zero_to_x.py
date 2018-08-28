class LoadRegistersZeroToX():
    def execute(self, opcode, cpu):
        for i in range(opcode.x + 1):
            cpu.general_purpose_registers[i] = cpu.ram[cpu.index_register + i]