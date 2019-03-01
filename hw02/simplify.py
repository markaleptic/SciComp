#!/usr/bin/python

#########################################
# module: derivtest.py
# Mark Allred
# A01647260
#########################################

from var import var
from const import const
from pwr import pwr
from prod import prod
from plus import plus
from maker import make_const, make_prod, make_plus, make_pwr, make_pwr_expr
from tof import tof, const_tof, pwr_tof, prod_tof, plus_tof


def simplify(ogExpr):
    chgFlag = False
    newExpr = None

    # Keep simplifying until the final simplifcation does nothing
    while not chgFlag:
        newExpr = remove_zeroes(ogExpr)
        newExpr = multiply_through(newExpr)
        chgFlag = str(ogExpr) == str(newExpr)
        # Update ogExpr with the newest change to check against
        # the next iteration
        ogExpr = newExpr
    return newExpr


##
# Simplifying function that reduces the
# number of zeroes in an expression, but
# will leave at least one occurence of 
# zero to maintain more explicit expressions
def remove_zeroes(expr):
    if isinstance(expr, plus):
        if is_zero_const(expr.get_elt1()):
            if is_zero_const(expr.get_elt2()):
                return make_const(val = 0.0)
            else:
                return expr.get_elt2()
        elif is_zero_const(expr.get_elt2()):
            return expr.get_elt1()
        else:
            return expr
    
    elif isinstance(expr, prod):
        if is_zero_const(expr.get_mult1()) or is_zero_const(expr.get_mult2()):
            return make_const(val = 0.0)
        else:
            elt1 = remove_zeroes(expr.get_mult1())
            elt2SubExpr = remove_zeroes(expr.get_mult2())
            return make_prod(
                    mult_expr1 = elt1, 
                    mult_expr2 = elt2SubExpr
                    )
    elif isinstance(expr, pwr):
        if expr.get_deg() == 0:
            return make_const(val = 1.0)
        else:
            return expr
    
    else:
        return expr
        

##
# Simplifying expression multiplies
# constants through the other expressions
def multiply_through(expr):
    if isinstance(expr, prod):
        if isinstance(expr.get_mult1(), const) and isinstance(expr.get_mult2(), const):
            return mult_const(expr.get_mult1(), expr.get_mult2())
        elif isinstance(expr.get_mult1(), const):
            # Mult1 is constant, see if we can multiply mult1 through the subexpressions of Mult2
            if isinstance(expr.get_mult2(), prod):
                # Make accessing subexpressions more obvious
                elt2SubExpr = expr.get_mult2()
                if isinstance(elt2SubExpr.get_mult1(), const) and isinstance(elt2SubExpr.get_mult2(), var):
                    # a * (b * x) -> return c*x
                    return make_prod(
                        mult_const(expr.get_mult1(), elt2SubExpr.get_mult1()), elt2SubExpr.get_mult2()
                    )
                elif isinstance(elt2SubExpr.get_mult1(), const) and isinstance(elt2SubExpr.get_mult2(), plus):
                    # a * (b * (+)) -> return c * (+)
                    return make_prod(
                        mult_const(expr.get_mult1(), elt2SubExpr.get_mult1()), 
                        multiply_through(elt2SubExpr.get_mult2())
                    )
                elif isinstance(elt2SubExpr.get_mult1(), const) and isinstance(elt2SubExpr.get_mult2(), pwr):
                    return make_prod(
                        mult_const(expr.get_mult1(), elt2SubExpr.get_mult1()), 
                        multiply_through(elt2SubExpr.get_mult2())
                    )
                else:
                    return expr
            else:
                return expr
        else:
            return expr
    elif isinstance(expr, pwr):
        if is_zero_const(expr.get_deg()):
            return make_const(val = 1.0)
        else:
            return expr

    elif isinstance(expr, plus):
        return make_plus(
            multiply_through(expr.get_elt1()),
            multiply_through(expr.get_elt2())
        )
    else:
        return expr


##
# Returns boolean of whether an expression
# is a const object and its value is zero
def is_zero_const(expr):
    if isinstance(expr, const):
        return expr.get_val() == 0
    else:
        return False


##
# Return const object of two const values 
# multiplied together
def mult_const(mult1, mult2):
    assert isinstance(mult1, const)
    assert isinstance(mult2, const)
    return make_const(val = (mult1.get_val() * mult2.get_val()))