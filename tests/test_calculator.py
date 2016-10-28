# -*- coding: utf-8 -*-

from .context import Calculator

import unittest


class CalculatorTestSuite(unittest.TestCase):

    def test_sum_of_two_integers(self):
        calculator = Calculator()
        self.assertEqual(5, calculator.sum(2, 3))

    def test_sum_of_two_floats(self):
        calculator = Calculator()
        self.assertEqual(5.4, calculator.sum(2.1, 3.3))

    def test_sum_first_argument_is_string_returns_error_message(self):
        calculator = Calculator()
        self.assertEqual("unsupported operand type(s) for +: 'float' and 'str'", calculator.sum('someText', 3.3))

    def test_sum_second_argument_is_string_returns_error_message(self):
        calculator = Calculator()
        self.assertEqual('Error, second argument is a string value.', calculator.sum(3.3, 'someText'))

    def test_multiplication_of_two_integers(self):
        calculator = Calculator()
        self.assertEqual(6, calculator.multiplication(2, 3))

    def test_multiplication_of_two_floats(self):
        calculator = Calculator()
        self.assertEqual(6.93, calculator.multiplication(2.1, 3.3))

    def test_multiplication_with_only_one_argument_returns_square(self):
        calculator = Calculator()
        self.assertEqual(4, calculator.multiplication(2))

    def test_multiplication_first_argument_is_string_returns_error_message(self):
        calculator = Calculator()
        self.assertEqual('Error, first argument is a string value.', calculator.multiplication('someText', 3.3))

    def test_multiplication_second_argument_is_string_returns_error_message(self):
        calculator = Calculator()
        self.assertEqual('Error, second argument is a string value.', calculator.multiplication(3.3, 'someText'))

    def test_power_of_two_with_an_integer(self):
        calculator = Calculator()
        self.assertEqual(36, calculator.poweroftwo(6)) 

    def test_power_of_two_with_a_float(self):
        calculator = Calculator()
        self.assertEqual(2.1435469250725863, calculator.poweroftwo(1.1))

    def test_power_of_two_with_string_returns_error_message(self):
        calculator = Calculator()
        self.assertEqual('Error, the argument is a string value.', calculator.poweroftwo('someText'))

    def test_division_of_two_integers(self):
        calculator = Calculator()
        self.assertEqual(6, calculator.division(12, 2))

    def test_division_of_two_floats(self):
        calculator = Calculator()
        self.assertEqual(2.2, calculator.division(5.5, 2.5))

    def test_division_by_zero_returns_error_message(self):
        calculator = Calculator()
        self.assertEqual('Error, the second argument can not be 0.', calculator.division(5.5, 0))

    def test_division_first_argument_is_string_returns_error_message(self):
        calculator = Calculator()
        self.assertEqual('Error, first argument is a string value.', calculator.division('someText', 3.3))

    def test_division_second_argument_is_string_returns_error_message(self):
        calculator = Calculator()
        self.assertEqual('Error, second argument is a string value.', calculator.division(3.3, 'someText'))

    def test_factorial_with_an_integer(self):
        calculator = Calculator()
        self.assertEqual(720, calculator.factorial(6))
        self.assertEqual(5040, calculator.factorial(7))
        self.assertEqual(479001600, calculator.factorial(12))
        self.assertEqual(355687428096000, calculator.factorial(17))

    def test_factorial_with_a_float_returns_error_message(self):
        calculator = Calculator()
        self.assertEqual('Error, argument must be a integer value.', calculator.factorial(6.1))

    # add the test for checking for string valuex


if __name__ == '__main__':
    unittest.main()