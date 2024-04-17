#!/usr/bin/python3
""" This is a function that writes a string to a text file (UTF8)
returns the number of characters written """


def write_file(filename="", text=""):
    with open(filename, "w", encoding="utf-8") as f_write:
        return (f_write.write(text))
