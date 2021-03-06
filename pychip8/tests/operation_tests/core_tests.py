from pychip8.opcode import Opcode
from pychip8.tests.operation_tests.operation_test_case import OperationTestCase
from pychip8.cpu import Cpu
from pychip8.operations import *


class CoreTests(OperationTestCase):

    def test_set_index_register(self):
        self._test_cpu_attribute_equals_value_after_execution(0xA123, SetI(), 'index_register', 0x123)

    def test_set_general_purpose_register(self):
        opcode = Opcode(0x61CD)
        operation = SetX()
        operation.execute(opcode, self.cpu)
        self.assertEqual(self.cpu.general_purpose_registers[1], 0xCD)

    def test_incremement_general_purpose_register(self):
        opcode = Opcode(0x71CD)
        operation = AddToX()
        self.cpu.general_purpose_registers[1] = 1
        operation.execute(opcode, self.cpu)     
        self.assertEqual(self.cpu.general_purpose_registers[1], 0xCD + 1)

    def test_copy_general_purpose_register(self):
        opcode = Opcode(0x8120)
        operation = SetXToY()
        self.cpu.general_purpose_registers[opcode.y] = 4
        operation.execute(opcode, self.cpu)
        self.assertEqual(self.cpu.general_purpose_registers[opcode.x], self.cpu.general_purpose_registers[opcode.y])

    def test_add_x_to_i(self):
        opcode = Opcode(0xF11E)
        operation = AddXToI()
        self.cpu.index_register = 0xFFFF
        self.cpu.general_purpose_registers[opcode.x] = 2
        operation.execute(opcode, self.cpu)
        self.assertEqual(self.cpu.index_register, 1)
        self.assertEqual(self.cpu.general_purpose_registers[Cpu.ARITHMETIC_FLAG_REGISTER_ADDRESS], 1)

    def test_random(self):
        opcode = Opcode(0xC10F)

        operation = Random()
        operation.execute(opcode, self.cpu)

        value = self.cpu.general_purpose_registers[opcode.x]

        self.assertGreaterEqual(value, 0)
        self.assertLessEqual(value, 0xF)

        operation.execute(opcode, self.cpu)

    def test_save_registers_zero_to_x(self):
        opcode = Opcode(0xF255)
        operation = SaveRegistersZeroToX()

        self.cpu.general_purpose_registers[0] = 1
        self.cpu.general_purpose_registers[1] = 2
        self.cpu.general_purpose_registers[2] = 3

        operation.execute(opcode, self.cpu)

        self.assertEqual(self.cpu.ram[self.cpu.index_register], 1)
        self.assertEqual(self.cpu.ram[self.cpu.index_register + 1], 2)
        self.assertEqual(self.cpu.ram[self.cpu.index_register + 2], 3)

    def test_load_registers_zero_to_x(self):
        opcode = Opcode(0xF265)
        operation = LoadRegistersZeroToX()

        self.cpu.ram[self.cpu.index_register] = 1
        self.cpu.ram[self.cpu.index_register + 1] = 2
        self.cpu.ram[self.cpu.index_register + 2] = 3

        operation.execute(opcode, self.cpu)

        self.assertEqual(self.cpu.general_purpose_registers[0], 1)
        self.assertEqual(self.cpu.general_purpose_registers[1], 2)
        self.assertEqual(self.cpu.general_purpose_registers[2], 3)

    def test_save_x_as_bcd(self):
        opcode = Opcode(0xF133)

        self.cpu.general_purpose_registers[opcode.x] = 123

        operation = SaveXAsBcd()

        operation.execute(opcode, self.cpu)

        self.assertEqual(self.cpu.ram[self.cpu.index_register], 1)
        self.assertEqual(self.cpu.ram[self.cpu.index_register + 1], 2)
        self.assertEqual(self.cpu.ram[self.cpu.index_register + 2], 3)
