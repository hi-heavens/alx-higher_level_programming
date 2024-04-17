#!/usr/bin/python3
""" A module that creates an Object from a “JSON file” """


def load_from_json_file(filename):
    """ A function that creates an Object from a “JSON file” """
    import json
    with open(filename, encoding="utf-8") as json_file:
        return json.load(json_file)
