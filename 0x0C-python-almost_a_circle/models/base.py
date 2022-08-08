#!/usr/bin/python3
"""Defines a Base class."""


class Base:
    """Represent a Base Class.

    Attributes:
        __nb_objects (int): The number of object instances.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base Object.

        Args:
            id (int): The id of the new base object.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
