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
        self.assertTrue(isinstance(operation, operation_type))

    def test_thows_if_no_mapping(self):
        self.assertRaises(KeyError, self.operation_mapper.find_operation, 0x2FFF)

    def test_set_index_register_mapping(self):
        self._test_mapping(0xA123, SetIndexRegister)

    def test_set_general_purpose_register_mapping(self):
        self._test_mapping(0x61CD, SetGeneralPurposeRegister)

    def test_copy_general_purpose_register_mapping(self):
        self._test_mapping(0x8120, CopyGeneralPurposeRegister)

    def test_set_delay_timer_mapping(self):
        self._test_mapping(0xF615, SetDelayTimer)

    def test_set_sound_timer_mapping(self):
        self._test_mapping(0xF618, SetSoundTimer)
    
    def test_clear_display_mapping(self):
        self._test_mapping(0x00E0, ClearDisplay)
    
    def test_clear_goto(self):
        self._test_mapping(0x1000, Goto)


if __name__ == '__main__':
    unittest.main()