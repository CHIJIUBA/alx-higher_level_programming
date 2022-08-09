#!/usr/bin/python3
"""Defines a Base class."""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON serialization of a list of dicts.

        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
