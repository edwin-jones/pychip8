class SetDelayTimer():
    
    def execute(self, opcode, cpu):
        cpu.delay_timer = cpu.general_purpose_registers[opcode.x]