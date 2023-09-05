import sys
sys.path.append('..')

import unittest
import exercises.lists_and_dicts as lists_and_dicts

class TestListsAndDicts(unittest.TestCase):
    
    def test_even_numbers(self):
        self.assertTrue(len(lists_and_dicts.even_numbers) > 0, "List of even numbers should not be empty")
        self.assertTrue(len(lists_and_dicts.even_numbers) >= 5, "List should contain at least 5 elements")
        for num in lists_and_dicts.even_numbers:
            self.assertEqual(num % 2, 0, "List should only contain even numbers")
            
    def test_square_numbers(self):
        self.assertTrue(len(lists_and_dicts.square_numbers) > 0, "Dictionary of square numbers should not be empty")
        self.assertTrue(len(lists_and_dicts.square_numbers) >= 5, "Dictionary should contain at least 5 key-value pairs")
        for key, value in lists_and_dicts.square_numbers.items():
            self.assertEqual(key**2, value, "Dictionary values should be squares of the keys")

if __name__ == "__main__":
    unittest.main()
