#!/usr/bin/python3
"""Defines a text file-writing (appends to a given file) function."""


def append_write(filename="", text=""):
    """Append to a given file, creates file if not exist

    Args:
        filename (any): The name of the file to write to.
        text (any): The text to write in the file
    """
    with open(filename, mode="a", encoding="utf_8") as f:
        f.write(text)
    return len(text)
