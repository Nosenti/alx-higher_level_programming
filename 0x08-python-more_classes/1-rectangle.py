#!/usr/bin/python3
"""A class that defines a rectangle"""


class Rectangle:
    """Class with private attibutes
    Attributes
        __width(int): width of the rectangle
        __height(int): height of the rectangle
    """
    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle
        Args:
            width (int): rectangle's side size. default is 0
            height(int): height of the rectangle
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Getter for the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width
        Args:
            value (int): value is an integer
        Raises:
            TypeError: if value is not an integer
        """
        if (value < 0):
            raise ValueError("width must be >= 0")
        elif (not isinstance(value, int)):
            raise TypeError("width must be an integer")
        self.__width = value

    @property
    def height(self):
        """Getter for the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height
        Args:
            value (int): value is an integer
        Raises:
            TypeError: if value is not an integer
        """
        if (value < 0):
            raise ValueError("height must be >= 0")
        elif (not isinstance(value, int)):
            raise TypeError("height must be an integer")
        self.__height = value
