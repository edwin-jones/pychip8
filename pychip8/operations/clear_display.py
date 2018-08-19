from numpy import uint8 as byte

class ClearDisplay:
    def execute(self, opcode, cpu):
        for i, value in enumerate(cpu.frame_buffer):
            cpu.frame_buffer[i] = byte(0)