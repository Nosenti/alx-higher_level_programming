#!/usr/bin/python3
"""Module to define a Square class."""


class Square:
    """Class that defines a square
    Attributes:
        __size(int): the zise of the side of the square
    """
    def __init__(self, size=0):
        """Initialize a new Square
        Args:
            size (int): square's side size. default is 0
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
