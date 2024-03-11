#!/usr/bin/python3
"""defining square."""


class Square:
    """defining Square"""

    def __init__(self, size=0, position=(0, 0)):
        """constructor.
        Args:
            size: parameter.
        """
        self.size = size

    @property
    def size(self):
        return (self.__size)

    @property
    def position(self):
        return (self.__position)

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

    @position.setter
    def position(self, value):
        """construction.
        Args:
            value: parameter.
        Raise:
            TyprError: position must be a tuple of 2 positive
        """
        if not isinstance(value, int):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__postion = value

    def area(self):

        """return currebt square area
        """
        return (self.__size ** 2)

    def my_print(self):
        for num in range(0, self.__size):
            for nums in range(0, self.__size):
                print("#", end="")
            print("")
        if self.__size == 0 or position[1] > 0:
            print("")
