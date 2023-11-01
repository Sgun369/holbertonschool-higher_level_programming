#!/usr/bin/python3
import json
import unittest
from models.base import Base
from models.rectangle import Rectangle
import pep8  # Import the pep8 module for PEP8 compliance check

class TestRectangleClass(unittest.TestCase):
    """Test cases for the Rectangle class"""

    def test_area(self):
        """Test the area calculation"""
        rect = Rectangle(2, 3)
        self.assertEqual(rect.area(), 6)

    def test_display(self):
        """Test the display method"""
        rect = Rectangle(3, 2)
        # Include your logic to capture the display output and assert against expected output

    def test_str(self):
        """Test the string representation method"""
        rect = Rectangle(3, 2, 1, 1, 1)
        self.assertEqual(str(rect), "[Rectangle] (1) 1/1 - 3/2")

    def test_update(self):
        """Test the update method"""
        rect = Rectangle(2, 3, 1, 1, 1)
        rect.update(10, 4, 5, 6, 7)
        self.assertEqual(str(rect), "[Rectangle] (10) 6/7 - 4/5")

    def test_to_dictionary(self):
        """Test the to_dictionary method"""
        rect = Rectangle(3, 2, 1, 1, 1)
        self.assertEqual(rect.to_dictionary(), {'id': 1, 'width': 3, 'height': 2, 'x': 1, 'y': 1})

    def test_pep8_conformance(self):
        """Test that the code conforms to PEP8."""
        style = pep8.StyleGuide(quiet=False)
        result = style.check_files(['models/rectangle.py'])  # Adjust the file path accordingly
        self.assertEqual(result.total_errors, 0, "PEP8 style errors found")

if __name__ == '__main__':
    unittest.main()
