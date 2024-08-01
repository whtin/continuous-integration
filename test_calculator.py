"""
Unit tests for the calculator library
"""
import unittest
import calculator


class TestCalculator1:

    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_subtraction(self):
        assert 2 == calculator.subtract(4, 2)

    def test_multiplication(self):
       assert 100 == calculator.multiply(10, 10)


class TestCalculator2(unittest.TestCase):

    def test_addition(self):
        result = calculator.add(3, 4)
        self.assertEqual(result, 7)
