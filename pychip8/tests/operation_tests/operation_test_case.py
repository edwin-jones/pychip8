from abc import ABC

from pychip8.opcode import Opcode
from pychip8.cpu import Cpu

import unittest

class OperationTestCase(ABC, unittest.TestCase):

    def _test_cpu_attribute_equals_value_after_execution(self, word, operation, cpu_attribute_name, value):
        opcode = Opcode(word)
        operation.execute(opcode, self.cpu)
        cpu_attribute = getattr(self.cpu, cpu_attribute_name)
        self.assertEqual(cpu_attribute, value)

    def setUp(self):
        self.cpu = Cpu(None)