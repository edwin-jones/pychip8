from pychip8.tests.operation_tests.operation_test_case import OperationTestCase
from pychip8.opcode import Opcode
from pychip8.cpu import Cpu
from pychip8.operations import *

from numpy import uint8 as byte
from numpy import uint16

class GraphicsTests(OperationTestCase):

    def _test_buffer_pixels_match_pattern(self, x, y, pattern):
        for i in range(8):
            mask = 128 >> i
            bit = bool(pattern & mask)
            self.assertEqual(self.cpu.frame_buffer[x + i][y], bit)

    def test_clear_display(self):
        opcode = Opcode(0x00E0)

        operation = ClearDisplay()
        operation.execute(opcode, self.cpu)
        
        for x in range(64):
            for y in range(32):
                self.assertEqual(self.cpu.frame_buffer[x][y], False)

    def test_draw_sprite(self):
        opcode = Opcode(0xD113)

        self.cpu.ram[self.cpu.index_register] = 0b1
        self.cpu.ram[self.cpu.index_register + 1] = 0b11
        self.cpu.ram[self.cpu.index_register + 2] = 0b111

        operation = DrawSprite()
        operation.execute(opcode, self.cpu)

        self._test_buffer_pixels_match_pattern(opcode.x, opcode.y, 0b1)
        self._test_buffer_pixels_match_pattern(opcode.x, opcode.y+1, 0b11)
        self._test_buffer_pixels_match_pattern(opcode.x, opcode.y+2, 0b111)
        self._test_buffer_pixels_match_pattern(opcode.x, opcode.y+3, 0b0)

    def test_draw_collision(self):
        opcode = Opcode(0xD113)
        self.cpu.ram[self.cpu.index_register] = 0b1111

        operation = DrawSprite()
        operation.execute(opcode, self.cpu)

        self.assertEqual(self.cpu.general_purpose_registers[self.cpu.ARITHMETIC_FLAG_REGISTER_ADDRESS], 0)

        self.cpu.ram[self.cpu.index_register] = 0b0110
        operation.execute(opcode, self.cpu)

        self._test_buffer_pixels_match_pattern(opcode.x, opcode.y, 0b1001)
        self.assertEqual(self.cpu.general_purpose_registers[self.cpu.ARITHMETIC_FLAG_REGISTER_ADDRESS], 1)