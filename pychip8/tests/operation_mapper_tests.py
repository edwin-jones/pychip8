from pychip8.opcode import Opcode
from pychip8.operation_mapper import OperationMapper
from pychip8.operations import *

import unittest

 
class TestOperationMapper(unittest.TestCase):

    def setUp(self):
        self.opcode = Opcode(0xABCD)
        self.operation_mapper = OperationMapper()

    def _test_mapping(self, word, operation_type):
        operation = self.operation_mapper.find_operation(word)
        self.assertIsInstance(operation, operation_type)

    def test_thows_if_no_mapping(self):
        self.assertRaises(KeyError, self.operation_mapper.find_operation, 0x2FFF)

    def test_set_index_register_mapping(self):
        self._test_mapping(0xA123, SetI)

    def test_set_general_purpose_register_mapping(self):
        self._test_mapping(0x61CD, SetX)

    def test_incremement_general_purpose_register_mapping(self):
        self._test_mapping(0x71CD, AddToX)

    def test_copy_general_purpose_register_mapping(self):
        self._test_mapping(0x8120, SetXToY)

    def test_set_delay_timer_mapping(self):
        self._test_mapping(0xF615, SetDelayTimer)

    def test_set_sound_timer_mapping(self):
        self._test_mapping(0xF618, SetSoundTimer)
    
    def test_clear_display_mapping(self):
        self._test_mapping(0x00E0, ClearDisplay)
    
    def test_goto(self):
        self._test_mapping(0x1000, Goto)

    def test_skip_if_equal_mapping(self):
        self._test_mapping(0x3122, SkipIfEqual)

    def test_skip_if_not_equal_mapping(self):
        self._test_mapping(0x4122, SkipIfNotEqual)

    def test_skip_x_y_equal_mapping(self):
        self._test_mapping(0x5120, SkipIfXyEqual)

    def test_bitwise_or_mapping(self):
        self._test_mapping(0x8121, BitwiseOr)
    
    def test_bitwise_and_mapping(self):
        self._test_mapping(0x8122, BitwiseAnd)

    def test_bitwise_xor_mapping(self):
        self._test_mapping(0x8123, BitwiseXor)

    def test_add_y_to_x_mapping(self):
        self._test_mapping(0x8124, AddYToX)

    def test_take_y_from_x_mapping(self):
        self._test_mapping(0x8125, TakeYFromX)

    def test_shift_x_right_mapping(self):
        self._test_mapping(0x8126, ShiftXRight)

    def test_shift_x_left_mapping(self):
        self._test_mapping(0x812E, ShiftXLeft)

    def test_add_x_to_i_mapping(self):
        self._test_mapping(0xF81E, AddXToI)

    def test_set_x_to_delay_timer_mapping(self):
        self._test_mapping(0xF307, SetXToDelayTimer)

    def test_take_x_from_y_mapping(self):
        self._test_mapping(0x8337, TakeXFromY)

    def test_skip_if_x_y_not_equal_mapping(self):
        self._test_mapping(0x9430, SkipIfXyNotEqual)

if __name__ == '__main__':
    unittest.main()