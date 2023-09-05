import sys
sys.path.append('..')

import unittest
import exercises.control_flow as control_flow

class TestControlFlow(unittest.TestCase):
    def test_total_sum(self):
        expected_sum = sum(control_flow.numbers)
        self.assertEqual(control_flow.total_sum, expected_sum, "Sum is incorrect")

if __name__ == "__main__":
    unittest.main()
