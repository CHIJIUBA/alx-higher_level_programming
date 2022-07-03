#!/usr/bin/env python3
"""function that removes all characters c and C from a string"""


def no_c(my_string):
    copy_str = [x for x in my_string if x != 'c' or x != 'C']
    return ("".join(copy_str))
