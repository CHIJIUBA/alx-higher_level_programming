#!/usr/bin/python3
"""Writes an Object to a text file, using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation"""
    text = json.dumps(my_obj)
    with open(filename, mode="w") as f:
        f.write(text)
