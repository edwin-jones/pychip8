from abc import ABC

from pychip8.opcode import Opcode
from pychip8.cpu import Cpu

from numpy import uint8 as byte
from numpy import uint16

import unittest

class OperationTestCase(ABC, unittest.TestCase):

    def _test_skip(self, word, operation):
        opcode = Opcode(word)
        operation.execute(opcode, self.cpu)
        self.assertEqual(self.cpu._program_counter, Cpu.PROGRAM_START_ADDRESS)
        self.cpu.general_purpose_registers[1] = byte(1)
        operation.execute(opcode, self.cpu)
        self.assertEqual(self.cpu._program_counter,  Cpu.PROGRAM_START_ADDRESS + Cpu.WORD_SIZE_IN_BYTES)

    def _test_cpu_attribute_equals_value_after_execution(self, word, operation, cpu_attribute_name, value):
        opcode = Opcode(word)
        operation.execute(opcode, self.cpu)
        cpu_attribute = getattr(self.cpu, cpu_attribute_name)
        self.assertEqual(cpu_attribute, value)

    def _test_bitwise_operation(self, word, operation, expected_value):
        opcode = Opcode(word)
        operation.execute(opcode, self.cpu)
        self.assertEqual(self.cpu.general_purpose_registers[opcode.x], expected_value)

    def _test_arithmetic(self, word, operation, x, y, expected_result, expected_flag_value):
        opcode = Opcode(word)

        self.cpu.general_purpose_registers[opcode.x] = byte(x)
        self.cpu.general_purpose_registers[opcode.y] = byte(y)

        operation.execute(opcode, self.cpu)

        self.assertEqual(self.cpu.general_purpose_registers[opcode.x], expected_result)
        self.assertEqual(self.cpu.general_purpose_registers[Cpu.ARITHMETIC_FLAG_REGISTER_ADDRESS], expected_flag_value)

    def setUp(self):
        self.cpu = Cpu(None)