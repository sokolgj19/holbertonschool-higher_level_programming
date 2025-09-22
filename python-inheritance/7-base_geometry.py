#!/usr/bin/python3
''' class with method that raises exception '''


class BaseGeometry:
    ''' class with method that raises exception '''
    def area(self):
        ''' method that raises exception '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        ''' method that validates value '''
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
