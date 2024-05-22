#!/usr/bin/python3
"""Includes Rectangle class"""


class Rectangle:
    """Rectangle class"""
    
    def __init__(self, width, height):
        """Initilization method"""
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
