import unittest   
from pychip8.tests.opcode_tests import TestOpcode

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(TestOpcode))

    runner=unittest.TextTestRunner()
    runner.run(suite)