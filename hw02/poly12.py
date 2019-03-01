#!/usr/bin/python

############################################
# module: poly12.py
# Mark Allred
# A01647260
############################################

from prod import prod
from const import const
from pwr import pwr
from plus import plus
from var import var
from deriv import deriv
from tof import tof
import math as m


##
# Returns const object that represents the x value where f(x) = 0
#
def find_poly_1_zeros(expr):
    # To solve a*x + c = 0 
    # Find the constant and make it negative --> a*x = -c
    constant = -1 * getConstant(expr)
    coefficient = firstOrderCoeff(expr)
    if coefficient == 0:
        return constant
    else:
        # Divide the constant by a to get x --> x = -c / a
        #print("find poly\n\nConst: %d\nCoef: %d" % (constant, coefficient))
        return const(val = (constant / coefficient))


##
# Returns const object tuple that represents the x values where f(x) = 0
#
def find_poly_2_zeros(expr):
    # Return result of quadratic
    a = secondOrderCoeff(expr)
    assert a != 0.0 # divide by zero error 
    b = firstOrderCoeff(expr)
    c = getConstant(expr)

    assert a is not None
    assert b is not None
    assert c is not None
    
    #print("find poly 2\n\na: %.4f\nb: %.4f\nc: %.4f" %(a, b, c))

    # Quadratic computation
    minB  = -1 * b
    root  = m.sqrt((b * b) - (4 * a * c))
    denom = 2 * a

    result1 = (minB + root) / denom
    result2 = (minB - root) / denom
    
    return (const(result1), const(result2))


##
# Return the constant value of polynomial
#
def getConstant(expr):
    assert expr is not None
    # Base case: return constant value
    if isinstance(expr, const):
        return expr.get_val()
    # Exclusionary base cases
    elif isinstance(expr, var):
        return 0
    elif isinstance(expr, pwr):
        if isinstance(expr.get_base(), var):
            return 0
        # Attempt to evaluate
        else:
            return getConstant(expr.get_base()) ** getConstant(expr.get_deg())
    elif isinstance(expr, prod):
        return getConstant(expr.get_mult1()) * getConstant(expr.get_mult2())
    elif isinstance(expr, plus):
        return getConstant(expr.get_elt1()) + getConstant(expr.get_elt2())
    else:
        raise Exception('getconst: ' + repr(expr))
        
    # elif isinstance(expr, prod):
    #     if(isinstance(expr.get_mult1(), var) or isinstance(expr.get_mult1(), var)):
    #         # Constant value will never be in a product
    #        return 0
    #     # TODO check for a*(x+-c)
    #     else:
    #         # Continue to unpack and return best result
    #         return findBestConst(expr.get_mult1(), expr.get_mult2())
    # elif isinstance(expr, plus):
    #     # Check for multiple constant values, although our only value is likely found
    #     if isinstance(expr.get_elt1(), const):
    #         return expr.get_elt1().get_val()
    #     # Switch elements to check for multiple constant values
    #     if isinstance(expr.get_elt2(), const):
    #         return expr.get_elt2().get_val()

    #     # Unpack further and return greatest value
    #     return findBestConst(expr.get_elt1(), expr.get_elt2())
    # elif isinstance(expr, pwr):
    #     if isinstance(expr.get_base(), var):
    #         # Constant value will not be a 'x^c'
    #         return 0
    #     else:
    #         return getConstant(expr.get_base())
    # elif isinstance(expr, var):
    #     # Return 0 if unpacked result is 'x' 
    #     return 0


##
# Return the coefficient of the first order polynomal
#
def firstOrderCoeff(expr):
    assert expr is not None
    # Constants handled inline
    if isinstance(expr, const):
        return 0

    # Return 1 if a coefficient isn't provided
    elif isinstance(expr, var):
        return 1

    # Check for power expression
    elif isinstance(expr, pwr):
        # Degrees are always constant objects - this may change
        if expr.get_deg().get_val() == 1.0:
            return firstOrderCoeff(expr.get_base())
        else:
            # Any expression with a degree != 1 will not contain the variable of interest
            return 0

    # Check for product expression
    elif isinstance(expr, prod):
        # Check for const multiplied by an object - a * (x + c)
        if isinstance(expr.get_mult1(), const):
            if isinstance(expr.get_mult2(), pwr):
                return expr.get_mult1().get_val() * firstOrderCoeff(expr.get_mult2())
            elif isinstance(expr.get_mult2(), var):
                return expr.get_mult1().get_val()
            else: 
                return expr.get_mult1().get_val() * firstOrderCoeff(expr.get_mult2())
        else:
            # Continue to unpack the expression
            return findBestFirstOrderCoefficient(expr.get_mult1(), expr.get_mult2())
    # Check for plus expression
    elif isinstance(expr, plus):
        # Continue to unpack the expression
        return findBestFirstOrderCoefficient(expr.get_elt1(), expr.get_elt2())
    else:
        raise Exception('firstOrderCoeff: ' + repr(expr))


##
# Return the coefficient of the second order polynomal
#
def secondOrderCoeff(expr):
    assert expr is not None
    # Base case: return constant value
    if isinstance(expr, const):
        return 0

    elif isinstance(expr, var):
        return 1

    # Check for product expression
    elif isinstance(expr, prod):
        # Check for const multiplied by an object - a * (x + c)
        if isinstance(expr.get_mult1(), const):
            return expr.get_mult1().get_val() * secondOrderCoeff(expr.get_mult2())
        # Switch values to check for const multiplied by an object
        elif isinstance(expr.get_mult2(), const):
            return expr.get_mult2().get_val() * secondOrderCoeff(expr.get_mult1())
        else:
            # Continue to unpack the expression
            return findBestSecondOrderCoefficient(expr.get_mult1(), expr.get_mult2())
    # Check for power expression
    elif isinstance(expr, pwr):
        # Degrees are always constant objects - this may change
        if expr.get_deg().get_val() == 2:
            # Base likely contains variable, check for prod inside
            return secondOrderCoeff(expr.get_base())
        else:
            return 0
            
    # Check for plus expression
    elif isinstance(expr, plus):
        # Attempt early exit for const
        if isinstance(expr.get_elt1(), const):
            # No need to verify, contine to unpack subexpression
            return secondOrderCoeff(expr.get_elt2())
        elif isinstance(expr.get_elt2(), const):
            # No need to verify, contine to unpack subexpression
            return secondOrderCoeff(expr.get_elt1())
        # Try to find nonzero coefficient by splitting
        else:
            return findBestSecondOrderCoefficient(expr.get_elt1(), expr.get_elt2()) 
    else:
        raise Exception('secondOrderCoeff: ' + repr(expr))


##
# Returns best match for the coefficient of an x^1.0 expression
def findBestConst(exprA, exprB):
    a = getConstant(exprA)
    b = getConstant(exprB)
    if a == b:
        return a
    elif a != 0:
        return a
    elif b != 0:
        return b
    else:
        return 0


##
# Returns best match for the coefficient of an x^1.0 expression
def findBestFirstOrderCoefficient(exprA, exprB):
    a = firstOrderCoeff(exprA)
    b = firstOrderCoeff(exprB)
    if a == b:
        return a
    elif a != 0:
        return a
    elif b != 0:
        return b
    else:
        return 0

##
# Returns best match for the coefficient of an x^2.0 expression
def findBestSecondOrderCoefficient(exprA, exprB):
    a = secondOrderCoeff(exprA)
    b = secondOrderCoeff(exprB)
    if a == b:
        return a
    elif a != 0:
        return a
    elif b != 0:
        return b
    else:
        return 0