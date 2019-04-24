#!/usr/bin/python
from const import const
from var import var
from prod import prod
from pwr import pwr
from plus import plus


class line_eq(object):
    def __init__(self, lhs=None, rhs=None):
        self.__lhs__ = lhs
        self.__rhs__ = rhs

    def get_lhs(self):
        return self.__lhs__

    def get_rhs(self):
        return self.__rhs__

    def __str__(self):
        return str(self.__lhs__) + ' = ' + str(self.__rhs__)