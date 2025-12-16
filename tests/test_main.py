import unittest
from utils import calculate_sum

class TestMain(unittest.TestCase):
    def test_calculate_sum_positive(self):
        self.assertEqual(calculate_sum(2, 3), 5)

    def test_calculate_sum_zero(self):
        self.assertEqual(calculate_sum(0, 0), 0)
