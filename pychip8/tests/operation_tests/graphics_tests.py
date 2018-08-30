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

        self.assertEqual(self.cpu.frame_buffer[opcode.x][opcode.y], False)
        self.assertEqual(self.cpu.frame_buffer[opcode.x + 6][opcode.y], False)
        self.assertEqual(self.cpu.frame_buffer[opcode.x + 7][opcode.y], True)

        self.assertEqual(self.cpu.frame_buffer[opcode.x][opcode.y], 0)
        self.assertEqual(self.cpu.frame_buffer[opcode.x + 5][opcode.y + 1], False)
        self.assertEqual(self.cpu.frame_buffer[opcode.x + 6][opcode.y + 1], True)
        self.assertEqual(self.cpu.frame_buffer[opcode.x + 7][opcode.y + 1], True)

        self.assertEqual(self.cpu.frame_buffer[opcode.x][opcode.y], False)
        self.assertEqual(self.cpu.frame_buffer[opcode.x + 5][opcode.y + 2], True)
        self.assertEqual(self.cpu.frame_buffer[opcode.x + 6][opcode.y + 2], True)
        self.assertEqual(self.cpu.frame_buffer[opcode.x + 7][opcode.y + 2], True)

    def test_draw_collision(self):
        opcode = Opcode(0xD113)

        self.cpu.ram[self.cpu.index_register] = 0b1
        self.cpu.ram[self.cpu.index_register + 1] = 0b11
        self.cpu.ram[self.cpu.index_register + 2] = 0b111

        operation = DrawSprite()
        operation.execute(opcode, self.cpu)

        self.assertEqual(self.cpu.general_purpose_registers[self.cpu.ARITHMETIC_FLAG_REGISTER_ADDRESS], 0)

        self.cpu.ram[self.cpu.index_register] = 0b0
        self.cpu.ram[self.cpu.index_register + 1] = 0b00
        self.cpu.ram[self.cpu.index_register + 2] = 0b010

        operation.execute(opcode, self.cpu)


        self.assertEqual(self.cpu.frame_buffer[opcode.x + 7][opcode.y], True)

        self.assertEqual(self.cpu.frame_buffer[opcode.x + 6][opcode.y + 1], True)
        self.assertEqual(self.cpu.frame_buffer[opcode.x + 7][opcode.y + 1], True)

        self.assertEqual(self.cpu.frame_buffer[opcode.x + 6][opcode.y + 2], False)

        self.assertEqual(self.cpu.general_purpose_registers[self.cpu.ARITHMETIC_FLAG_REGISTER_ADDRESS], 1)