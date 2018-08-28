from pychip8.tests.operation_tests.operation_test_case import OperationTestCase
from pychip8.opcode import Opcode
from pychip8.cpu import Cpu
from pychip8.operations import *

from numpy import uint8 as byte
from numpy import uint16

class GraphicsTests(OperationTestCase):

    def test_clear_display(self):
        opcode = Opcode(0x00E0)

        self.cpu.frame_buffer = [byte(255)] * (64 * 32)

        operation = ClearDisplay()
        operation.execute(opcode, self.cpu)
        
        for pixel in self.cpu.frame_buffer:
            self.assertEqual(pixel, 0)

    def test_draw_sprite(self):
        opcode = Opcode(0xD111)

        operation = DrawSprite()
        operation.execute(opcode, self.cpu)