from pychip8.opcode import Opcode
from pychip8.cpu import Cpu
from pychip8.operations.set_register import SetRegister

import unittest

 
class TestOperation(unittest.TestCase):

    def setUp(self):
        self.opcode = Opcode(0xABCD)

    def test_set_register(self):

        opcode = Opcode(0x61CD)
        cpu = Cpu()
        operation = SetRegister()
        operation.execute(opcode, cpu)

        self.assertEqual(cpu.main_registers[1], 0xCD)


if __name__ == '__main__':
    unittest.main()