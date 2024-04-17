#!/usr/bin/python3
"""
    A module that writes an Object to a text file, using a JSON representation
"""


def save_to_json_file(my_obj, filename):
    """
        A function that writes an Object to a text file,
        using a JSON representation
        Args:
            my_obj: object to write
            filename: file to write to
    """
    import json
    with open(filename, "w", encoding="utf-8") as json_file:
        return json_file.write(json.dumps(my_obj))
