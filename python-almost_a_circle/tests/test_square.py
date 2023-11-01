import pep8
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for Square class"""

    def test_str_representation(self):
        """Test the string representation of the square"""
        square = Square(5, 2, 3, 1)
        self.assertEqual(str(square), "[Square] (1) 2/3 - 5")

    def test_size_getter(self):
        """Test the size getter method"""
        square = Square(5)
        self.assertEqual(square.size, 5)

    def test_size_setter(self):
        """Test the size setter method"""
        square = Square(5)
        square.size = 10
        self.assertEqual(square.size, 10)

    def test_update(self):
        """Test updating the attributes of the square"""
        square = Square(5)
        square.update(2, 7, 8, 10)
        self.assertEqual(str(square), "[Square] (2) 7/8 - 10")

    def test_to_dictionary(self):
        """Test converting the square attributes to a dictionary"""
        square = Square(5, 2, 3, 1)
        square_dict = square.to_dictionary()
        expected_dict = {'id': 1, 'size': 5, 'x': 2, 'y': 3}
        self.assertDictEqual(square_dict, expected_dict)

    def test_pep8_conformance(self):
        """Test that base.py conforms to PEP8."""
        style = pep8.StyleGuide()
        res = style.check_files(["models/base.py"])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")


if __name__ == '__main__':
    unittest.main()
