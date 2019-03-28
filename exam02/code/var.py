#!/usr/bin/python

# bugs to vladimir kulyukin on canvas.

class var(object):
    def __init__(self, name='var'):
        self.__name__ = name

    def get_name(self):
        return self.__name__

    def __str__(self):
        return self.__name__
