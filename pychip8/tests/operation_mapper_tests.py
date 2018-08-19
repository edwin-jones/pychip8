from pychip8.opcode import Opcode
from pychip8.operation_mapper import OperationMapper
from pychip8.operations import *

import unittest

 
class TestOperationMapper(unittest.TestCase):

    def setUp(self):
        self.opcode = Opcode(0xABCD)
        self.operation_mapper = OperationMapper()

    def _test_execution(self, word, operation_type):
        operation = self.operation_mapper.find_operation(word)
        self.assertTrue(isinstance(operation, operation_type))

    def test_operation_mapper_thows(self):
        self.assertRaises(KeyError, self.operation_mapper.find_operation, 0x2FFF)

    def test_operation_mapper_set_index_register(self):
        self._test_execution(0xA123, SetIndexRegister)

    def test_operation_mapper_set_register(self):
        self._test_execution(0x61CD, SetGeneralPurposeRegister)

    def test_operation_mapper_copy_register(self):
        self._test_execution(0x8120, CopyGeneralPurposeRegister)

    def test_operation_mapper_set_delay_timer(self):
        self._test_execution(0xF615, SetDelayTimer)

    def test_operation_mapper_set_sound_timer(self):
        self._test_execution(0xF618, SetSoundTimer)


if __name__ == '__main__':
    unittest.main()