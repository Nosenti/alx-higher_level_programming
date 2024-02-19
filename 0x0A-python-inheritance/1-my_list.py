#!/usr/bin/python3
"""MyListc-class for a List"""


class MyList(list):
    """A class MyList inherits from a list"""

    def print_sorted(self):
        print(sorted(self))

