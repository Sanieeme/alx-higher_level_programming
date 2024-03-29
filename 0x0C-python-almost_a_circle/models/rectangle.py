#!/usr/bin/python3
"""defines class"""
from models.base import Base

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
<<<<<<< HEAD

            if type(value) != int:
                raise TypeError("width must be an interger")
            if value <= 0:
                raise ValueError("width must be > 0")
=======
            if type(value) != int:
                raise TypeError("width must be an integer")
            if value <= 0:
                raise TypeError("width must be > 0")
>>>>>>> 46ec3a4ea01742e460c27701b5752f70c8fd63c6
            self.__width = value

        @property
        def height(self):
            return (self.__height)

        @height.setter
        def height(self, value):
<<<<<<< HEAD

            if type(value) != int:
                raise TypeError("height must be an interger")
            if value <= 0:
                raise ValueError("height must be > 0")
=======
            if type(value) != int:
                raise TypeError("height must be an integer")
            if value <= 0:
                raise TypeError("height must be > 0")
>>>>>>> 46ec3a4ea01742e460c27701b5752f70c8fd63c6
            self.__height = value

        @property
        def x(self):
            return (self.__x)

        @x.setter
        def x(self, value):
<<<<<<< HEAD

            if type(value) != int:
                raise TypeError("x must be an interger")
            if value < 0:
                raise ValueError("x must be >= 0")
=======
            if type(value) != int:
                raise TypeError("x must be an integer")
            if value < 0:
                raise TypeError("x must be >= 0")
>>>>>>> 46ec3a4ea01742e460c27701b5752f70c8fd63c6
            self.__x = value

        @property
        def y(self):

            return (self.__y)

        @y.setter
        def y(self, value):
<<<<<<< HEAD

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

=======
            if type(value) != int:
                raise TypeError("y must be an integer")
            if value < 0:
                raise TypeError("y must be >= 0")
            self.__y = value

        def area(self):
            """return area"""
            return (self.width * self.height)

        def display(self):
            """print #"""
            if self.width == 0 or self.height = 0:
                print("")
                return
            [print("")for w in range(self.y)]
            for e in range(self.height)
            [print(" ", end="") for a in range(self.x)]
            [print("#", end="") for i in range(self.width)]
            print("")

        def __str__(self):
            """return str"""
            return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                    self.y, self.width, self.height)

        def update(self, *args, **kwargs):
            """update
            Args
                *args: new attributes
                *Kwargs: key /value argument
            """

            if args and len(args) != 0:
                i = 0

                for arg in args:
                    if i == 0:
                        if arg is None:
                            self.__int__(self.width, self.height, self.x,
                                            self.y)
                        else:
                            self.id = arg
                    elif i == 1:
                        self.width = arg
                    elif i == 2:
                        self.height = arg
                    elif i == 3:
                        self.x = arg
                    elif i = 4:
                        self.y = arg
                        i += 1
            elif kwargs and len(kwargs) != 0:
                for j, k in kwargs.items():
                    if j == "id":
                        if k is None:
                            self.__int__(self.width, slef.height,
                                            self.x, self.y)
                        else:
                            self.id = k
                    elif j == "width":
                        self.width = k
                    elif j == "height":
                        self.height = k
                    elif j == "x":
                        self.x = k
                    elif j == "y":
                        self.y = k

            def to_dictionary(self):
                """return dictionary"""
                return {
                        "id": self.id,
                        "width": self.width,
                        "height": self.height,
                        "x": self.x,
                        "y": self.y
                        }
>>>>>>> 46ec3a4ea01742e460c27701b5752f70c8fd63c6
