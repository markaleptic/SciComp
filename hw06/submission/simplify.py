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


##
# Returns a simplified expression by removing zeroes
# and multiplying constants objects through plus, product
# expressions.
def simplify(ogExpr):
    chgFlag = False
    newExpr = None

    # Keep simplifying until the final simplifcation is equal to the last simplification
    while not chgFlag:
        newExpr = remove_zeroes(ogExpr)
        newExpr = multiply_through(newExpr)
        chgFlag = str(ogExpr) == str(newExpr)
        # Update ogExpr with the newest change to check against it in the next iteration
        ogExpr = newExpr
    return newExpr


##
# Simplifying function that reduces the
# number of zeroes in an expression.
def remove_zeroes(expr):
    if isinstance(expr, plus):
        if is_zero_const(expr.get_elt1()):
            if is_zero_const(expr.get_elt2()):
                # Reduce two zeroes to one
                return make_const(val = 0.0)
            else:
                # Return single non zero expression
                return expr.get_elt2()
        elif is_zero_const(expr.get_elt2()):
            # Return single non zero expression
            return expr.get_elt1()
        else:
            # No zeros found, return whole expression
            return expr
    
    elif isinstance(expr, prod):
        if is_zero_const(expr.get_mult1()) or is_zero_const(expr.get_mult2()):
            return make_const(val = 0.0)
        else:
            return make_prod(
                    mult_expr1 = remove_zeroes(expr.get_mult1()), 
                    mult_expr2 = remove_zeroes(expr.get_mult2()))
    elif isinstance(expr, pwr):
        # Return 1.0 when something is raised to the zeroeth power
        if isinstance(expr.get_deg(), const):
            if expr.get_deg().get_val() == 0:
                return make_const(val = 1.0)
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
            # Return single product of two constant objects
            return mult_const(expr.get_mult1(), expr.get_mult2())
        elif isinstance(expr.get_mult1(), const):
            # See if we can multiply Mult1 through the subexpressions of Mult2
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
            # Return 'f(x)' when 1.0 * f(x) occurs
            elif expr.get_mult1().get_val() == 1.0:
                return expr.get_mult2()
            else:
                return expr
        elif isinstance(expr.get_mult2(), const):
            # Return 'f(x)' when f(x) * 1.0 occurs
            if expr.get_mult2().get_val() == 1.0:
                return expr.get_mult1()
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
# multiplied together.
#TODO figure out the static method in const class
def mult_const(mult1, mult2):
    assert isinstance(mult1, const)
    assert isinstance(mult2, const)
    product = mult1.get_val() * mult2.get_val()
    return make_const(val = product)