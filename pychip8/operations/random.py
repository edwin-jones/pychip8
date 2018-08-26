from numpy import uint8 as byte
import random

class Random():
    def execute(self, opcode, cpu):
        random_int = random.randint(0, 255)
        cpu.general_purpose_registers[opcode.x] = byte(opcode.nn & random_int)