class SaveXAsBcd():
    """
    this opcode saves the value of register X as binary coded decimal value in three bytes of ram,
    starting at the current index register address and ending at that address + 2
    """
    def execute(self, opcode, cpu):
        value = cpu.general_purpose_registers[opcode.x]
        cpu.ram[cpu.index_register] = int(value / 100) & 0xFF # store the most significant digit as a byte
        cpu.ram[cpu.index_register + 1] = int((value / 10) % 10) & 0xFF # store the middle digit as a byte
        cpu.ram[cpu.index_register + 2] = int(value % 10) & 0xFF # store the least significant digit as a byte
