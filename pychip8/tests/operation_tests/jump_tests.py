from pychip8.tests.operation_tests.operation_test_case import OperationTestCase
from pychip8.opcode import Opcode
from pychip8.cpu import Cpu
from pychip8.operations import *

from numpy import uint8 as byte
from numpy import uint16

class JumpTests(OperationTestCase):

    def _test_skip(self, word, operation):
        opcode = Opcode(word)
        operation.execute(opcode, self.cpu)
        self.assertEqual(self.cpu._program_counter, Cpu.PROGRAM_START_ADDRESS)
        self.cpu.general_purpose_registers[1] = byte(1)
        operation.execute(opcode, self.cpu)
        self.assertEqual(self.cpu._program_counter,  Cpu.PROGRAM_START_ADDRESS + Cpu.WORD_SIZE_IN_BYTES)

    def test_goto(self):
        self._test_cpu_attribute_equals_value_after_execution(0x1123, Goto(), '_program_counter', 0x123)

    def test_goto_plus(self):
        self.cpu.general_purpose_registers[0] = byte(4)
        self._test_cpu_attribute_equals_value_after_execution(0xB123, GotoPlus(), '_program_counter', 295)

    def test_skip_if_not_equal(self):
        self._test_skip(0x3100, SkipIfNotEqual())

    def test_skip_if_equal(self):
        self._test_skip(0x4101, SkipIfEqual())

    def test_skip_if_x_y_equal(self):
        self.cpu.general_purpose_registers[2] = byte(1)
        self._test_skip(0x5120, SkipIfXyEqual())

    def test_skip_if_x_y_not_equal(self):
        self._test_skip(0x9120, SkipIfXyNotEqual())