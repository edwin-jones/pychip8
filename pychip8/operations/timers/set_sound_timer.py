class SetSoundTimer():
    def execute(self, opcode, cpu):
        cpu.sound_timer = cpu.general_purpose_registers[opcode.x]