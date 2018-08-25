from pychip8.operations import *
from pychip8.opcode import Opcode

from collections import OrderedDict

class OperationMapper():

    def __init__(self):
        self._operations = OrderedDict()

        self._operations[0x00E0] = ClearDisplay()
        self._operations[0x1FFF] = Goto()
        self._operations[0x3FFF] = SkipIfEqual()
        self._operations[0x4FFF] = SkipIfNotEqual()
        self._operations[0x5FF0] = SkipIfXyEqual()
        
        self._operations[0x6FFF] = SetX()
        self._operations[0x7FFF] = AddToX()
        self._operations[0x8FF0] = SetXToY()
        self._operations[0x8FF1] = BitwiseOr()
        self._operations[0x8FF2] = BitwiseAnd()

        self._operations[0x8FF3] = BitwiseXor()
        self._operations[0x8FF4] = AddYToX()
        self._operations[0x8FF5] = TakeYFromX()
        self._operations[0x8FF6] = ShiftXRight()
        self._operations[0x8FF7] = TakeXFromY()

        self._operations[0x8FFE] = ShiftXLeft()
        self._operations[0x9FF0] = SkipIfXyNotEqual()
        self._operations[0xAFFF] = SetI()
        self._operations[0xBFFF] = GotoPlus()
        self._operations[0xCFFF] = Random()

        self._operations[0xFF07] = SetXToDelayTimer()
        self._operations[0xFF15] = SetDelayTimer()
        self._operations[0xFF18] = SetSoundTimer()
        self._operations[0xFF1E] = AddXToI()


    def find_operation(self, word):

        for key in self._operations:

            key_as_opcode = Opcode(key)
            word_as_opcode = Opcode(word)

            if key_as_opcode.a != word_as_opcode.a:
                continue

            mask = key | word

            if mask in self._operations:
                return self._operations[mask]

        raise KeyError(f"Opcode {word:#06x} not present in list of valid operations")

            