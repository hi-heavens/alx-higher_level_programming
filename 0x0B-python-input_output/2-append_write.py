#!/usr/bin/python3
""" A module that appends a string at the end of a text file """


def append_write(filename="", text=""):
    """
        A function that appends a string at the end of a text file (UTF8)
        and returns the number of characters added
        Args:
            filename: name of the file
            text: text to append in the file
    """
    with open(filename, "a", encoding="utf-8") as f_append:
        return (f_append.write(text))
