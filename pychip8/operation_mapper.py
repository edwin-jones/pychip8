from pychip8.operations import *
from pychip8.opcode import Opcode

class OperationMapper():

    def __init__(self):
        self.operations = {}
        self.operations[0x6FFF] = SetGeneralPurposeRegister()
        self.operations[0x8FF0] = CopyGeneralPurposeRegister()
        self.operations[0xAFFF] = SetIndexRegister()
        self.operations[0xFF15] = SetDelayTimer()
        self.operations[0xFF18] = SetSoundTimer()

    def find_operation(self, word):

        for key in self.operations:

            key_as_opcode = Opcode(key)
            word_as_opcode = Opcode(word)

            if key_as_opcode.a != word_as_opcode.a:
                continue

            mask = key | word

            if mask in self.operations:
                return self.operations[mask]

        raise KeyError(f"Opcode {word:#06x} not present in list of valid operations")

            