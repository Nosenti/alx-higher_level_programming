#!/usr/bin/python3
"""Module to define a Square class."""


class Square:
    """Class that defines a square
    Attributes:
        __size(int): the zise of the side of the square
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square
        Args:
            size (int): square's side size. default is 0
            position (tuple): coordinates. default is (0, 0)
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        self.__size = size
        self.__position = position
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if (not isinstance(position, tuple) or len(position) != 2
                or not all(num >= 0 for num in position)
                or not all(isinstance(n, int) for n in position)):
            raise TypeError("position must be a tuple of 2 positive integers")
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

    @property
    def position(self):
        """Getter for position"""
        return self.__position

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

    @position.setter
    def position(self, value):
        """Setter for the positioin
        Args:
            value (int): value is an integer
        Raises:
            TypeError: if value is not an integer
        """
        self.__position = value
        if (not isinstance(self.__position, tuple)
                or len(self.__position) != 2 or
                not all(num >= 0 for num in self.__position) or
                not all(isinstance(n, int) for n in self.__position)):
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """prints in stdout the square with the char #"""
        if self.__size == 0:
            print("")
            return
        for i in range(0, self.__position[1]):
            [print("")]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("{:s}".format("#"), end="") for k in range(self.__size)]
            print("")
