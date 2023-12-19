#!/usr/bin/python3
"""defining square."""


class Square:
    """defining Square"""

    def __init__(self, size=0):
        """constructor.
        Args:
            size: parameter.
        """
        self.size = size

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        """constructor.
        Args:
             size: parameter.
        Raise:
            TypeError: size must be an integer
            ValueError: size must be >=0
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >=0')
        self.__size = value

    def area(self):

        """return currebt square area
        """
        return (self.__size ** 2)
