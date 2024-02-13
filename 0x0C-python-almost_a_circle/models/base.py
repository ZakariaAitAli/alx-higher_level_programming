#!/usr/bin/python3
# 0x0C. Python - Almost a circle
# Zakaria AIT ALI <zakariaaitali555@gmail.com>

"""Base class"""


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Base class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def reset_id(self):
        """reset the id"""
        self.__nb_objects = 0