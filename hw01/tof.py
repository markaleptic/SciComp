#!/usr/bin/python


###########################################
# module: tof.py
# Your Name
# Your A#
###########################################

from var import var
from const import const
from pwr import pwr
from prod import prod
from plus import plus
import math

def tof(expr):
    if isinstance(expr, const):
        return const_tof(expr)
    elif isinstance(expr, pwr):
        return pwr_tof(expr)
    elif isinstance(expr, prod):
        return prod_tof(expr)
    elif isinstance(expr, plus):
        return plus_tof(expr)
    else:
        raise Exception('tof: ' + str(expr))

## here is how you can implement converting
## a constant to a function.
def const_tof(c):
    assert isinstance(c, const)
    def f(x):
        return c.get_val()
    return f

# Return functional representation of exponential expression
def pwr_tof(expr):
    assert isinstance(expr, pwr)
    expb = expr.get_base()
    d = expr.get_deg()

    # Wrapper for composing multiple functions
    def compose(f, g):
        return lambda x: f(x) ** g(x)

    if isinstance(expb, const):
        # expb and d are constant values
        return compose(const_tof(expb), const_tof(d))

    elif isinstance(expb, var):
        # Variable raised to a constant power
        if isinstance(d, const):
            return lambda x: x ** d.get_val()
        else:
            raise Exception('pw_tof: case 1:' + str(expr))

    elif isinstance(expb, plus):
        if isinstance(d, const):
            # Return composition of plus representation and const
            return compose(plus_tof(expb), const_tof(d))
        else:
            raise Exception('pw_tof: case 2:' + str(expr))

    elif isinstance(expb, pwr):
        if isinstance(d, const):
            return compose(pwr_tof(expb), const_tof(d))
        else:
            raise Exception('pw_tof: case 3:' + str(expr))

    elif isinstance(expb, prod):
        if isinstance(d, const):
            return compose(prod_tof(expb), const_tof(d))
        else:
            raise Exception('pw_tof: case 4:' + str(expr))
    else:
        raise Exception('pw_tof: case 5:' + str(expr))


# Return functional representation of multiplication expressions
def prod_tof(expr):
    assert isinstance(expr, prod)
    a = expr.get_mult1()
    b = expr.get_mult2()

    # Wrapper for composing multiple functions
    def compose(f, g):
        return lambda x: f(x) * g(x)

    if(isinstance(a, const) and isinstance(b, const)):
        return compose(const_tof(a), const_tof(b))
    elif isinstance(a, const):
        return compose(const_tof(a), tof(b))
    elif isinstance(b, const):
        return compose(const_tof(b), tof(a))
    else:
        return compose(tof(a), tof(b))


# Return functional representation of addition expressions
def plus_tof(expr):
    assert isinstance(expr, plus)
    a = expr.get_elt1()
    b = expr.get_elt2()

    # Wrapper for composing multiple functions
    def compose(f, g):
        return lambda x: f(x) + g(x)

    if(isinstance(a, const) and isinstance(b, const)):
        return compose(const_tof(a), const_tof(b))
    elif isinstance(a, const):
        return compose(const_tof(a), tof(b))
    elif isinstance(b, const):
        return compose(const_tof(b), tof(a))
    else:
        return compose(tof(a), tof(b))