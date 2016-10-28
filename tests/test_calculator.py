# -*- coding: utf-8 -*-

from .context import Calculator

import unittest


class CalculatorTestSuite(unittest.TestCase):

    def test_SumWithTwoParameterTest(self):
        calculator = Calculator()
        self.assertEqual(5, calculator.sum(2, 3))


if __name__ == '__main__':
    unittest.main()