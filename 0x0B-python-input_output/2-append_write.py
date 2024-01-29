#!/usr/bin/python3
"""defines append"""


def append_write(filename="", text=""):
    """appends filename"""
    with open(filename, 'a', encoding="utf-8") as f:
            return f.write(text)
