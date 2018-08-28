from numpy import uint8 as byte

class ClearDisplay:
    def execute(self, opcode, cpu):
        for i in range(len(cpu.frame_buffer)):
            cpu.frame_buffer[i] = byte(0)