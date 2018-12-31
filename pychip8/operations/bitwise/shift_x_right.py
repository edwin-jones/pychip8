from pychip8.cpu import Cpu

class ShiftXRight():
    def execute(self, opcode, cpu):
        least_significant_bit = cpu.general_purpose_registers[opcode.x] & 0x01
        cpu.general_purpose_registers[Cpu.ARITHMETIC_FLAG_REGISTER_ADDRESS] = least_significant_bit
        cpu.general_purpose_registers[opcode.x] = cpu.general_purpose_registers[opcode.x] >> 1 # restrict the shifted value to one byte or less
