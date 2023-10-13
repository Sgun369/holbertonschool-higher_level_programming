#!/usr/bin/python3
"""
unittest module
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_maw_integer(self):
        """
        Test max_integer with a list of integers.
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_integer_negative_values(self):
        """Test max_integer with a list of negative values."""
        self.assertEqual(max_integer([-5, -2, -8, -1]), -1)

    def test_max_integer_single_element(self):
        """
        test max_integer with a list containing a sinngle element.
        """
        self.assertEqual(max_integer([42]), 42)

    def test_max_integer_mixed_values(self):
        """Test max_integer with a list of mixed
        positive and negative values."""
        self.assertEqual(max_integer([-5, 2, -8, 10]), 10)

    def test_max_integer_strings(self):
        """Test max_integer with a list of strings."""
        self.assertEqual(
            max_integer(["apple", "banana", "cherry", "date"]), "date"
            )


if __name__ == '__main__':
    unittest.main()
