#!/usr/bin/python3
""" Define a Rectangle class that inherits from Base """
from models.base import Base


class Rectangle(Base):
    """ A Rectangle class that inherits from Base class """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Get the width of this Rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Get the height of this Rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Get the x of this Rectangle """
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Get the y of this Rectangle """
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Returns the area value of the Rectangle instance """
        return self.__width * self.__height

    def display(self):
        """ Prints in stdout the Rectangle instance with the character # """
        for noline in range(self.__y):
            print("")
        for i in range(self.__height):
            for space in range(self.__x):
                print(" ", end='')
            for j in range(self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """ Update the class Rectangle by overriding the __str__ method """
        return "[Rectangle] (" + str(self.id) + ") " + str(self.__x)\
            + "/" + str(self.__y) + " - " + str(self.__width) + "/"\
            + str(self.__height)

    def update(self, *args):
        count_argument = 0
        """
            Method that assigns an argument to each attribute
            Args:
                args: arguments replacing the attributes
        """
        for argument in args:
            if count_argument == 0:
                if argument is None:
                    self.__init__(self.width, self.height, self.x, self.y)
                else:
                    self.id = argument
            elif count_argument == 1:
                self.__width = argument
            elif count_argument == 2:
                self.__height = argument
            elif count_argument == 3:
                self.x = argument
            elif count_argument == 4:
                self.y = argument
            count_argument += 1
