#!/usr/bin/python3
from abc import ABC, abstractmethod
"""abstract method introduction"""


class Animal(ABC):
    '''define animal'''
    @abstractmethod
    def sound(self):
        '''animal sound'''
        pass


class Dog(Animal):
    '''define dog'''
    def sound(self):
        '''dog sound'''
        return "Bark"


class Cat(Animal):
    '''define cat'''
    def sound(self):
        '''cat sound'''
        return "Meow"
