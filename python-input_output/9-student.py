#!/usr/bin/python3
"""create a class Student"""


class Student():
    """a class named student"""
    def __init__(self, first_name, last_name, age):
        """a constructor of the obj"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Public method"""
        return self.__dict__
