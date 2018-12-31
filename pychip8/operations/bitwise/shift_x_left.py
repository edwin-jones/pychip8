from pychip8.cpu import Cpu

class ShiftXLeft():
    def execute(self, opcode, cpu):
        most_significant_bit = (cpu.general_purpose_registers[opcode.x] >> 7)
        cpu.general_purpose_registers[Cpu.ARITHMETIC_FLAG_REGISTER_ADDRESS] = most_significant_bit
        cpu.general_purpose_registers[opcode.x] = (cpu.general_purpose_registers[opcode.x] << 1) & 0xFF # restrict the shifted value to one byte or less