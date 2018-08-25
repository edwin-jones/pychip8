from numpy import uint8 as byte
import numpy

class TakeXFromY():
    def execute(self, opcode, cpu):
        
        cpu.clear_arithmetic_flag()

        with numpy.errstate(over='ignore'): #ignore underflows just for this code block!
            original_value = cpu.general_purpose_registers[opcode.x]
            result = cpu.general_purpose_registers[opcode.y] - cpu.general_purpose_registers[opcode.x]
            
            if result > original_value:
                cpu.set_arithmetic_flag()

            cpu.general_purpose_registers[opcode.x] = result