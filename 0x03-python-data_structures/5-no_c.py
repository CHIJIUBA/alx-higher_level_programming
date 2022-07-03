#!/usr/bin/env python3
"""function that removes all characters c and C from a string"""


def no_c(my_string):
    new_string = ""
    for i in my_string:
        if not ((i == 'c') or (i == 'C')):
            new_string = new_string + i
    return new_string
