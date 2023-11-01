import unittest
import pep8
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for Base class"""

    def test_to_json_string(self):
        """Test to_json_string method"""
        data = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
        json_data = Base.to_json_string(data)
        expected_json = ('[\n  {\n    "id": 1,\n    "name": "Alice"\n  },\n'
                         ' {\n    "id": 2,\n    "name": "Bob"\n  }\n]')
        self.assertEqual(json_data, expected_json)

        # Test with an empty list
        empty_data = []
        json_empty_data = Base.to_json_string(empty_data)
        self.assertEqual(json_empty_data, '[]')

    def test_save_to_file(self):
        """Test save_to_file method"""
        # Test with a non-empty list of objects
        obj1 = Base()
        obj2 = Base()
        objects = [obj1, obj2]
        Base.save_to_file(objects)
        # Validate the content of the file or check file existence

    def test_from_json_string(self):
        """Test from_json_string method"""
    # Test with valid JSON string
        valid_json = '[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]'
        expected_data = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
        data = Base.from_json_string(valid_json)
        self.assertEqual(data, expected_data)

        # Test with empty string
        empty_json = '[]'
        empty_data = Base.from_json_string(empty_json)
        self.assertEqual(empty_data, [])

    def test_create(self):
        """Test create method"""
        # Test creation with a dictionary
        data = {'id': 1, 'name': 'Alice'}
        obj = Base.create(**data)
        self.assertEqual(str(obj), "<class 'Base'>")

    def test_load_from_file(self):
        """Test load_from_file method"""
        test_data = '[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]'

        with open('test_data.json', 'w') as file:
            file.write(test_data)
        # Verify the loaded data matches the expected content
        loaded_data = Base.load_from_file()
        expected_data = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
        self.assertEqual(loaded_data, expected_data)

    def test_pep8_conformance(self):
        """Test that base.py conforms to PEP8."""
        style = pep8.StyleGuide()
        res = style.check_files(["models/base.py"])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")


if __name__ == '__main__':
    unittest.main()
