from pychip8.tests.operation_tests.operation_test_case import OperationTestCase
from pychip8.opcode import Opcode
from pychip8.cpu import Cpu
from pychip8.operations import *

from numpy import uint8 as byte
from numpy import uint16

class InputTests(OperationTestCase):

    def test_skip_if_key_down(self):
        opcode = Opcode(0xEF9E)
        operation = SkipIfKeyPressed()

        operation.execute(opcode, self.cpu)

        self.assertEqual(self.cpu.program_counter, self.cpu.PROGRAM_START_ADDRESS)

        self.cpu.key_down(0xF)
        operation.execute(opcode, self.cpu)

        self.assertEqual(self.cpu.program_counter, self.cpu.PROGRAM_START_ADDRESS + self.cpu.WORD_SIZE_IN_BYTES)

    def test_skip_if_key_not_down(self):
        opcode = Opcode(0xEFA1)
        operation = SkipIfKeyNotPressed()

        self.cpu.key_down(0xF)
        operation.execute(opcode, self.cpu)
        self.assertEqual(self.cpu.program_counter, self.cpu.PROGRAM_START_ADDRESS)

        self.cpu.key_up(0xF)
        operation.execute(opcode, self.cpu)
        self.assertEqual(self.cpu.program_counter, self.cpu.PROGRAM_START_ADDRESS + self.cpu.WORD_SIZE_IN_BYTES)