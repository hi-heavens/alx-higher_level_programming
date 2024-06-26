#!/usr/bin/python3
"""This is a rectangle module."""


class Rectangle:
    """nstantiation with optional width and height"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """property to retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """property setter to set value of width"""
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """property to retrieve height"""
        return self.__height

    @height.setter
    def height(self, value):
        """property setter to set value of height"""
        if (type(value) is not int):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return 2 * (self.__width + self.__height)

    def __str__(self):
        str = ""
        if self.__height == 0 or self.__width == 0:
            return (str)
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    str += '#'
                str += "\n"
        return str[:-1]
