#!/usr/bin/python

####################################
# Mark Allred
# A01647260
# Homework 1
####################################

from var import var
from const import const
from pwr import pwr
from prod import prod
from plus import plus
from maker import make_const, make_pwr, make_pwr_expr
import math


# Wrapper to direct expressions to their
# requisite derivative function
def deriv(expr):
    if isinstance(expr, const):
        return const_deriv(expr)
    elif isinstance(expr, pwr):
        return pwr_deriv(expr)
    elif isinstance(expr, prod):
        return prod_deriv(expr)
    elif isinstance(expr, plus):
        return plus_deriv(expr)
    else:
        raise Exception('deriv:' + repr(expr))


# Returns the derivative of a consant--0.
def const_deriv(c = make_const(1.0)):
    assert isinstance(c, const)
    return const(val = 0.0)


# Returns the derivative of a variable--1
def var_deriv(x):
    assert isinstance(x, var)
    return const(val = 1.0)


# Returns the derivative of an addition expression
def plus_deriv(s):
    assert isinstance(s, plus)
    a = s.get_elt1()
    b = s.get_elt2()
    # Decompose expression and recompose with the derivative of
    # each component
    return plus(elt1=deriv(a), elt2=deriv(b))


# Returns the derivative of a power (exponent) expression
def pwr_deriv(p):
    assert isinstance(p, pwr)
    b = p.get_base()
    d = p.get_deg()
    if isinstance(b, var):
        if isinstance(d, const):
            # b is a variable and d is a constant
            # Return d/dx(b^d) is d * b ^ (d-1.0)
            return prod(mult1 = d, 
                        mult2 = make_pwr(b, d.get_val() - 1.0))
        else:
            raise Exception('pwr_deriv: case 1: ' + str(p))
    if isinstance(b, pwr):
        if isinstance(d, const):
            # b is another power expression and d is a constant
            # Return the product as the derivative of the outside
            # times the derivative of the inside
            return prod(mult1 = prod(mult1 = d,
                                     mult2 = make_pwr_expr(b, d.get_val() - 1.0)),
                        mult2 = pwr_deriv(b))
        else:
            raise Exception('pwr_deriv: case 2: ' + str(p))
    elif isinstance(b, plus):
        if isinstance(d, const):
            # b is an instance of plus, e.g. b represents (x + 1.0)
            # and d is a constant; return as a product the power
            # rule of the outside power and the derivative of 
            # the plus object
            return prod(mult1 = prod(mult1 = d,
                                   mult2 = make_pwr_expr(b, d.get_val() - 1.0)),
                        mult2 = plus_deriv(b))
        else:
            raise Exception('pwr_deriv: case 3: ' + str(p))
    elif isinstance(b, prod):
        if isinstance(d, const):
            # b is an instance of product, e.g. b represents (x * 1.0)
            # and d is a constant; return as a product the power
            # rule of the outside power and the derivative of 
            # the product object
            return prod(mult1 = prod(mult1 = d,
                                     mult2 = make_pwr_expr(b, d.get_val() - 1.0)),
                        mult2 = prod_deriv(b))
        else:
            raise Exception('pwr_deriv: case 4: ' + str(p))
    else:
        raise Exception('power_deriv: case 5: ' + str(p))


# Returns the derivative of a product expression
def prod_deriv(p):
    assert isinstance(p, prod)
    m1 = p.get_mult1()
    m2 = p.get_mult2()
    if isinstance(m1, const):
        if isinstance(m2, const):
            # Returns a 0-const object as the derivative of constants is zero
            return const_deriv()
        elif isinstance(m2, pwr):
            # Return constant times derivative of the power expression
            return prod(mult1 = m1,
                        mult2 = pwr_deriv(m2))
        elif isinstance(m2, plus):
            # Return constant times derivative of the plus expression
            return prod(mult1 = m1,
                        mult2 = plus_deriv(m2))
        elif isinstance(m2, prod):
            # Return constant times derivative of the product expression
            return prod(mult1 = m1,
                        mult2 = prod_deriv(m2))
        else:
            raise Exception('prod_deriv: case 1' + str(p))
    elif isinstance(m1, plus):
        if isinstance(m2, const):
            # Return constant times derivative of the plus expression
            return prod(mult1 = m2,
                        mult2 = plus_deriv(m1))
        else:
            raise Exception('prod_deriv: case 2:' + str(p))
    elif isinstance(m1, pwr):
        if isinstance(m2, const):
            # Return constant times derivative of the power expression
            return prod(mult1 = m2,
                        mult2 = pwr_deriv(m1))
        else:
            raise Exception('prod_deriv: case 3:' + str(p))
    elif isinstance(m1, prod):
        if isinstance(m2, const):
            # Return constant times derivative of the product expression
            return prod(mult1 = m2,
                        mult2 = prod_deriv(m1))
        else:
            raise Exception('prod_deriv: case 4:' + str(p))
    else:
       raise Exception('prod_deriv: case 5:' + str(p))