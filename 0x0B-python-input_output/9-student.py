#!/usr/bin/python3
"""defines class"""


class Student:
    """representation of student"""
    def __init__(self, first_name, last_name, age):
        """initialises the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns the dictionary representation"""
        return self.__dict__
