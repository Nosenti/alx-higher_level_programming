#!/usr/bin/python3
"""check if an object is instance of"""

def is_kind_of_class(obj, a_class):
    """Check of is instance of a class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False

