import unittest
from Calculator import Calculator


class TestCalculator(unittest.TestCase):
    def test_valid_plus_operation(self):
        calculator_instance = Calculator("1,2,3,4,+")
        result = calculator_instance.calculate()
        self.assertEqual(result, 10)

    def test_valid_minus_operation(self):
        calculator_instance = Calculator("10,5,-")
        result = calculator_instance.calculate()
        self.assertEqual(result, 5)

    def test_valid_multiply_operation(self):
        calculator_instance = Calculator("2,3,4,*")
        result = calculator_instance.calculate()
        self.assertEqual(result, 24)

    def test_divide_by_positive_zero(self):
        calculator_instance = Calculator("10,0,/")
        result = calculator_instance.calculate()
        self.assertEqual(result, float('inf'))

    def test_divide_by_negative_zero(self):
        calculator_instance = Calculator("-10,0,/")
        result = calculator_instance.calculate()
        self.assertEqual(result, float('-inf'))

    def test_ignore_extra_numbers(self):
        calculator_instance = Calculator("1,2,3,4,5,6,7,+")
        result = calculator_instance.calculate()
        self.assertEqual(result, 10)

    def test_throw_error_for_one_number(self):
        with self.assertRaises(ValueError):
            calculator_instance = Calculator("1,+")
            calculator_instance.calculate()

    def test_throw_error_for_zero_numbers(self):
        with self.assertRaises(ValueError):
            calculator_instance = Calculator("+")
            calculator_instance.calculate()

    def test_throw_error_for_invalid_input(self):
        with self.assertRaises(ValueError):
            calculator_instance = Calculator("1234,5,67,8,9+")
            calculator_instance.calculate()


if __name__ == '__main__':
    unittest.main()
