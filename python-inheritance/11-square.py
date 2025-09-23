#!/usr/bin/python3
''' new class square '''

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    ''' class that inherits from another class '''

    def __init__(self, size):
        ''' instantation with width and height '''
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        ''' method that returns area '''
        return self.__size ** 2

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
