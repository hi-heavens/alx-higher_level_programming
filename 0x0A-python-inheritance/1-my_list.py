#!/usr/bin/python3
"""
Write a class MyList that inherits from list
"""


class MyList(list):
  """A class that inherit from a class"""
  def print_sorted(self):
      """print the inherited list"""
  
      print(sorted(self))


"""
Public instance method: def print_sorted(self): that prints the list, but sorted (ascending sort)
You can assume that all the elements of the list will be of type int
You are not allowed to import any module
"""
