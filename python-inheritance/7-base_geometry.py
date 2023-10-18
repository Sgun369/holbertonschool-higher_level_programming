#!/usr/bin/python3
""""
Geometry module
"""


class BaseGeometry:
    """"
     class BaseGeometry
    """

    def area(self):
        """"
        Raise an exception with a message
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """"
        a public instance method that vlidates value
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
