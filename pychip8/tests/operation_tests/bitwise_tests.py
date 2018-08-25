from pychip8.tests.operation_tests.operation_test_case import OperationTestCase
from pychip8.opcode import Opcode
from pychip8.cpu import Cpu
from pychip8.operations import *

from numpy import uint8 as byte
from numpy import uint16

class BitwiseTests(OperationTestCase):

    def _test_bitwise_operation(self, word, operation, expected_value):
        opcode = Opcode(word)
        operation.execute(opcode, self.cpu)
        self.assertEqual(self.cpu.general_purpose_registers[opcode.x], expected_value)


    def test_or(self):
        self.cpu.general_purpose_registers[1] = byte(4)
        self.cpu.general_purpose_registers[2] = byte(2)
        self._test_bitwise_operation(0x8121, BitwiseOr(), 6)

    def test_and(self):
        self.cpu.general_purpose_registers[1] = byte(0xF)
        self.cpu.general_purpose_registers[2] = byte(0xF)
        self._test_bitwise_operation(0x8122, BitwiseAnd(), 0xF)

    def test_xor(self):
        self.cpu.general_purpose_registers[1] = byte(3)
        self.cpu.general_purpose_registers[2] = byte(2)
        self._test_bitwise_operation(0x8123, BitwiseXor(), 1)

    def test_shift_x_right(self):
        opcode = Opcode(0x8106)
        operation = ShiftXLeft()
        self.cpu.general_purpose_registers[opcode.x] = byte(0xFF)
        operation.execute(opcode, self.cpu)
        self.assertEqual(self.cpu.general_purpose_registers[Cpu.ARITHMETIC_FLAG_REGISTER_ADDRESS], byte(1))
        self.assertEqual(self.cpu.general_purpose_registers[opcode.x], byte(254))

    def test_shift_x_left(self):
        opcode = Opcode(0x810E)
        operation = ShiftXRight()
        self.cpu.general_purpose_registers[opcode.x] = byte(1)
        operation.execute(opcode, self.cpu)
        self.assertEqual(self.cpu.general_purpose_registers[Cpu.ARITHMETIC_FLAG_REGISTER_ADDRESS], byte(1))
        self.assertEqual(self.cpu.general_purpose_registers[opcode.x], byte(0))