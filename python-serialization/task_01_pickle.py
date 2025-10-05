#!/usr/bin/env python3
"""Module that serializes and deserializes with pickle."""

import pickle


class CustomObject:
    """Object made for testing pickle implementation."""

    def __init__(self, name, age, is_student):
        """Initialize custom object."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display object attributes."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize object using pickle."""
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
            return True
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize object from file using pickle."""
        try:
            with open(filename, "rb") as file:
                python_object = pickle.load(file)
            return python_object
        except Exception:
            return None
