#!/usr/bin/python3
"""Author: Innocent Ingabire"""


def inherits_from(obj, a_class):
    """If object is instance of a class that
    inherited from a specified class"""
    if type(obj) != a_class:
        return True
    else:
        return False
