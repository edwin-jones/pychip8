from pychip8.tests.operation_tests.operation_test_case import OperationTestCase
from pychip8.opcode import Opcode
from pychip8.cpu import Cpu
from pychip8.operations import *


class JumpTests(OperationTestCase):

    def _test_skip(self, word, operation):
        opcode = Opcode(word)
        operation.execute(opcode, self.cpu)
        self.assertEqual(self.cpu.program_counter, Cpu.PROGRAM_START_ADDRESS)
        self.cpu.general_purpose_registers[1] = 1
        operation.execute(opcode, self.cpu)
        self.assertEqual(self.cpu.program_counter,  Cpu.PROGRAM_START_ADDRESS + Cpu.WORD_SIZE_IN_BYTES)

    def test_goto(self):
        self._test_cpu_attribute_equals_value_after_execution(0x1123, Goto(), 'program_counter', 0x123)

    def test_goto_plus(self):
        self.cpu.general_purpose_registers[0] = 4
        self._test_cpu_attribute_equals_value_after_execution(0xB123, GotoPlus(), 'program_counter', 295)

    def test_skip_if_not_equal(self):
        self._test_skip(0x3100, SkipIfNotEqual())

    def test_skip_if_equal(self):
        self._test_skip(0x4101, SkipIfEqual())

    def test_skip_if_x_y_equal(self):
        self.cpu.general_purpose_registers[2] = 1
        self._test_skip(0x5120, SkipIfXyEqual())

    def test_skip_if_x_y_not_equal(self):
        self._test_skip(0x9120, SkipIfXyNotEqual())

    def test_call_function(self):

        opcode = Opcode(0x2ABC)

        operation = CallFunction()
        operation.execute(opcode, self.cpu)
        
        self.assertEqual(self.cpu.program_counter, 0xABC)
        self.assertEqual(len(self.cpu.stack), 1)
        self.assertEqual(self.cpu.stack[0], 512)

    def test_return_from_function(self):
        self.cpu.stack.append(513)

        operation = ReturnFromFunction()
        operation.execute(None, self.cpu)

        self.assertEqual(self.cpu.program_counter, 513)
        self.assertEqual(len(self.cpu.stack), 0)
