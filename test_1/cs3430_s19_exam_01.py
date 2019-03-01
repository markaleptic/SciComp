#!/usr/bin/python

#############################################################
# module: cs3430_s19_exam_01.py
# Mark Allred
# A01647260
##############################################################

## add all your imports here
from prod import prod
from plus import plus
from quot import quot
from const import const
from maker import make_const, make_pwr, make_const, make_plus
from maker import make_prod, make_pwr_expr, make_quot, make_e_expr
from maker import make_ln, make_absv, make_var
from tof import tof
from deriv import deriv
from deriv import logdiff
from tof import tof
from deriv import deriv
from simplify import simplify
from derivtest import loc_xtrm_2nd_drv_test
from infl import find_infl_pnts
import matplotlib           # Cannot produce plots without these
matplotlib.use('TkAgg')     # two lines. Remove if necessary.
import matplotlib.pyplot as plt
import math as m
import numpy as np
import random

# ************* Problem 1 (1 point) **********************

def test_deriv(fexpr, gt, lwr, uppr, err):
    assert isinstance(lwr, const)
    assert isinstance(uppr, const)
    assert isinstance(err, const)
    
    try:
        dydx = deriv(fexpr)
    except:
        print("Unable to execute deriv using deriv() function. Attempting logderiv")
        try:
            dydx = logdiff(fexpr)
        except :
            print("Unable to determine derivative. Exiting function")
            return

    dydxFunc = tof(dydx)
    err = err.get_val()
    for i in range(lwr.get_val(), uppr.get_val()):
        assert abs(dydxFunc(i) - gt(i)) <= err

def test_q1():
    f2 = make_pwr('x', 2.0)
    f3 = make_plus(make_pwr('x', 1.0), make_const(7))
    f4 = make_plus(f2, f3)
    f5 = make_ln(f4)

    f1 = make_e_expr(make_e_expr(make_pwr('x', 1.0)))
    expr = make_plus(f1, f5)
    grTruth = lambda x: (m.e ** m.e ** x) + ((2 * x + 1) / (x**2 + x + 7))
    lower = make_const(0)
    upper = make_const(10)
    err = make_const(0.001)
    test_deriv(expr, grTruth, lower, upper, err)
test_q1()

# ************* Problem 2 (2 points) **********************

def max_profit(cost_fun, rev_fun):
    profit = make_plus(elt_expr1 = rev_fun, 
                       elt_expr2 = make_prod(mult_expr1 = make_const(-1.0), 
                                             mult_expr2 = cost_fun))
    profitPoints = loc_xtrm_2nd_drv_test(profit)
    
    assert profitPoints is not None

    maxPoint = -1
    for criteria, point in profitPoints:
        if criteria == 'max':
                if point.get_x().get_val() > 0:
                    maxPoint = point.get_x()
    
    assert maxPoint != -1

    return make_const(maxPoint)


def test_q2():
    c1 = make_pwr('x', 3.0)
    c2 = make_prod(make_const(-6.0), make_pwr('x', 2.0))
    c3 = make_prod(make_const(13.0), make_pwr('x', 1.0))
    c4 = make_const(15.0)
    c6 = make_plus(c1, c2)
    c7 = make_plus(c3, c4)
    cost = make_plus(c6, c7)
    rev = make_prod(make_const(28.0), make_pwr('x', 1.0))
    print(max_profit(cost, rev))
test_q2()

# ************* Problem 3 (2 points) **********************

def fastest_growth_time(pm, tl, tu):
    assert isinstance(tl, const)
    assert isinstance(tu, const)
    
    inflPoints = find_infl_pnts(pm)
    maxPoint = tl.get_val() - 1
    for point in inflPoints:
        if tl.get_val() <= point.get_x().get_val() <= tu.get_val():
            maxPoint = point.get_x().get_val()
    
    assert maxPoint != tl.get_val() - 1

    
    # Generate plot points for plots
    xvals = np.linspace(tl.get_val(), tu.get_val(), 1000)
    pmFunc = tof(pm)
    yVals = np.array([pmFunc(x) for x in xvals])

    # Generate Plot
    fig = plt.figure(1)
    fig.suptitle('Hive Beetle Population Growth')
    plt.xlabel('t')
    plt.ylabel('P(t)')
    xlim = [tl.get_val(), tu.get_val()]
    plt.xlim(xlim)
    plt.grid()
    plt.plot(xvals, yVals, label = str(pm), c = 'r')
    plt.legend(loc = 'best')
    plt.show()


# ************* Problem 4 (2 points) **********************

def max_norman_window_area(p):
    assert isinstance(p, const)
    first = make_prod(mult_expr1 = make_const(-1*((3.0/2.0) * m.pi - 2)), 
                      mult_expr2 = make_pwr('x', 2.0))
    second = make_prod(p, make_pwr('x', 1.0))
    expr = make_plus(first, second)
    xtrma = loc_xtrm_2nd_drv_test(expr)

    maxPoint = -1
    for criteria, point in xtrma:
        if criteria == 'max':
                if point.get_x().get_val() > 0:
                    maxPoint = point.get_x()
    
    assert maxPoint != -1

    return make_const(maxPoint)

# ************* Problem 5 (2 points) **********************

def tumor_volume_change(m, c, k):
    assert isinstance(m, const)
    assert isinstance(c, const)
    assert isinstance(k, const)
    
    vol = make_prod(mult_expr1 = make_prod(make_const(k), make_const(m.pi)), 
                    mult_expr2 = make_pwr('x', make_const(3.0)))

    volPrime = deriv(vol)
    dydt = make_prod(volPrime, c)
    dydtFunc = tof(dydt)
    dydtAtX = dydtFunc(m.get_val())
    return make_const(dydtAtX)


# ************* Problem 6 (1 point) **********************

def penicillin_amount(p0, lmbda, t):
    assert isinstance(p0, const)
    assert isinstance(lmbda, const)
    assert isinstance(t, const)
    
    pt = make_prod(mult_expr1 = p0,
                   mult_expr2 = make_e_expr(make_prod(
                                                mult_expr1 = make_const(-1 * lmbda.get_val()),
                                                mult_expr2 = make_pwr('x', 1.0))))
    ptFunc = tof(pt)
    amtRem = ptFunc(t.get_val())
    return make_const(amtRem)

def penicillin_half_life(lmbda):
    assert isinstance(lmbda, const)
    lmbda = lmbda.get_val()

    halfLifeVal = (-1 * m.log(0.5)) / lmbda
    return make_const(halfLifeVal)
    


    
