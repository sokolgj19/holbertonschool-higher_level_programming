#!/usr/bin/python3
""""this module creates a rectangle"""


class Rectangle:
    """creating a rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """property getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """property setter for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """property getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """property setter for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculate area"""
        return self.width * self.height

    def perimeter(self):
        """"calculate perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        new_string = ""
        for i in range(self.height):
            for j in range(self.width):
                new_string += "#"
            if i < self.height - 1:
                new_string += "\n"
        return new_string

    def __repr__(self):
        """representing string"""
        return f"Rectangle({self.width}, {self.height})"
