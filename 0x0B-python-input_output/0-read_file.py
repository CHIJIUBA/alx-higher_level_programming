#!/usr/bin/python3
"""Defines a function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """Add a new attribute to an object if possible.

    Args:
        filename (any): The name of the file to read.
    """
    with open(filename, encoding="utf-8") as myFile:
        print(myFile.read(), end="")
