#!/usr/bin/python3
""""the Suare module"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square that inherits from Recttangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns a string representation of the class"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
