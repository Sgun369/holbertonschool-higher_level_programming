#!/usr/bin/python3
""""
module Rectangle
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """"
    a class Retangle that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """"
        define width and height
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """"
        return the area
        """
        return self.__width * self.__height

    def __str__(self):
        """"
        return a descirption of the rectangle
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
