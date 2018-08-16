from pychip8.operations.set_register import SetRegister

class OperationMapper():

    def __init__(self):
        self.operations = {}
        self.operations[0x6FFF] = SetRegister()

    def find_operation(self, opcode):

        for key in self.operations:
            mask = key | opcode.word

            if mask not in self.operations:
                raise KeyError(f"Opcode {opcode.word} not present in list of valid operations")

            return self.operations[mask]