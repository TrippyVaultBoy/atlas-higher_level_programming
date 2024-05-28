#!/usr/bin/python3
"""Includes Square class that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines class Square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(id)
        super().__init__(width)
        super().__init__(height)
        super().__init__(x)
        super().__init__(y)

        Square.attribute_validate(width, "width")
        Square.attribute_validate(height, "height")
        Square.attribute_validate(x, "x")
        Square.attribute_validate(y, "y")

        self.__width = size
        self.__height = size
        self.__x = x
        self.__y = y