class TakeYFromX():

    def execute(self, opcode, cpu):

        cpu.set_arithmetic_flag()

        original_value = cpu.general_purpose_registers[opcode.x]
        result = cpu.general_purpose_registers[opcode.x] - cpu.general_purpose_registers[opcode.y]

        # restrict the value to one byte or less
        result &= 0xFF

        if result > original_value:
            cpu.clear_arithmetic_flag()

        cpu.general_purpose_registers[opcode.x] = result

