from app.app import Calculator

import unittest

class TestCalculator(unittest.TestCase):
    """
    Test the sumInt function
    """
    def test_sumInt(self):
        self.assertEqual(Calculator.sumInt(1, 1), 2)
        self.assertEqual(Calculator.sumInt(1, 2), 3)
        self.assertEqual(Calculator.sumInt(1, -1), 0)

    """
    Test the sumFloat function
    """
    def test_sumFloat(self):
        self.assertEqual(Calculator.sumFloat(1.0, 1.0), 2.0)
        self.assertEqual(Calculator.sumFloat(1.0, 2.0), 3.0)
        self.assertEqual(Calculator.sumFloat(1.0, -1.0), 0.0)

    """
    Test the sum function
    """
    def test_sum(self):
        self.assertEqual(Calculator.sum(1, 1), 2)
        self.assertEqual(Calculator.sum(1, 2), 3)
        self.assertEqual(Calculator.sum(1, -1), 0)
        self.assertEqual(Calculator.sum(1.0, 1.0), 2.0)
        self.assertEqual(Calculator.sum(1.0, 2.0), 3.0)
        self.assertEqual(Calculator.sum(1.0, -1.0), 0.0)
