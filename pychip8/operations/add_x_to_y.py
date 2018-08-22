from numpy import uint8 as byte
import numpy

class AddXtoY():
    def execute(self, opcode, cpu):

        with numpy.errstate(over='ignore'): #ignore overflows just for this code block!
            original_value = cpu.general_purpose_registers[int(opcode.x)]
            result = cpu.general_purpose_registers[int(opcode.x)] + cpu.general_purpose_registers[int(opcode.y)]
            
            if result < original_value:
                cpu.general_purpose_registers[cpu.MATH_FLAG_REGISTER_ADDRESS] = byte(1)

            cpu.general_purpose_registers[opcode.x] = result