#!/usr/bin/puthon3

import json
import unittest
from models.base import Base
from models.square import Square
import pep8  # Import the pep8 module for PEP8 compliance check

class TestSquareClass(unittest.TestCase):
    """Test cases for the Square class"""

    def test_size_property(self):
        """Test the size property"""
        sq = Square(5)
        self.assertEqual(sq.size, 5)

    def test_str(self):
        """Test the string representation method"""
        sq = Square(5, 1, 1, 1)
        self.assertEqual(str(sq), "[Square] (1) 1/1 - 5")

    def test_update(self):
        """Test the update method"""
        sq = Square(5, 1, 1, 1)
        sq.update(10, 7, 8, 9)
        self.assertEqual(str(sq), "[Square] (10) 9/8 - 7")

    def test_to_dictionary(self):
        """Test the to_dictionary method"""
        sq = Square(5, 1, 1, 1)
        self.assertEqual(sq.to_dictionary(), {'id': 1, 'size': 5, 'x': 1, 'y': 1})

    def test_pep8_conformance(self):
        """Test that the code conforms to PEP8."""
        style = pep8.StyleGuide(quiet=False)
        result = style.check_files(['models/square.py'])  # Adjust the file path accordingly
        self.assertEqual(result.total_errors, 0, "PEP8 style errors found")

if __name__ == '__main__':
    unittest.main()
