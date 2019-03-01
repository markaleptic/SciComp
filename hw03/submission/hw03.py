#!/usr/bin/python

#######################################
# module: hw03.py
# Mark Allred
# A01647260
#######################################

from var import var
from const import const
from pwr import pwr
from prod import prod
from plus import plus
from quot import quot
from point2d import point2d
from maker import make_const, make_prod, make_pwr, make_pwr_expr
from maker import make_quot, make_e_expr, make_var, make_plus
from tof import tof
from deriv import deriv
from derivtest import loc_xtrm_2nd_drv_test, loc_xtrm_1st_drv_test
import math


##
# Report units, revenue, and price that will maximize a revenue
# equation given a constraint function. Revenue is demand * units.
# Function takes a conservative approach to helper functions actually
# being able to solve required problems.
def maximize_revenue(demandEquation, constraint=lambda x: x >= 0):
    # Get expression that is equivalent to multiplying demand equation by 'x',
    # rather than deriving make_prod('x', demandEquation) because find_zeros
    # functions can only solve simply polynomial expressions, not product-ruled
    # derived expressions.
    revEquation = multByVar(demandEquation)
    xtremePoints = loc_xtrm_2nd_drv_test(revEquation)
    
    if xtremePoints is None:
        xtremePoints = loc_xtrm_1st_drv_test(revEquation)
    
    maxPoint = -1.0 # impossible value
    errorCount = 0
    if xtremePoints is not None:
        for criteria, point in xtremePoints:
            if criteria == 'max':
                if constraint(point.get_x().get_val()):
                    maxPoint = point.get_x()
                else:
                    errorCount += .5
            else:
                errorCount += 1

    # Derivative tests failed, attempt brute-force linear find
    if maxPoint == -1.0 and errorCount >= len(xtremePoints):
        maxPoint = 0
        revDeriv = deriv(revEquation)
        revDerivFunc = tof(revDeriv)
        revMax = revDeriv(maxPoint)

        for unit in range(1000):
            if constraint(unit):
                if revDeriv(unit) > revMax:
                    revMax = revDerivFunc(unit)
                    maxPoint = unit
        maxPoint = make_const(val = maxPoint)
    
    # Calculate maximum revenue
    revFunc = tof(revEquation)
    maxRev = revFunc(maxPoint.get_val())
    # Calculate maximum price
    priceFunc = tof(demandEquation)
    maxPrice = priceFunc(maxPoint.get_val())

    return (make_const(maxPoint), make_const(maxRev), make_const(maxPrice))


##
# Work around for deriving Revenue Function - plays nice with find_zeroes
def multByVar(expr):
    if isinstance(expr, const):
        return make_prod(expr, make_var('x'))
    if isinstance(expr, pwr):
        if isinstance(expr.get_base(), var) and isinstance(expr.get_deg(), const):
            return make_pwr_expr(
                    expr.get_base(),
                    make_const(expr.get_deg().get_val() + 1.0)
            )
        else:
            return make_prod(make_var('x'), expr)

    elif isinstance(expr, prod):
        if isinstance(expr.get_mult1(), const) and (isinstance(expr.get_mult2(), pwr) or isinstance(expr.get_mult2(), var)):
            return make_prod(expr.get_mult1(), multByVar(expr.get_mult2()))
        else:
            return make_prod(multByVar(expr.get_mult1()), multByVar(expr.get_mult1()))

    elif isinstance(expr, plus):
        return make_plus(multByVar(expr.get_elt1()), multByVar(expr.get_elt2()))

    elif isinstance(expr, quot):
        return make_quot(multByVar(expr.get_num()), expr.get_denom())
    else:
        raise Exception('multByVar: case 01:' + str(expr))


##
# Returns const object that represents the value of 
# the derivative of yt times dxdt at the point x, 
# (y'(t) * dxdt), as a means to mirror implicit
# differentiation.
def dydt_given_x_dxdt(yt, x, dxdt):
    ytPrime = deriv(yt)

    # Multiply dx/dt by y'(t) to reduce derivative computation time
    dydt = make_prod(ytPrime, dxdt)
    
    # Convert to function to evaluate x
    dydtFunc = tof(dydt)
    assert isinstance(x, const)

    # Create and return object
    dydtAtX = dydtFunc(x.get_val())
    return make_const(dydtAtX)


##
# Specific use cases of the dydt function
def oil_disk_test():
    yt = make_prod(make_const(0.02 * math.pi),
                    make_pwr('r', 2.0))
    print(yt)
    dydt = dydt_given_x_dxdt(yt, make_const(150.0),
                             make_const(20.0))
    assert not dydt is None
    assert isinstance(dydt, const)
    print(dydt)

def arm_tumor_test():
    yt = make_prod(make_const(0.003 * math.pi),
                   make_pwr('r', 3.0))
    print(yt)
    dydt = dydt_given_x_dxdt(yt, make_const(10.3), make_const(-1.75))
    assert not dydt is None
    assert isinstance(dydt, const)
    print(dydt)