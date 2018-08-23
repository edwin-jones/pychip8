class SetDelayTimer():
    def execute(self, opcode, cpu):
        cpu.delay_timer = opcode.x