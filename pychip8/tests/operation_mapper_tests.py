from pychip8.opcode import Opcode
from pychip8.operations.operation_mapper import OperationMapper
from pychip8.operations.set_register import SetRegister

import unittest

 
class TestOperationMapper(unittest.TestCase):

    def setUp(self):
        self.opcode = Opcode(0xABCD)

    def test_operation_mapper_thows(self):
        opcode = Opcode(0xFFFF)
        mapper = OperationMapper()

        self.assertRaises(KeyError, mapper.find_operation, opcode)

    def test_operation_mapper_set_register(self):
        opcode = Opcode(0x61CD)
        mapper = OperationMapper()
        operation = mapper.find_operation(opcode)

        self.assertTrue(isinstance(operation, SetRegister))


if __name__ == '__main__':
    unittest.main()