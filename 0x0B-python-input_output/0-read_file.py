#!/usr/bin/python3
<<<<<<< HEAD
def read_file(filename=""):

=======
"""Defines a read file"""


def read_file(filename=""):
    """ reads a text file"""
    with open(filename, encoding="utf-8") as fl:
        print(fl.read(), end="")
>>>>>>> 6656863b24a76c0b5fab0d35ff5c21a83e0e9902
