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

    def test_wait_for_key_press(self):
        opcode = Opcode(0xF10A)
        operation = WaitForKeyPress()

        program_address = self.cpu.program_counter

        operation.execute(opcode, self.cpu)
        self.cpu.move_to_next_instruction()

        self.assertEqual(self.cpu.general_purpose_registers[opcode.x], 0x0)
        self.assertEqual(self.cpu.program_counter, program_address)

        self.cpu.key_down(0xF)
        operation.execute(opcode, self.cpu)
        self.cpu.move_to_next_instruction()

        self.assertEqual(self.cpu.general_purpose_registers[opcode.x], 0xF)
        self.assertGreater(self.cpu.program_counter, program_address)
        self.assertEqual(self.cpu.program_counter - program_address, self.cpu.WORD_SIZE_IN_BYTES)
