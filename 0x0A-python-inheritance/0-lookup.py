#!/usr/bin/python3
"""returns the list of available attributes and methods of an object."""

def lookup(obj):
    """returns the list of available attributes and methods of an object.

    Args:
        obj (object): The object to check.
    """

    obj_class = type(obj).__name__
    method_list = [attribute for attribute in dir(obj_class)]

    return method_list
