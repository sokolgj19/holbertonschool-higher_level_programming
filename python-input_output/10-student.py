#!/usr/bin/python3
"""create a class Student"""


class Student():
    """a class named student"""
    def __init__(self, first_name, last_name, age):
        """a constructor of the obj"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Public method"""
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for key in self.__dict__.keys():
            if key in attrs:
                new_dict[key] = self.__dict__[key]
        return new_dict
