class SetXToDelayTimer():
    def execute(self, opcode, cpu):
        cpu.general_purpose_registers[opcode.x] = cpu.delay_timer