import sys
sys.path.append('..')

import unittest
import exercises.variables as variables

class TestVariables(unittest.TestCase):
    def test_name(self):
        self.assertNotEqual(variables.name, "", "Name should not be empty")

if __name__ == "__main__":
    unittest.main()