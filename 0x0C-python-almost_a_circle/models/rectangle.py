#!/usr/bin/python3
"""Defines a Rectangle Class"""
Base = __import__('base').Base


class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
            x (int): The height of the new rectangle.
            y (int): The height of the new rectangle.
        """
        super.__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get/set the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Get/set the width of the Rectangle."""
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Get/set the height of the Rectangle."""
        self.__height = value

    @property
    def x(self):
        """Get/set the x of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Get/set the x of the Rectangle."""
        self.__x = value

    @property
    def y(self):
        """Get/set the y of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Get/set the y of the Rectangle."""
        self.__y = value
