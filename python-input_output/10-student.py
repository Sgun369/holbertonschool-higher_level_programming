#!/usr/bin/python3
"""
Student to JSON module
"""


class Student:
    """
    class Student
    """
    def __init__(self, first_name, last_name, age):
        """initialize the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation
        of a Student instance"""
        if attrs is None:
            return self.__dict__
        else:
            data = {}
            for attr in attrs:
                if hasattr(self, attr):
                    data[attr] = getattr(self, attr)
            return data
