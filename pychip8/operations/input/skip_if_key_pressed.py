class SkipIfKeyPressed():
    def execute(self, opcode, cpu):
        key = opcode.x
        if key in cpu.keys:
            cpu.move_to_next_instruction()