#!/usr/bin/python3
"""
    A module that returns an object (Python data structure)
    represented by a JSON string
"""
import json


def from_json_string(my_str):
    """
        A function that returns an object (Python data structure)
        represented by a JSON string
        Args:
            my_str: JSON string to represent
    """
    return json.loads(my_str)
