#!/usr/bin/python3
"""defines a class."""


class Rectangle:
    """represent Rectangle"""

    number_of_instances = 0

    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """constructor.
        Args:
            width: parameter.
            height: parameter.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        return (self.width * self.height)

    def perimeter(self):
        if not self.height == 0 or not self.width == 0:
            return (0)
        return ((self.width * 2) + (self.height * 2))

    def __str__(self):
        if not self.height or not self.width:
            return ('')
        return (((str(self.print_symbol) * self.width + '\n') *
                self.height)[:-1])

    def __repr__(self):
        return ('Rectangle(' + str(self.width) + ', ' + str(self.height) + ')')

    def __del__(self):
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area.
        Args:
            rect_1: rectangle.
            rect_2: rectangle.
        Raise:
            TypeError:rect_1 and rect_2 must be an instance of Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() < rect_2.area():
            return (rect_2)
        return (rect_1)

    @classmethod
    def square(cls, size=0):
        """return a new Rectangle.

        Args:
            size: size of a square.
        """
        return (cls(size, size))
