from numpy import uint8 as byte

class ClearDisplay:
    def execute(self, opcode, cpu):
        for x in range(cpu.FRAME_BUFFER_WIDTH):
            for y in range(cpu.FRAME_BUFFER_HEIGHT):
                cpu.frame_buffer[x][y] = bool()