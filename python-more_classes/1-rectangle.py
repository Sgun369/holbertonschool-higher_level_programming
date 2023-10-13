#!/usr/bin/python3
class Rectangle:
    """A class to define a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a rectangle with optional width and height."""
        self.width = width
        self.height = height

        @property
        def width(self):
            """get the width of the rectangle"""
            return self.__width

        @width.setter
        def width(self, value):
            """set the width of the rectangle"""
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

            @property
            def height(self):
                """get the height of the rectangle."""
                return self.__height

            @height.setter
            def height(self, value):
                """set the height of the rectangle."""
                if not isinstance(value, int):
                    raise TypeError("height must be an integer")
                if value < 0:
                    raise ValueError("height must be >= 0")
                self.__height = value
