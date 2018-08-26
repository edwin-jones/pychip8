from pychip8.operations import *
from pychip8.opcode import Opcode

from collections import OrderedDict

class OperationMapper():

    def __init__(self):
        self._valid_opcodes = set() # use a set rather than a list for iteration speed
        self._set_valid_opcodes()
        self._operations = OrderedDict()
        self._set_operation_mappings()

    def _set_valid_opcodes(self):
        self._valid_opcodes.add(0x00E0)
        self._valid_opcodes.add(0x00EE)

        # add 1 to the known final value so we don't omit the final part of the range
        self._valid_opcodes.update(range(0x1000, 0x1FFF + 1))
        self._valid_opcodes.update(range(0x2000, 0x2FFF + 1))
        self._valid_opcodes.update(range(0x3000, 0x3FFF + 1))
        self._valid_opcodes.update(range(0x4000, 0x4FFF + 1))
        self._valid_opcodes.update(range(0x5010, 0x5FF0 + 1))
        self._valid_opcodes.update(range(0x6000, 0x6FFF + 1))
        self._valid_opcodes.update(range(0x7000, 0x7FFF + 1))
        self._valid_opcodes.update(range(0x8010, 0x8FFE + 1))
        self._valid_opcodes.update(range(0x9010, 0x9FF0 + 1))
        self._valid_opcodes.update(range(0xA000, 0xAFFF + 1))
        self._valid_opcodes.update(range(0xB000, 0xBFFF + 1))
        self._valid_opcodes.update(range(0xC000, 0xCFFF + 1))

        #use a step of 256 so we don't add values we don't mean to the list of known opcodes
        self._valid_opcodes.update(range(0xF007, 0xFF07 + 1, 0x0100)) 
        self._valid_opcodes.update(range(0xF015, 0xFF15 + 1, 0x0100))
        self._valid_opcodes.update(range(0xF018, 0xFF18 + 1, 0x0100))
        self._valid_opcodes.update(range(0xF01E, 0xFF1E + 1, 0x0100))

    def _set_operation_mappings(self):
        self._operations[0x00E0] = ClearDisplay()
        self._operations[0x00EE] = ReturnFromFunction()
        self._operations[0x1FFF] = Goto()
        self._operations[0x2FFF] = CallFunction()
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

        if word in self._valid_opcodes:

            for key in self._operations:

                key_as_opcode = Opcode(key)
                word_as_opcode = Opcode(word)

                if key_as_opcode.a != word_as_opcode.a:
                    continue

                mask = key | word

                if mask in self._operations:
                    return self._operations[mask]

        raise KeyError(f"Opcode {word:#06x} not present in list of valid operations")