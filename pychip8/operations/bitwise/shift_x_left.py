from numpy import uint8 as byte
from pychip8.cpu import Cpu

class ShiftXLeft():
    def execute(self, opcode, cpu):
        most_significant_bit = cpu.general_purpose_registers[opcode.x] >> 7
        cpu.general_purpose_registers[Cpu.ARITHMETIC_FLAG_REGISTER_ADDRESS] = byte(most_significant_bit)
        cpu.general_purpose_registers[opcode.x] = byte(cpu.general_purpose_registers[opcode.x] << 1)