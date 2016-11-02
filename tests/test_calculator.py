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
        self.assertEqual('Error, first argument is a string value.', calculator.sum('someText', 3.3))

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
        self.assertEqual(1.2100000000000002, calculator.poweroftwo(1.1))

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

    def test_factorial_with_a_string_returns_error_message(self):
        calculator = Calculator()
        self.assertEqual('Error, argument must be a integer value.', calculator.factorial('someText'))

    def test_roman_number_translation(self):
        calculator = Calculator()
        self.assertEqual(1, calculator.roman_to_latin('I'))
        self.assertEqual(2, calculator.roman_to_latin('II'))
        self.assertEqual(3, calculator.roman_to_latin('III'))
        self.assertEqual(4, calculator.roman_to_latin('IV'))
        self.assertEqual(5, calculator.roman_to_latin('V'))
        self.assertEqual(6, calculator.roman_to_latin('VI'))
        self.assertEqual(7, calculator.roman_to_latin('VII'))
        self.assertEqual(8, calculator.roman_to_latin('VIII'))
        self.assertEqual(9, calculator.roman_to_latin('IX'))
        self.assertEqual(10, calculator.roman_to_latin('X'))
        self.assertEqual(20, calculator.roman_to_latin('XX'))
        self.assertEqual(30, calculator.roman_to_latin('XXX'))
        self.assertEqual(40, calculator.roman_to_latin('XL'))
        self.assertEqual(50, calculator.roman_to_latin('L'))
        self.assertEqual(60, calculator.roman_to_latin('LX'))
        self.assertEqual(70, calculator.roman_to_latin('LXX'))
        self.assertEqual(80, calculator.roman_to_latin('LXXX'))
        self.assertEqual(90, calculator.roman_to_latin('XC'))
        self.assertEqual(100, calculator.roman_to_latin('C'))
        self.assertEqual(200, calculator.roman_to_latin('CC'))
        self.assertEqual(300, calculator.roman_to_latin('CCC'))
        self.assertEqual(330, calculator.roman_to_latin('CCCXXX'))
        self.assertEqual(400, calculator.roman_to_latin('CD'))
        self.assertEqual(440, calculator.roman_to_latin('CDXL'))
        self.assertEqual(500, calculator.roman_to_latin('D'))
        self.assertEqual(550, calculator.roman_to_latin('DL'))
        self.assertEqual(600, calculator.roman_to_latin('DC'))
        self.assertEqual(660, calculator.roman_to_latin('DCLX'))
        self.assertEqual(700, calculator.roman_to_latin('DCC'))
        self.assertEqual(770, calculator.roman_to_latin('DCCLXX'))
        self.assertEqual(800, calculator.roman_to_latin('DCCC'))
        self.assertEqual(880, calculator.roman_to_latin('DCCCLXXX'))
        self.assertEqual(900, calculator.roman_to_latin('CM'))
        self.assertEqual(990, calculator.roman_to_latin('CMXC'))
        self.assertEqual(1000, calculator.roman_to_latin('M'))
        self.assertEqual(1911, calculator.roman_to_latin('MCMXI'))
        self.assertEqual(1920, calculator.roman_to_latin('MCMXX'))
        self.assertEqual(1922, calculator.roman_to_latin('MCMXXII'))
        self.assertEqual(1930, calculator.roman_to_latin('MCMXXX'))
        self.assertEqual(1933, calculator.roman_to_latin('MCMXXXIII'))
        self.assertEqual(1940, calculator.roman_to_latin('MCMXL'))
        self.assertEqual(1944, calculator.roman_to_latin('MCMXLIV'))
        self.assertEqual(1950, calculator.roman_to_latin('MCML'))
        self.assertEqual(1955, calculator.roman_to_latin('MCMLV'))
        self.assertEqual(1960, calculator.roman_to_latin('MCMLX'))
        self.assertEqual(1966, calculator.roman_to_latin('MCMLXVI'))
        self.assertEqual(1970, calculator.roman_to_latin('MCMLXX'))
        self.assertEqual(1977, calculator.roman_to_latin('MCMLXXVII'))
        self.assertEqual(1980, calculator.roman_to_latin('MCMLXXX'))
        self.assertEqual(1988, calculator.roman_to_latin('MCMLXXXVIII'))
        self.assertEqual(1990, calculator.roman_to_latin('MCMXC'))
        self.assertEqual(1999, calculator.roman_to_latin('MCMXCIX'))
        self.assertEqual(2000, calculator.roman_to_latin('MM'))
        self.assertEqual(2015, calculator.roman_to_latin('MMXV'))
        self.assertEqual(2000, calculator.roman_to_latin('MM'))
        self.assertEqual(3000, calculator.roman_to_latin('MMM'))
        self.assertEqual(3999, calculator.roman_to_latin('MMMCMXCIX'))


if __name__ == '__main__':
    unittest.main()