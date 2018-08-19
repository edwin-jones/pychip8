from pychip8.opcode import Opcode
from pychip8.cpu import Cpu
from pychip8.operations import * 

import unittest

 
class TestOperation(unittest.TestCase):

    def setUp(self):
        self.cpu = Cpu()

    def test_set_delay_timer(self):
        opcode = Opcode(0xF615)
        operation = SetDelayTimer()
        operation.execute(opcode, self.cpu)
        self.assertEqual(self.cpu.delay_timer, 0x6)
    
    def test_set_sound_timer(self):
        opcode = Opcode(0xF618)
        operation = SetSoundTimer()
        operation.execute(opcode, self.cpu)
        self.assertEqual(self.cpu.sound_timer, 0x6)

    def test_set_index_register(self):
        opcode = Opcode(0xA123)
        operation = SetIndexRegister()
        operation.execute(opcode, self.cpu)
        self.assertEqual(self.cpu.index_register, 0x123)

    def test_set_general_purpose_register(self):
        opcode = Opcode(0x61CD)
        operation = SetGeneralPurposeRegister()
        operation.execute(opcode, self.cpu)
        self.assertEqual(self.cpu.main_registers[1], 0xCD)

    def test_copy_general_purpose_register(self):
        opcode = Opcode(0x8120)
        operation = CopyGeneralPurposeRegister()
        self.cpu.main_registers[int(opcode.y)] = 4
        operation.execute(opcode, self.cpu)
        self.assertEqual(self.cpu.main_registers[int(opcode.x)], self.cpu.main_registers[int(opcode.y)])


if __name__ == '__main__':
    unittest.main()