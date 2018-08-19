from pychip8.opcode import Opcode
from pychip8.operation_mapper import OperationMapper
from pychip8.operations import *

import unittest

 
class TestOperationMapper(unittest.TestCase):

    def setUp(self):
        self.opcode = Opcode(0xABCD)

    def test_operation_mapper_thows(self):
        mapper = OperationMapper()
        self.assertRaises(KeyError, mapper.find_operation, 0x2FFF)

    def test_operation_mapper_set_index_register(self):
        mapper = OperationMapper()
        operation = mapper.find_operation(0xA123)
        self.assertTrue(isinstance(operation, SetIndexRegister))

    def test_operation_mapper_set_register(self):
        mapper = OperationMapper()
        operation = mapper.find_operation(0x61CD)
        self.assertTrue(isinstance(operation, SetGeneralPurposeRegister))

    def test_operation_mapper_copy_register(self):
        mapper = OperationMapper()
        operation = mapper.find_operation(0x8120)
        self.assertTrue(isinstance(operation, CopyGeneralPurposeRegister))

    def test_operation_mapper_set_delay_timer(self):
        mapper = OperationMapper()
        operation = mapper.find_operation(0xF615)
        self.assertTrue(isinstance(operation, SetDelayTimer))

    def test_operation_mapper_set_sound_timer(self):
        mapper = OperationMapper()
        operation = mapper.find_operation(0xF618)
        self.assertTrue(isinstance(operation, SetSoundTimer))


if __name__ == '__main__':
    unittest.main()