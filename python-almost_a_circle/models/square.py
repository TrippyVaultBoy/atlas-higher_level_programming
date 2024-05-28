#!/usr/bin/python3
"""Includes Square class that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines class Square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

        self.__width = size
        self.__height = size

    def __str__(self):
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}".format(
            type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """size getter"""
        return self.size

    @size.setter
    def size(self, value):
        """size setter"""
        self.attribute_validate(value, "width")

        self.size = size
