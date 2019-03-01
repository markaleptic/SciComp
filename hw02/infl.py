#!/usr/bin/python

#######################################
# module: infl.py
# Mark Allred
# A01647260
#######################################

from const import const
from deriv import deriv
from poly12 import find_poly_1_zeros, find_poly_2_zeros
from ispwr import is_pwr_1, is_pwr_2
from tof import tof
from point2d import point2d
from simplify import simplify


##
# Returns list of tuples containing
# (x, y) coordinates that are inflection
# points of an expression
def find_infl_pnts(expr):
    firstDerivExpr = simplify(deriv(expr))
    secondDerivExpr = simplify(deriv(firstDerivExpr))

    # No change in concavity, no inflection points
    if isinstance(secondDerivExpr, const): return None

    if is_pwr_1(secondDerivExpr):
        # place value into tuple for ease of operation between one or two values
        zero = find_poly_1_zeros(secondDerivExpr)
        zeroes = (zero,)
    elif is_pwr_2(secondDerivExpr):
        zeroes = find_poly_2_zeros(secondDerivExpr)
    else:
        raise Exception('Deriv Polynomial Power Error: ' + str(expr))

    # Variable to store critical critera, and (x, y) coordinates 
    inflectionPoints = []
    # Convert to function to evaluate points
    exprFunc = tof(expr)

    for x in zeroes:
        x = x.get_val()
        y = exprFunc(x)
        inflectionPoints.append(point2d(const(x), const(y)))
    
    return inflectionPoints
    
    
            

    
