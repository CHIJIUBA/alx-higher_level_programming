#!/usr/bin/python3
"""Defines a class-checking function."""


def inherits_from(obj, a_class):
    """Check if an object is inherits from a given class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj inherits from a_class - True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
