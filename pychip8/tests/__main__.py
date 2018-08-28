import unittest

from pychip8.tests.opcode_tests import OpcodeTests
from pychip8.tests.cpu_tests import CpuTests
from pychip8.tests.operation_mapper_tests import OperationMapperTests
from pychip8.tests.operation_tests.input_tests import InputTests
from pychip8.tests.operation_tests.arithmetic_tests import ArithmeticTests
from pychip8.tests.operation_tests.core_tests import CoreTests
from pychip8.tests.operation_tests.jump_tests import JumpTests
from pychip8.tests.operation_tests.bitwise_tests import BitwiseTests
from pychip8.tests.operation_tests.timer_tests import TimerTests
from pychip8.tests.operation_tests.font_tests import FontTests
from pychip8.tests.operation_tests.graphics_tests import GraphicsTests


if __name__ == '__main__':
    suite = unittest.TestSuite()
    
    suite.addTests(unittest.makeSuite(OperationMapperTests))
    suite.addTests(unittest.makeSuite(OpcodeTests))
    suite.addTests(unittest.makeSuite(CpuTests))
    suite.addTests(unittest.makeSuite(InputTests))
    suite.addTests(unittest.makeSuite(ArithmeticTests))
    suite.addTests(unittest.makeSuite(BitwiseTests))
    suite.addTests(unittest.makeSuite(CoreTests))
    suite.addTests(unittest.makeSuite(JumpTests))
    suite.addTests(unittest.makeSuite(TimerTests))
    suite.addTests(unittest.makeSuite(FontTests))
    suite.addTests(unittest.makeSuite(GraphicsTests))

    runner=unittest.TextTestRunner()
    runner.run(suite)