import sys
sys.path.append('..')

import unittest
import exercises.functions as functions

class TestFunctions(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(functions.factorial(5), 120, "Factorial is incorrect")
        self.assertEqual(functions.factorial(0), 1, "Factorial is incorrect")

if __name__ == "__main__":
    unittest.main()
