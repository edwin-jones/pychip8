from pychip8.operations.operation import Operation

class CopyGeneralPurposeRegister(Operation):
    
    def execute(self, opcode, cpu):
        cpu.main_registers[int(opcode.x)] = cpu.main_registers[int(opcode.y)]