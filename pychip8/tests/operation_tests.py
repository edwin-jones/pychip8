from pychip8.opcode import Opcode
from pychip8.cpu import Cpu
from pychip8.operations import * 

from numpy import uint8 as byte
from numpy import uint16

import unittest

 
class TestOperation(unittest.TestCase):

    def _test_skip(self, word, operation):
        opcode = Opcode(word)
        operation.execute(opcode, self.cpu)
        self.assertEqual(self.cpu._program_counter, Cpu.PROGRAM_START_ADDRESS)
        self.cpu.general_purpose_registers[1] = byte(1)
        operation.execute(opcode, self.cpu)
        self.assertEqual(self.cpu._program_counter,  Cpu.PROGRAM_START_ADDRESS + Cpu.WORD_SIZE_IN_BYTES)

    def _test_cpu_attribute_equals_value_after_execution(self, word, operation, cpu_attribute_name, value):
        opcode = Opcode(word)
        operation.execute(opcode, self.cpu)
        cpu_attribute = getattr(self.cpu, cpu_attribute_name)
        self.assertEqual(cpu_attribute, value)

    def _test_bitwise_operation(self, word, operation, expected_value):
        opcode = Opcode(word)
        operation.execute(opcode, self.cpu)
        self.assertEqual(self.cpu.general_purpose_registers[opcode.x], expected_value)

    def _test_arithmetic(self, word, operation, x, y, expected_result, expected_flag_value):
        opcode = Opcode(word)

        self.cpu.general_purpose_registers[opcode.x] = byte(x)
        self.cpu.general_purpose_registers[opcode.y] = byte(y)

        operation.execute(opcode, self.cpu)

        self.assertEqual(self.cpu.general_purpose_registers[opcode.x], expected_result)
        self.assertEqual(self.cpu.general_purpose_registers[Cpu.ARITHMETIC_FLAG_REGISTER_ADDRESS], expected_flag_value)

    def setUp(self):
        self.cpu = Cpu()

    def test_set_delay_timer(self):
        self._test_cpu_attribute_equals_value_after_execution(0xF615, SetDelayTimer(), 'delay_timer', 0x6)
    
    def test_set_sound_timer(self):
        self._test_cpu_attribute_equals_value_after_execution(0xF618, SetSoundTimer(), 'sound_timer', 0x6)

    def test_set_index_register(self):
        self._test_cpu_attribute_equals_value_after_execution(0xA123, SetI(), 'index_register', 0x123)

    def test_goto(self):
        self._test_cpu_attribute_equals_value_after_execution(0x1123, Goto(), '_program_counter', 0x123)

    def test_skip_if_not_equal(self):
        self._test_skip(0x3100, SkipIfNotEqual())

    def test_skip_if_equal(self):
        self._test_skip(0x4101, SkipIfEqual())

    def test_skip_if_x_y_equal(self):
        self.cpu.general_purpose_registers[2] = byte(1)
        self._test_skip(0x5120, SkipIfXyEqual())

    def test_clear_display(self):
        opcode = Opcode(0x00E0)

        self.cpu.frame_buffer = [byte(255)] * (64 * 32)

        operation = ClearDisplay()
        operation.execute(opcode, self.cpu)
        
        for pixel in self.cpu.frame_buffer:
            self.assertEqual(pixel, 0)

    def test_set_general_purpose_register(self):
        opcode = Opcode(0x61CD)
        operation = SetX()
        operation.execute(opcode, self.cpu)
        self.assertEqual(self.cpu.general_purpose_registers[1], 0xCD)

    def test_incremement_general_purpose_register(self):
        opcode = Opcode(0x71CD)
        operation = AddToX()
        self.cpu.general_purpose_registers[1] = byte(1)
        operation.execute(opcode, self.cpu)     
        self.assertEqual(self.cpu.general_purpose_registers[1], 0xCD + 1)

    def test_copy_general_purpose_register(self):
        opcode = Opcode(0x8120)
        operation = SetXToY()
        self.cpu.general_purpose_registers[opcode.y] = 4
        operation.execute(opcode, self.cpu)
        self.assertEqual(self.cpu.general_purpose_registers[opcode.x], self.cpu.general_purpose_registers[opcode.y])

    def test_or(self):
        self.cpu.general_purpose_registers[1] = byte(4)
        self.cpu.general_purpose_registers[2] = byte(2)
        self._test_bitwise_operation(0x8121, BitwiseOr(), 6)

    def test_and(self):
        self.cpu.general_purpose_registers[1] = byte(0xF)
        self.cpu.general_purpose_registers[2] = byte(0xF)
        self._test_bitwise_operation(0x8122, BitwiseAnd(), 0xF)

    def test_xor(self):
        self.cpu.general_purpose_registers[1] = byte(3)
        self.cpu.general_purpose_registers[2] = byte(2)
        self._test_bitwise_operation(0x8123, BitwiseXor(), 1)

    def test_add_y_to_x_overflow(self):
        self._test_arithmetic(0x8124, AddYToX(), 255, 2, 1, 1)

    def test_add_y_to_x_no_overflow(self):
        self._test_arithmetic(0x8124, AddYToX(), 2, 3, 5, 0)

    def test_take_y_from_x_underflow(self):
        self._test_arithmetic(0x8124, TakeYFromX(), 1, 2, 255, 1)

    def test_take_y_from_x_no_underflow(self):
        self._test_arithmetic(0x8124, TakeYFromX(), 6, 4, 2, 0)

    def test_shift_x_right(self):
        opcode = Opcode(0x8106)
        operation = ShiftXLeft()
        self.cpu.general_purpose_registers[opcode.x] = byte(0xFF)
        operation.execute(opcode, self.cpu)
        self.assertEqual(self.cpu.general_purpose_registers[Cpu.ARITHMETIC_FLAG_REGISTER_ADDRESS], byte(1))
        self.assertEqual(self.cpu.general_purpose_registers[opcode.x], byte(254))

    def test_shift_x_left(self):
        opcode = Opcode(0x810E)
        operation = ShiftXRight()
        self.cpu.general_purpose_registers[opcode.x] = byte(1)
        operation.execute(opcode, self.cpu)
        self.assertEqual(self.cpu.general_purpose_registers[Cpu.ARITHMETIC_FLAG_REGISTER_ADDRESS], byte(1))
        self.assertEqual(self.cpu.general_purpose_registers[opcode.x], byte(0))

    def test_add_x_to_i(self):
        opcode = Opcode(0xF11E)
        operation = AddXToI()
        self.cpu.index_register = byte(128)
        self.cpu.general_purpose_registers[opcode.x] = byte(129)
        operation.execute(opcode, self.cpu)
        self.assertEqual(self.cpu.index_register, 1)
        self.assertEqual(self.cpu.general_purpose_registers[Cpu.ARITHMETIC_FLAG_REGISTER_ADDRESS], byte(1))

    def test_set_x_to_delay_timer(self):
        opcode = Opcode(0xF207)
        operation = SetXToDelayTimer()
        self.cpu.delay_timer = byte(0xA)
        operation.execute(opcode, self.cpu)
        self.assertEqual(self.cpu.general_purpose_registers[opcode.x], self.cpu.delay_timer)

if __name__ == '__main__':
    unittest.main()