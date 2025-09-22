#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
''' class that inherits from another class '''


class Rectangle(BaseGeometry):
    ''' class that inherits from another class '''
    def __init__(self, width, height):
        ''' instantation with width and height '''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
