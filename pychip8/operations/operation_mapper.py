from pychip8.operations import *

class OperationMapper():

    def __init__(self):
        self.operations = {}
        self.operations[0x6FFF] = SetRegister()
        self.operations[0x8FF0] = CopyRegister()

    def find_operation(self, opcode):

        for key in self.operations:
            mask = key | opcode.word

            if mask in self.operations:
                return self.operations[mask]

        raise KeyError(f"Opcode {opcode.word:#06x} not present in list of valid operations")

            