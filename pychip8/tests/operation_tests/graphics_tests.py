from pychip8.tests.operation_tests.operation_test_case import OperationTestCase
from pychip8.opcode import Opcode
from pychip8.cpu import Cpu
from pychip8.operations import *

from numpy import uint8 as byte
from numpy import uint16

class GraphicsTests(OperationTestCase):

    def test_clear_display(self):
        opcode = Opcode(0x00E0)

        operation = ClearDisplay()
        operation.execute(opcode, self.cpu)
        
        for pixel in self.cpu.frame_buffer:
            self.assertEqual(pixel, 0)

    def test_draw_sprite(self):
        opcode = Opcode(0xD113)

        self.cpu.ram[self.cpu.index_register] = 0b1
        self.cpu.ram[self.cpu.index_register + 1] = 0b11
        self.cpu.ram[self.cpu.index_register + 2] = 0b111

        operation = DrawSprite()
        operation.execute(opcode, self.cpu)

        self.assertEqual(self.cpu.frame_buffer[opcode.x + opcode.y], 0b1)
        self.assertEqual(self.cpu.frame_buffer[opcode.x + (opcode.y + 1)], 0b11)
        self.assertEqual(self.cpu.frame_buffer[opcode.x + (opcode.y + 2)], 0b111)

    def test_draw_collision(self):
        opcode = Opcode(0xD113)

        self.cpu.ram[self.cpu.index_register] = 0b1
        self.cpu.ram[self.cpu.index_register + 1] = 0b11
        self.cpu.ram[self.cpu.index_register + 2] = 0b111

        operation = DrawSprite()
        operation.execute(opcode, self.cpu)

        self.cpu.ram[self.cpu.index_register] = 0b0
        self.cpu.ram[self.cpu.index_register + 1] = 0b00
        self.cpu.ram[self.cpu.index_register + 2] = 0b010
        operation.execute(opcode, self.cpu)

        self.assertEqual(self.cpu.general_purpose_registers[self.cpu.ARITHMETIC_FLAG_REGISTER_ADDRESS], 1)
        self.assertEqual(self.cpu.frame_buffer[opcode.x + opcode.y], 0b1)
        self.assertEqual(self.cpu.frame_buffer[opcode.x + (opcode.y + 1)], 0b11)
        self.assertEqual(self.cpu.frame_buffer[opcode.x + (opcode.y + 2)], 0b101)