#!/usr/bin/python3
"""Define a class Rectangle"""


from ast import Return


class Rectangle:
    """Represents a Rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns the width of the rectangle"""
        return (self.__width)

    @property
    def height(self):
        """Returns the height of the rectangle"""
        return (self.__height)

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return (self.__height * self.__width)

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return (0)
        return (2 * (self.__height + self.__width))
