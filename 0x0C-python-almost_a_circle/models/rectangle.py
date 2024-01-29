#!/usr/bin/python3
"""defines class"""
from models.Base import Base


class Rectangle(Base):
    """represents class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property
        def width(self):
            return (self.__width)

        @width.setter
        def width(self, value):

            if type(value) != int:
                raise TypeError("width must be an interger")
            if value <= 0:
                raise ValueError("width must be > 0")
            self.__width = value

        @property
        def height(self):
            return (self.__height)

        @height.setter
        def height(self, value):

            if type(value) != int:
                raise TypeError("height must be an interger")
            if value <= 0:
                raise ValueError("height must be > 0")
            self.__height = value

        @property
        def x(self):
            return (self.__x)

        @x.setter
        def x(self, value):

            if type(value) != int:
                raise TypeError("x must be an interger")
            if value < 0:
                raise ValueError("x must be >= 0")
            self.__x = value

        @property
        def y(self):

            return (self.__y)

        @y.setter
        def y(self, value):

            if type(value) != int:
                raise TypeError("y must be an interger")
            if value < 0:
                raise ValueError("y must be >= 0")
            self.__y = value

        def area(self):

            return (self.width * self.height)

        def display(self):

            if width == 0 or height == 0:
                return ()
            for n in range self.width:
                print("#")
            for num in range self.height:
                print("#")

        def __str__(self):
            return ("[Rectangle] {} {}/{} - {}/{}".format(self.id, self.x,
                    self.y, self.width, self.height))

        def update(self, *args):
            if id is not None:
                self.id = id
            if width is not None:
                self.width = width
            if x is not None:
                self.x = x
            if y is not None:
                self.y = y

        def update(self, *args, **kwargs):
            if args:
                self.__update(args)
            elif kwargs:
                self.__update(kwargs)

