"""
This module defines a class that handles
mapping a 16 bit opcode value to an operation object
"""
from operation_code import Opcode
import operations as operations


class OperationMapper():
    "This class handles mapping a 16 bit opcode value to an operation object"

    def __init__(self):
        self._operations = {}

        # opcode 0NNN (call RCA 1802 program) is NOT SUPPORTED!
        self._operations[0x00E0] = operations.clear_display
        self._operations[0x00EE] = operations.return_from_function
        self._operations[0x1] = operations.goto
        self._operations[0x2] = operations.call_function
        self._operations[0x3] = operations.skip_if_equal

        self._operations[0x4] = operations.skip_if_not_equal
        self._operations[0x6] = operations.set_x
        self._operations[0x7] = operations.add_to_x
        self._operations[0xA] = operations.set_i
        self._operations[0xB] = operations.goto_plus

        self._operations[0xC] = operations.generate_random
        self._operations[0xD] = operations.draw_sprite
        self._operations[0x50] = operations.skip_if_x_y_equal
        self._operations[0x80] = operations.set_x_to_y
        self._operations[0x81] = operations.bitwise_or
        self._operations[0x82] = operations.bitwise_and
        self._operations[0x83] = operations.bitwise_xor
        self._operations[0x84] = operations.add_y_to_x
        self._operations[0x85] = operations.take_y_from_x
        self._operations[0x86] = operations.shift_x_right

        self._operations[0x87] = operations.take_x_from_y
        self._operations[0x8E] = operations.shift_x_left
        self._operations[0x90] = operations.skip_if_not_equal
        self._operations[0xE9E] = operations.skip_if_key_pressed
        self._operations[0xEA1] = operations.skip_if_key_not_pressed

        self._operations[0xF07] = operations.set_x_to_delay_timer
        self._operations[0xF0A] = operations.wait_for_key_press
        self._operations[0xF15] = operations.set_delay_timer
        self._operations[0xF18] = operations.set_sound_timer
        self._operations[0xF1E] = operations.add_x_to_i

        self._operations[0xF29] = operations.load_character_address
        self._operations[0xF33] = operations.save_x_as_bcd
        self._operations[0xF55] = operations.save_registers_zero_to_x
        self._operations[0xF65] = operations.load_registers_zero_to_x

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
