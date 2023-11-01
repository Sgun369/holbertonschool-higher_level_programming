#!/usr/bin/pyhthon3

import json
import unittest
import pep8 
from models.base import Base

class TestBase(unittest.TestCase):

    def test_pep8(self):
        """Test that the code conforms to PEP8"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0, "Fix pep8")

    def test_save_load(self):
        rectangles = [Base.create(width=2, height=3, id=1),
                      Base.create(width=4, height=3, id=2)]
        self.assertEqual(len(rectangles), 2)

        # Save to disk
        filename = 'rectangles.json'
        with open(filename, 'w') as f:
            json.dump([r.to_json_string() for r in rectangles], f)

        # Load from disk
        with open(filename, 'r') as f:
            saved_rectangles = json.load(f)

        loaded_rectangles = [Base.from_json_string(r) for r in saved_rectangles]
        self.assertEqual(len(loaded_rectangles), 2)

    def test_to_json_string(self):
        obj = Base.create(width=2, height=3, id=1)
        self.assertEqual(obj.to_json_string(), '{"id": 1, "width": 2, "height": 3}')

    def test_from_json_string(self):
        expected_obj = Base.create(width=2, height=3, id=1)
