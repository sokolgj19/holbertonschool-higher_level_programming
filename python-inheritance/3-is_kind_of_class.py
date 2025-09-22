#!/usr/bin/python3
"""returns True if the object is an instance """


def is_kind_of_class(obj, a_class):
    """an instance of the specified class"""
    if not isinstance(obj, a_class):
        return False
    return True
