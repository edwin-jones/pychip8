from pychip8.opcode import Opcode
from pychip8.tests.operation_tests.operation_test_case import OperationTestCase
from pychip8.cpu import Cpu
from pychip8.operations import *

from numpy import uint8 as byte


class TimerTests(OperationTestCase):

    def test_set_delay_timer(self):
        self.cpu.general_purpose_registers[6] = 0x8
        self._test_cpu_attribute_equals_value_after_execution(0xF615, SetDelayTimer(), 'delay_timer', 0x8)

    def test_set_sound_timer(self):
        self.cpu.general_purpose_registers[6] = 0x7
        self._test_cpu_attribute_equals_value_after_execution(0xF618, SetSoundTimer(), 'sound_timer', 0x7)

    def test_set_x_to_delay_timer(self):
        opcode = Opcode(0xF207)
        operation = SetXToDelayTimer()
        self.cpu.delay_timer = byte(0xA)
        operation.execute(opcode, self.cpu)
        self.assertEqual(self.cpu.general_purpose_registers[opcode.x], self.cpu.delay_timer)

