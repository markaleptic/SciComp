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
from deriv import deriv
from poly12 import find_poly_1_zeros, find_poly_2_zeros
from ispwr import is_pwr_1, is_pwr_2
from tof import tof
from point2d import point2d
from simplify import simplify, remove_zeroes, multiply_through


##
# Returns list of tuples containing critical 
# points and whether they're min or max using 
# the first derivative and estimating around 
# the function. Returns None if only Saddle 
# Points are found.
def loc_xtrm_1st_drv_test(expr):
    exprDeriv = deriv(expr)

    if is_pwr_1(exprDeriv):
        # place value into tuple for ease of operation between one or two values
        zero = find_poly_1_zeros(exprDeriv)
        zeroes = (zero,)
    elif is_pwr_2(exprDeriv):
        zeroes = find_poly_2_zeros(exprDeriv)
    else:
        raise Exception('1st Deriv Polynomial Power Error: ' + str(exprDeriv))

    if isinstance(zeroes, const):
        zero = zeroes
        zeroes = []
        zeroes.append(zero)
  
    # Variables to determine if points 
    # are min, max, or saddle point
    exprFunc = tof(expr)
    leftOfX  = 0
    rightOfX = 0
    step = 0.001

    # Variable to store critical critera, and x,y coordinates 
    returnPoints = []
    
    for x in zeroes:
        # Given x in zeroes, y should equal 0 (or be close to it)
        x = x.get_val()
        y = exprFunc(x)

        leftOfX  = exprFunc(x - step)
        rightOfX = exprFunc(x + step)

        if (y - leftOfX > 0 and y - rightOfX > 0):
            # y is a max value
            returnPoints.append(('max', point2d(const(x), const(y))))
        elif (y - leftOfX < 0 and y - rightOfX < 0 ):
            # y is a min value
            returnPoints.append(('min', point2d(const(x), const(y))))
        elif ((y - leftOfX < 0 and y - rightOfX > 0) or (y - leftOfX > 0 and y - rightOfX < 0)):
            # y is a saddle point
            pass
        else:
            raise Exception('1st Deriv Critical Point Estimation Error: ' + repr(expr))
    
    if len(returnPoints) > 0:
        return returnPoints
    else:
        return None


##
# Returns list of tuples containing critical 
# points and whether they're min or max 
# using the first and second derivative test.
# Returns None if only Saddle Points are found
def loc_xtrm_2nd_drv_test(expr):
    exprFirstDeriv = simplify(deriv(expr))

    if is_pwr_1(exprFirstDeriv):
        # place value into tuple for ease of operation between one or two values
        zero = find_poly_1_zeros(exprFirstDeriv)
        zeroes = (zero,)
    elif is_pwr_2(exprFirstDeriv):
        zeroes = find_poly_2_zeros(exprFirstDeriv)
    else:
        raise Exception('1st Deriv Polynomial Power Error: ' + str(expr))

    # Variable to store critical critera, and x, y coordinates 
    returnPoints = []

    exprSecondDeriv = deriv(exprFirstDeriv)
    exprSecondDerivFunc = tof(exprSecondDeriv)
    exprFunc = tof(expr)

    for x in zeroes:
        x = x.get_val()
        criticalPoint = exprSecondDerivFunc(x)
        y = exprFunc(x)

        if criticalPoint < 0:
            returnPoints.append(('max', point2d(const(x), const(y))))
        elif criticalPoint > 0:
            returnPoints.append(('min', point2d(const(x), const(y))))
        elif criticalPoint == 0:
            pass
        else:
            raise Exception('2nd Deriv Critical Point Estimation Error: ' + str(expr))

    if len(returnPoints) > 0:
        return returnPoints
    else:
        return None