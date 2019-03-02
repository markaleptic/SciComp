#!/usr/bin/python


###########################################
# module: tof.py
# Mark Allred
# A01647260
###########################################

from var import var
from const import const
from pwr import pwr
from prod import prod
from plus import plus
from quot import quot
from ln import ln
from absv import absv
import math

##
# Wrapper for directing expressions to the requisite functional representation
def tof(expr):
    if isinstance(expr, const):
        return const_tof(expr)
    elif isinstance(expr, pwr):
        return pwr_tof(expr)
    elif isinstance(expr, prod):
        return prod_tof(expr)
    elif isinstance(expr, plus):
        return plus_tof(expr)
    elif isinstance(expr, quot):
        return quot_tof(expr)
    elif isinstance(expr, var):
        return var_tof(expr)
    elif isinstance(expr, ln):
        return ln_tof(expr)
    elif isinstance(expr, absv):
        return absv_tof(expr)
    else:
        raise Exception('tof: ' + str(expr))


##
# Return functional representation of a constant
def const_tof(c):
    assert isinstance(c, const)
    return lambda x: c.get_val()


##
# Return functional representation of a single variable
def var_tof(x):
    assert isinstance(x, var)
    return lambda x: x


##
# Return functional representation of exponential expression
def pwr_tof(expr):
    assert isinstance(expr, pwr)
    expb = expr.get_base()
    d = expr.get_deg()

    # Wrapper for composing multiple functions
    def compose(f, g):
        return lambda x: f(x) ** g(x)

    return compose(tof(expb), tof(d))


##
# Return functional representation of multiplication expressions
def prod_tof(expr):
    assert isinstance(expr, prod)
    a = expr.get_mult1()
    b = expr.get_mult2()

    # Wrapper for composing product / multiplication functions
    def compose(f, g):
        return lambda x: f(x) * g(x)

    return compose(tof(a), tof(b))


##
# Return functional representation of addition expressions
def plus_tof(expr):
    assert isinstance(expr, plus)
    a = expr.get_elt1()
    b = expr.get_elt2()

    # Wrapper for composing plus functions
    def compose(f, g):
        return lambda x: f(x) + g(x)

    return compose(tof(a), tof(b))


##
# Return functional representation of quotient / division expressions
def quot_tof(expr):
    assert isinstance(expr, quot)
    
    num  = expr.get_num()
    denom = expr.get_denom()

    # Wrapper for composing quotient functions
    def compose(f, g):
        return lambda x: f(x) / g(x)
    
    return compose(tof(num), tof(denom))


##
# Return functional representation of natural logarithm
def ln_tof(expr):
    assert isinstance(expr, ln)

    def compose(f):
        return lambda x: math.log(f(x), math.e)

    return compose(tof(expr.get_expr()))


##
# Return functional representation of absolute value
def absv_tof(expr):
    assert isinstance(expr, absv)

    def compose(f):
        return lambda x: abs(f(x))

    return compose(tof(expr.get_expr()))