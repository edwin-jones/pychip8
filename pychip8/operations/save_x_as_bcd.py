from numpy import uint8 as byte

class SaveXAsBcd():
    """
    this opcode saves the value of register X as binary coded decimal value in three bytes of ram,
    starting at the current index register address and ending at that address + 2
    """
    def execute(self, opcode, cpu):
        value = cpu.general_purpose_registers[opcode.x]
        cpu.ram[cpu.index_register] = byte(value / 100) # store the most significant digit
        cpu.ram[cpu.index_register + 1] = byte((value / 10) % 10) # store the middle digit
        cpu.ram[cpu.index_register + 2] = byte(value % 10) # store the least significant digit
