import unittest   
from pychip8.tests.opcode_tests import TestOpcode
from pychip8.tests.operation_tests import TestOperation

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(TestOpcode))
    suite.addTests(unittest.makeSuite(TestOperation))

    runner=unittest.TextTestRunner()
    runner.run(suite)