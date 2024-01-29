#!/usr/bin/python3
"""Defines a read file"""


def read_file(filename=""):
    """ reads a text file"""
    with open(filename, encoding="utf-8") as fl:
        print(fl.read(), end="")
