from pychip8.tests.operation_tests.operation_test_case import OperationTestCase
from pychip8.opcode import Opcode
from pychip8.cpu import Cpu
from pychip8.operations import *

from numpy import uint8 as byte
from numpy import uint16

class ArithmeticTests(OperationTestCase):

    def test_add_y_to_x_overflow(self):
        self._test_arithmetic(0x8124, AddYToX(), 255, 2, 1, 1)

    def test_add_y_to_x_no_overflow(self):
        self._test_arithmetic(0x8124, AddYToX(), 2, 3, 5, 0)

    def test_take_y_from_x_underflow(self):
        self._test_arithmetic(0x8124, TakeYFromX(), 1, 2, 255, 1)

    def test_take_y_from_x_no_underflow(self):
        self._test_arithmetic(0x8124, TakeYFromX(), 6, 4, 2, 0)

    def test_take_x_from_y_underflow(self):
        self._test_arithmetic(0x8127, TakeXFromY(), 5, 10, 5, 0)

    def test_take_x_from_y_no_underflow(self):
        self._test_arithmetic(0x8127, TakeXFromY(), 3, 1, 254, 1)