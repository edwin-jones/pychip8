from numpy import uint8 as byte
import numpy

class AddXToI():

    def execute(self, opcode, cpu):

        with numpy.errstate(over='ignore'): #ignore overflows just for this code block!
            cpu.clear_arithmetic_flag()
            original_value = cpu.index_register
            result = cpu.index_register + cpu.general_purpose_registers[opcode.x]
            
            if result < original_value:
                cpu.set_arithmetic_flag()

            cpu.index_register +=  cpu.general_purpose_registers[opcode.x]