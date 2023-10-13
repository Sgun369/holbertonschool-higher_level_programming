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

    def test_max_integer_empty_list(self):
        """
        Test max_integer with an empty list
        """
        self.assert_IsNone(max_integer([]))

    def test_max_integer_single_element(self):
        """
        test max_integer with a list containing a sinngle element.
        """
        self.assertEqual(max_integer([42]), 42)


if __name__ == '__main__':
    unittest.main()
