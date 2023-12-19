#!/usr/bin/python3
"""defining class."""

class Square:
    """defines Square."""
    
    def __init__(self, size=0):

        """constructor.

        Args:
            size: parameter.
        Raise:
            TypeError: If size must be an integer
            ValueError: If size mut be >= 0
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
