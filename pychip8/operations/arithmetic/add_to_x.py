from numpy import uint8 as byte
import numpy

class AddToX():
    def execute(self, opcode, cpu):
        with numpy.errstate(over='ignore'):
            cpu.general_purpose_registers[opcode.x] += byte(opcode.nn)