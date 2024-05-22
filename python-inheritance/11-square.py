#!/usr/bin/python3
"""Includes Square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """Initialization method"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """returns square area"""
        return self.__size * self.__size

    def __str__(self):
        """prints string rep of square"""
        return ("[Square] {}/{}".format(self.__size, self.__size))
