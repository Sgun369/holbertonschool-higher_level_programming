import pep8
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle class"""

    def test_area(self):
        """Test the area calculation of the rectangle"""
        rect = Rectangle(3, 4)
        self.assertEqual(rect.area(), 12)

    def test_perimeter(self):
        """Test the perimeter calculation of the rectangle"""
        rect = Rectangle(3, 4)
        self.assertEqual(rect.perimeter(), 14)

    def test_str_representation(self):
        """Test the string representation of the rectangle"""
        rect = Rectangle(3, 4, 2, 1, 5)
        self.assertEqual(str(rect), "[Rectangle] (5) 2/1 - 3/4")

    def test_update(self):
        """Test updating the attributes of the rectangle"""
        rect = Rectangle(3, 4, 2, 1, 5)
        rect.update(10, 5, 5, 2, 3)
        self.assertEqual(str(rect), "[Rectangle] (10) 5/5 - 2/3")

    def test_to_dictionary(self):
        """Test converting the rectangle attributes to a dictionary"""
        rect = Rectangle(3, 4, 2, 1, 5)
        rect_dict = rect.to_dictionary()
        expected_dict = {'id': 5, 'width': 3, 'height': 4, 'x': 2, 'y': 1}
        self.assertDictEqual(rect_dict, expected_dict)

    def test_pep8_conformance(self):
        """Test that base.py conforms to PEP8."""
        style = pep8.StyleGuide()
        res = style.check_files(["models/base.py"])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")


if __name__ == '__main__':
    unittest.main()
