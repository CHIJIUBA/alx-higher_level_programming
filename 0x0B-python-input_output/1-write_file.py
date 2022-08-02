#!/usr/bin/python3
"""Defines a text file-writing function."""


def write_file(filename="", text=""):
    """Writes to a given file.

    Args:
        filename (any): The name of the file to write to.
        text (any): The text to write in the file
    """
    with open(filename, mode="w", encoding="utf_8") as f:
        f.write(text)
    return (len(text))
