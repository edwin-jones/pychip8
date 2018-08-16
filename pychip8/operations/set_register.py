from pychip8.operations.operation import Operation

class SetRegister(Operation):

    def execute(self, opcode, cpu):
        cpu.main_registers[int(opcode.x)] = opcode.nn