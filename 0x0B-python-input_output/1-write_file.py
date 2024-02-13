#!/usr/bin/python3
"""define file"""


def write_file(filename="", text=""):
    """reads filename"""
    with open(filename, "w", encoding='utf-8') as f:
        return f.write(text)
