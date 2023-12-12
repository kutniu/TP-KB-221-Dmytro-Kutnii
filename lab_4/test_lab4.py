import unittest
from lab4 import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_is_number(self):
        self.assertTrue(self.calc.is_number('123'))
        self.assertFalse(self.calc.is_number('12a'))

    def test_get_prior(self):
        self.assertEqual(self.calc.get_prior('+'), 0)
        self.assertEqual(self.calc.get_prior('*'), 1)
        self.assertEqual(self.calc.get_prior('^'), 2)

    def test_to_rev(self):
        self.assertEqual(self.calc.to_rev('3+4*2/(1-5)^2'), ['3', '4', '2', '*', '1', '5', '-', '2', '^', '/', '+'])

    def test_calculate(self):
        self.assertEqual(self.calc.calculate(['3', '4', '2', '*', '1', '5', '-', '2', '^', '/', '+']), 3.5)

if __name__ == '__main__':
    unittest.main