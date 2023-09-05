import sys
sys.path.append('..')

import unittest
import exercises.libraries as libraries

class TestLibraries(unittest.TestCase):
    def test_square_root(self):
        expected_root = libraries.math.sqrt(libraries.number)
        self.assertEqual(libraries.square_root, expected_root, "Square root is incorrect")

if __name__ == "__main__":
    unittest.main()
