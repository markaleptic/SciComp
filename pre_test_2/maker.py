#!/usr/bin/python

from var import var
from pwr import pwr
from const import const
from plus import plus
from prod import prod
from quot import quot
from point2d import point2d
from ln import ln
from absv import absv
import math
import sys

GETFRAME_EXPR = 'sys._getframe({}).f_code.co_name'

def make_var(var_name):
    # Check to see if the calling function is make_pwr 
    # and if it isn't, pass the var_name to make_pwr to 
    # avoid the error when a user wants 'x^1.0' but 
    # doesn't call make_pwr.
    callingFunc = eval(GETFRAME_EXPR.format(2))
    if callingFunc != "make_pwr":
        return make_pwr(var_name, 1.0)

    return var(name=var_name)

def make_pwr(var_name, d):
    return pwr(base=var(name=var_name), deg=const(val=d))

def make_pwr_expr(expr, deg):
    if isinstance(deg, const):
        return pwr(base=expr, deg=deg)
    else:
        return pwr(base=expr, deg=const(val=deg))

def make_const(val):
    return const(val=val)

def make_point2d(xv, yv):
    return point2d(x=make_const(xv),
                   y=make_const(yv))

def make_e_expr(d):
    if isinstance(d, float):
        return pwr(base=make_const(math.e), deg=const(val=d))
    elif isinstance(d, const):
        return pwr(base=make_const(math.e), deg=d)
    elif isinstance(d, pwr) or isinstance(d, plus) or \
         isinstance(d, prod) or isinstance(d, quot):
        return pwr(base=make_const(math.e), deg=d)
    else:
        raise Exception('make_e_expr: case 1: ' + str(d))

def make_ln(expr):
    return ln(expr=expr)

def make_quot(nexpr, dexpr):
    return quot(num=nexpr, denom=dexpr)

def make_prod(mult_expr1, mult_expr2):
    return prod(mult1=mult_expr1, mult2=mult_expr2)

def make_plus(elt_expr1, elt_expr2):
    return plus(elt1=elt_expr1, elt2=elt_expr2)

def make_absv(expr):
    return absv(expr)

def make_quadratic(a = 0.0, b = 0.0, c = 0.0, var = 'x'):
    if not isinstance(a, const):
        a = make_const(a)
    if not isinstance(b, const):
        b = make_const(b)
    if not isinstance(c, const):
        c = make_const(c)

    sq_coeff = make_prod(
                    mult_expr1 = a,
                    mult_expr2 = make_pwr(var, 2.0))
    single_coeff = make_prod(
                    mult_expr1 = b,
                    mult_expr2 = make_pwr(var, 1.0))
    constant = c
    
    expr = make_plus(elt_expr1 = make_plus(
                                    elt_expr1 = sq_coeff, 
                                    elt_expr2 = single_coeff),
                     elt_expr2 = constant)
    return expr



