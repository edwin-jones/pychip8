import unittest   
from pychip8.tests.opcode_tests import TestOpcode
from pychip8.tests.operation_tests.arithmetic_tests import ArithmeticTests
from pychip8.tests.operation_tests.core_tests import CoreTests
from pychip8.tests.operation_tests.jump_tests import JumpTests
from pychip8.tests.operation_tests.bitwise_tests import BitwiseTests
from pychip8.tests.operation_mapper_tests import TestOperationMapper

if __name__ == '__main__':
    suite = unittest.TestSuite()
    
    suite.addTests(unittest.makeSuite(TestOpcode))
    suite.addTests(unittest.makeSuite(ArithmeticTests))
    suite.addTests(unittest.makeSuite(BitwiseTests))
    suite.addTests(unittest.makeSuite(CoreTests))
    suite.addTests(unittest.makeSuite(JumpTests))
    suite.addTests(unittest.makeSuite(TestOperationMapper))

    runner=unittest.TextTestRunner()
    runner.run(suite)