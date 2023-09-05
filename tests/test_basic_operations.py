import sys
sys.path.append('..')

import unittest
import exercises.basic_operations as basic_operations
import math

class TestBasicOperations(unittest.TestCase):
    def test_area(self):
        expected_area = math.pi * basic_operations.radius ** 2
        self.assertEqual(basic_operations.area, expected_area, "Area calculation is incorrect")

if __name__ == "__main__":
    unittest.main()
