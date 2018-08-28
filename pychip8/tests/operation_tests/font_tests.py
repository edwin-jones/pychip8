from pychip8.opcode import Opcode
from pychip8.tests.operation_tests.operation_test_case import OperationTestCase
from pychip8.cpu import Cpu
from pychip8.operations import *

from numpy import uint8 as byte
import pychip8.font as Font
 
class FontTests(OperationTestCase):
    
    def setUp(self):
        super().setUp()
        self.operation = LoadCharacterAddress()

    def _test_load_character_address(self, word):
        opcode = Opcode(word)
        self.operation.execute(opcode, self.cpu)

    def test_load_character_address_a(self):
        self._test_load_character_address(0xFA29)
        self.assertEqual(self.cpu.index_register, 0xA * Font.CHAR_SIZE_IN_BYTES)


