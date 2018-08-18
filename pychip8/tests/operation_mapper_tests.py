from pychip8.opcode import Opcode
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
        self.assertTrue(isinstance(operation, SetRegister))

    def test_operation_mapper_copy_register(self):
        mapper = OperationMapper()
        operation = mapper.find_operation(0x8120)
        self.assertTrue(isinstance(operation, CopyRegister))


if __name__ == '__main__':
    unittest.main()