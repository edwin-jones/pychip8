from pychip8.opcode import Opcode
from pychip8.tests.operation_tests.operation_test_case import OperationTestCase
from pychip8.cpu import Cpu
from pychip8.operations import LoadCharacterAddress

from numpy import uint8 as byte

import pychip8.font as Font
 
class FontTests(OperationTestCase):
    
    def test_load_character_addresses(self):
        operation = LoadCharacterAddress()
        for number in range(16):
            opcode = Opcode(0xF029)
            self.cpu.general_purpose_registers[opcode.x] = number
            operation.execute(opcode, self.cpu)
            self.assertEqual(self.cpu.index_register, number * Font.CHAR_SIZE_IN_BYTES)

