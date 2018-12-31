class AddXToI():

    def execute(self, opcode, cpu):

        cpu.clear_arithmetic_flag()
        original_value = cpu.index_register
        result = cpu.index_register + cpu.general_purpose_registers[opcode.x]

        # restrict the value to two bytes or less
        result &= 0xFFFF

        if result < original_value:
            cpu.set_arithmetic_flag()

        cpu.index_register = result
