import unittest
from calc import Calc

class CalcTests(unittest.TestCase):

    def test_sum(self):
        calc = Calc()
        result = calc.sum(1, 1)
        self.assertEqual(2, result)


