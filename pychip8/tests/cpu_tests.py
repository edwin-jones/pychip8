from pychip8.cpu import Cpu

import unittest
 
class CpuTests(unittest.TestCase):

    def setUp(self):
        self.cpu = Cpu(None)

    def test_key_down(self):
        self.cpu.key_down(0xF)
        self.assertTrue(0xF in self.cpu.keys)

    def test_key_up(self):
        self.cpu.key_down(0xF)
        self.cpu.key_up(0xF)
        self.assertTrue(0xF not in self.cpu.keys)