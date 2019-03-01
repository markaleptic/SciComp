#!/usr/bin/python

###########################################
# module: maker.py
# bugs to vladimir kulyukin via canvas
###########################################

from var import var
from pwr import pwr
from const import const
from plus import plus
from prod import prod
import math

def make_var(var_name):
    return var(name=var_name)

def make_pwr(var_name, d):
    return pwr(base=var(name=var_name), deg=const(val=d))

def make_pwr_expr(expr, deg):
    return pwr(base=expr, deg=const(val=deg))

def make_const(val):
    return const(val=val)