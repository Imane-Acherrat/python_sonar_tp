import unittest
from utils import calculate_sum

class TestUtils(unittest.TestCase):
    def test_negative_numbers(self):
        self.assertEqual(calculate_sum(-2, -3), -5)

if __name__ == "__main__":
    unittest.main()
