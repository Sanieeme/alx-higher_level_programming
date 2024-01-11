#!/usr/bin/python3
"""defines a class."""


class Rectangle:
    """represent Rectangle"""

    def __init__(self, width=0, height=0):
        """constructor.
        Args:
            width: parameter.
            height: parameter.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        """constructor.
        Args:
            width: parameter.
        raise:
            TypeError:width must be an integer
            ValueError: width is less than 0
        """

        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        """constructor
        Args:
            height: parameter.
        raise:
            TypeError:height must be an integer
            ValueError: height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
