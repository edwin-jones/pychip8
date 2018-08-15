from pychip8.opcode import Opcode

import unittest
 
class TestOpcode(unittest.TestCase):

    def setUp(self):
        self.opcode = Opcode(0xABCD)

    def test_n(self):       
        self.assertEqual(self.opcode.n, 0xD)

    def test_nn(self):       
        self.assertEqual(self.opcode.nn, 0xCD)
    
    def test_nnn(self):       
        self.assertEqual(self.opcode.nnn, 0xBCD)

    def test_a(self):       
        self.assertEqual(self.opcode.a, 0xA)
    
    def test_x(self):       
        self.assertEqual(self.opcode.x, 0xB)

    def test_y(self):       
        self.assertEqual(self.opcode.y, 0xC)

if __name__ == '__main__':
    unittest.main()