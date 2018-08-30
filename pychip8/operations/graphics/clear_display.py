from numpy import uint8 as byte

class ClearDisplay:
    def execute(self, opcode, cpu):
        for x in range(64):
            for y in range(32):
                cpu.frame_buffer[x][y] = bool()