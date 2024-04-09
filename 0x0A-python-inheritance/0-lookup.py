#!/usr/bin/python3
"""
Write a function that returns the list of available
attributes and methods of an object
"""


def lookup(obj):
    """Returns a list"""

    return dir(obj)


"""
Prototype: def lookup(obj):
Returns a list object
You are not allowed to import any module
"""
