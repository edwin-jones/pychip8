from collections import OrderedDict

from pychip8.operations import *
from pychip8.opcode import Opcode

class OperationMapper():
    "This class handles mapping a 16 bit opcode value to an operation object"

    def __init__(self):
        self._operations = {}

        self._operations[0x00E0] = ClearDisplay()
        self._operations[0x00EE] = ReturnFromFunction()

        # add 1 to the known final value so we don't omit the final part of the range
        self._operations.update(dict.fromkeys(range(0x1000, 0x1FFF + 1), Goto()))
        self._operations.update(dict.fromkeys(range(0x2000, 0x2FFF + 1), CallFunction()))
        self._operations.update(dict.fromkeys(range(0x3000, 0x3FFF + 1), SkipIfEqual()))
        self._operations.update(dict.fromkeys(range(0x4000, 0x4FFF + 1), SkipIfNotEqual()))
        self._operations.update(dict.fromkeys(range(0x6000, 0x6FFF + 1), SetX()))

        self._operations.update(dict.fromkeys(range(0x7000, 0x7FFF + 1), AddToX()))
        self._operations.update(dict.fromkeys(range(0xA000, 0xAFFF + 1), SetI()))
        self._operations.update(dict.fromkeys(range(0xB000, 0xBFFF + 1), GotoPlus()))
        self._operations.update(dict.fromkeys(range(0xC000, 0xCFFF + 1), Random()))

        # use a step of 16 so we don't add values we don't mean to the list of known opcodes
        self._operations.update(dict.fromkeys(range(0x8010, 0x8FF0 + 1, 0x0010), SetXToY()))
        self._operations.update(dict.fromkeys(range(0x8011, 0x8FF1 + 1, 0x0010), BitwiseOr()))
        self._operations.update(dict.fromkeys(range(0x8012, 0x8FF2 + 1, 0x0010), BitwiseAnd()))
        self._operations.update(dict.fromkeys(range(0x8013, 0x8FF3 + 1, 0x0010), BitwiseXor()))
        self._operations.update(dict.fromkeys(range(0x8014, 0x8FF4 + 1, 0x0010), AddYToX()))
        self._operations.update(dict.fromkeys(range(0x8015, 0x8FF5 + 1, 0x0010), TakeYFromX()))
        self._operations.update(dict.fromkeys(range(0x8016, 0x8FF6 + 1, 0x0010), ShiftXRight()))
        self._operations.update(dict.fromkeys(range(0x8017, 0x8FF7 + 1, 0x0010), TakeXFromY()))
        self._operations.update(dict.fromkeys(range(0x801E, 0x8FFE + 1, 0x0010), ShiftXLeft()))

        self._operations.update(dict.fromkeys(range(0x5010, 0x5FF0 + 1, 0x0010), SkipIfXyEqual()))
        self._operations.update(dict.fromkeys(range(0x9010, 0x9FF0 + 1, 0x0010), SkipIfXyNotEqual()))

        # use a step of 256 so we don't add values we don't mean to the list of known opcodes
        self._operations.update(dict.fromkeys(range(0xF007, 0xFF07 + 1, 0x0100), SetXToDelayTimer()))
        self._operations.update(dict.fromkeys(range(0xF015, 0xFF15 + 1, 0x0100), SetDelayTimer()))
        self._operations.update(dict.fromkeys(range(0xF018, 0xFF18 + 1, 0x0100), SetSoundTimer()))
        self._operations.update(dict.fromkeys(range(0xF01E, 0xFF1E + 1, 0x0100), AddXToI()))

    def find_operation(self, word):
        "This method takes a 16 bit value representing an opcode and returns the related operation"
        return self._operations[word]
