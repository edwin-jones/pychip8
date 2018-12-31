"""This operation adds the value of 'nn' to the register 'x'"""

class AddToX():

    def execute(self, opcode, cpu):
        cpu.general_purpose_registers[opcode.x] += opcode.nn

        # restrict the value to one byte or less
        cpu.general_purpose_registers[opcode.x] &= 0xFF
