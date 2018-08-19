class SetSoundTimer():
    def execute(self, opcode, cpu):
        cpu.sound_timer = opcode.x