"""
This module defines a class that handles
mapping a 16 bit opcode value to an operation object
"""

from pychip8.operations import *
from pychip8.opcode import Opcode


class OperationMapper():
    "This class handles mapping a 16 bit opcode value to an operation object"

    def __init__(self):
        self._operations = {}

        # opcode 0NNN (call RCA 1802 program) is NOT SUPPORTED!
        self._operations[0x00E0] = ClearDisplay()
        self._operations[0x00EE] = ReturnFromFunction()
        self._operations[0x1] = Goto()
        self._operations[0x2] = CallFunction()
        self._operations[0x3] = SkipIfEqual()

        self._operations[0x4] = SkipIfNotEqual()
        self._operations[0x6] = SetX()
        self._operations[0x7] = AddToX()
        self._operations[0xA] = SetI()
        self._operations[0xB] = GotoPlus()

        self._operations[0xC] = Random()
        self._operations[0xD] = DrawSprite()
        self._operations[0x50] = SkipIfXyEqual()
        self._operations[0x80] = SetXToY()
        self._operations[0x81] = BitwiseOr()

        self._operations[0x82] = BitwiseAnd()
        self._operations[0x83] = BitwiseXor()
        self._operations[0x84] = AddYToX()
        self._operations[0x85] = TakeYFromX()
        self._operations[0x86] = ShiftXRight()

        self._operations[0x87] = TakeXFromY()
        self._operations[0x8E] = ShiftXLeft()
        self._operations[0x90] = SkipIfXyNotEqual()
        self._operations[0xE9E] = SkipIfKeyPressed()
        self._operations[0xEA1] = SkipIfKeyNotPressed()

        self._operations[0xF07] = SetXToDelayTimer()
        self._operations[0xF0A] = WaitForKeyPress()
        self._operations[0xF15] = SetDelayTimer()
        self._operations[0xF18] = SetSoundTimer()
        self._operations[0xF1E] = AddXToI()

        self._operations[0xF29] = LoadCharacterAddress()
        self._operations[0xF33] = SaveXAsBcd()
        self._operations[0xF55] = SaveRegistersZeroToX()
        self._operations[0xF65] = LoadRegistersZeroToX()

    def find_operation(self, word):
        "This method takes a 16 bit value representing an opcode and returns the related operation"

        opcode = Opcode(word)

        # make a key of a + n + n so that 0xA123 becomes 0xA23
        twelve_bit_key = int((opcode.a << 8) + opcode.nn)
        if twelve_bit_key in self._operations:
            return self._operations[twelve_bit_key]

        # make a key of a + n so that 0xA123 becomes 0xA3
        eight_bit_key = int((opcode.a << 4) + opcode.n)
        if eight_bit_key in self._operations:
            return self._operations[eight_bit_key]

        four_bit_key = opcode.a
        if four_bit_key in self._operations:
            return self._operations[four_bit_key]

        raise KeyError(f"Opcode {word:#06x} not present in list of valid operations")
