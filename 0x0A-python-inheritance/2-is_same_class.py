#!/usr/bin/python3
"""check if object is an instance"""


def is_same_class(obj, a_class):
    """check of obj is instance of a_class
    Return: True or False
    """
    if isinstance(type(obj), a_class):
        return True
    else:
        return False
