#!/usr/bin/python3
''' class with method that raises exception '''


class BaseGeometry:
    ''' class with method that raises exception '''
    def area(self):
        ''' method that raises exception '''
        raise Exception("area() is not implemented")
