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

    def area(self):
        """public instance method area
        Returns:
            square area
        """
        square_area = self.__size * self.__size
        return square_area

    @property
    def size(self):
        """Getter for the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size
        Args:
            value (int): value is an integer
        Raises:
            TypeError: if value is not an integer
        """
        self.__size = value
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
