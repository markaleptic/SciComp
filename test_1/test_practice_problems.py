import unittest
import unittest
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
import matplotlib           # Cannot produce plots without these
matplotlib.use('TkAgg')     # two lines. Remove if necessary.
import matplotlib.pyplot as plt
import math as m
import random


def generateXValues(lbound, ubound, numPoints):
    step = abs(ubound - lbound) / numPoints
    xValues = [0]*numPoints
    for i in range(numPoints):
        xValues[i] = step * i + lbound
    
    return xValues

def getDecayConstant(t, returnConst = True):
    if isinstance(t, const):
        t = t.get_val()

    decayVal = m.log(0.5) / t

    if returnConst:
        decayVal = make_const(decayVal)

    return decayVal

##
# Question: Write a function that takes a function representation a function, f(x), differentiates it, and plots f(x) and f'(x) on the interval |x_1, x_2|.
# Approach: Differentiate the function, convert both the expr and expr_prime through tof to get all the xvals in the range and yvals.
#           Use min, max logic to get |y_1, y_2| interval 
def problem_1(expr, xvals):
    assert len(xvals) == 2

    if(xvals[0] == xvals[1]):
        print("Range in x values is zero, no points to plot")
        return

    # Convert expressions to functions to evaluate x-values
    fx = tof(expr)
    fxdx = tof(logdiff(expr))

    # Generate list of range values - dynamically determine step to always generate 1000 points
    numberOfPoints = 1000
    step = abs(xvals[0] - xvals[1]) / numberOfPoints
    xValues = [0]*numberOfPoints
    for i in range(numberOfPoints):
        xValues[i] = step * i + xvals[0]

    # Generate range of y values for f(x) and f'(x)
    yValsFx = [fx(x) for x in xValues]
    yValsfxdx = [fxdx(x) for x in xValues]

    # Determine the largest y-value for plotting
    fxMax = max(yValsFx)
    fxdxMax = max(yValsfxdx)
    
    ymax = 0
    if fxMax >= fxdxMax:
        ymax = fxMax
    else:
        ymax = fxdxMax

    # Determine the smallest y-value for plotting
    fxMin = min(yValsFx)
    fxdxMin = min(yValsfxdx)

    ymin = 0
    if fxMin <= fxdxMin:
        ymin = fxMin
    else:
        ymin = fxdxMin
    
    # Set range for y-values using min, max
    yRange = [ymin, ymax]

    fig = plt.figure(1)
    fig.suptitle('Function and its Derivative')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xlim(xvals)
    plt.ylim(yRange)
    plt.grid()
    plt.plot(xValues, yValsFx, label = 'y = f(x)', c = 'r')
    plt.plot(xValues, yValsfxdx, label = 'y = f\'(x)', c = 'g')
    plt.legend(loc = 'best')
    plt.show()

    

def problem_1_test():
    # Top of expression = (x+1)*(2x+1)*(3x+1)
    f1 = make_plus(make_pwr('x', 1), make_const(1))
    f2 = make_plus(make_prod(make_const(2), make_pwr('x', 1)), make_const(1))
    f3 = make_plus(make_prod(make_const(3), make_pwr('x', 1)), make_const(1))
    f5 = make_prod(f1, f2)
    f6 = make_prod(f5, f3)

    # Bottom of expression = (4x + 1)^(1/2)
    f4 = make_pwr_expr(make_plus(make_prod(make_const(4), make_pwr('x', 1)), make_const(1)), make_const(1.0/2.0))

    # Full expression = top / bottom
    expr = make_quot(f6, f4)
    # Create range for graphs
    x_range = [0, 50]
    # Pass to function
    problem_1(expr, x_range)
    return

# Question: Write a function that takes a function representation of f(x), computes the second derivative, and evalutes it at some point
def problem_2(expr, x):
    try:
        d2fdx2 = deriv(deriv(expr))
        d2fdx2Func = tof(d2fdx2)
    except:
        print("Unable to estimate derivative using regular deriv, atttempting with logdiff then deriv...")
        try:
            d2fdx2 = deriv(logdiff(expr))
            d2fdx2Func = tof(d2fdx2)
        except:
            print("Failed to estimate derivative. Exiting function..")
            return
    
    print("The value of x in the second derivative is %s" % str(d2fdx2Func(x)))
    return


def problem_2_test():
    f1 = make_pwr('x', 2.0)
    f2 = make_ln(make_var('x'))
    f3 = make_prod(f1, f2)
    problem_2(f3, 5.0)

# Write a function that takes a function representation and a point and returns a tanglent representation at that point
def problem_3(expr, point):
    # Calculate derivative and create function to evaluate point
    dydx = deriv(expr)
    dydxFunc = tof(dydx)
    
    # Convert point to raw point if it's a const
    if isinstance(point, const):
        point = point.get_val()
    
    slope = dydxFunc(point)
    
    yfunc = tof(expr)
    y1 = yfunc(point)
    #Create y = mx - m*x_1 + y_1 for tangent line
    tangent = make_plus(
                elt_expr1 = make_prod(make_const(slope), make_var('x')), 
                elt_expr2 = make_const(val = ((-slope * point) + y1)))
    
    tangentFunc = tof(tangent)
    return tangent, tangentFunc

def problem_3_test():
    expr = make_e_expr(make_pwr('x', 1.0))
    tangent, func = problem_3(expr, -1)
    print(tangent)

def problem_4():
    pass

def problem_4_test():
    pass

def problem_5():
    pass

def problem_6():
    pass

def problem_7():
    pass

def problem_8():
    pass

def problem_9(expr, p0):
    t = -0.021 # the constant that satisfies p'(t) = c * p(t)
    decayConst = -m.log(0.5) / t
    return


def problem_9_test():
    pass


# Question: write a function that takes a constant value and genereates 3 arbitray solutions to the function
def problem_10(k):
    arbitraryValue1 = random.randint(1,10)
    fx1 = make_prod(
                mult_expr1 = make_const(arbitraryValue1), 
                mult_expr2 = make_e_expr(make_prod(make_const(k), make_pwr('x', 1.0))))

    arbitraryValue2 = random.randint(1,10)
    fx2 = make_prod(
                mult_expr1 = make_const(arbitraryValue2), 
                mult_expr2 = make_e_expr(make_prod(make_const(k), make_pwr('x', 1.0))))

    arbitraryValue3 = random.randint(1,10)
    fx3 = make_prod(
                mult_expr1 = make_const(arbitraryValue3), 
                mult_expr2 = make_e_expr(make_prod(make_const(k), make_pwr('x', 1.0))))

    fx1Func = tof(fx1)
    fx2Func = tof(fx2)
    fx3Func = tof(fx3)

    xlim = [-5, 5]
    xvals = generateXValues(xlim[0], xlim[1], 1000)
    yvals1 = [fx1Func(x) for x in xvals]
    yvals2 = [fx2Func(x) for x in xvals]
    yvals3 = [fx3Func(x) for x in xvals]

    fig = plt.figure(1)
    fig.suptitle('Solutions to y\' = %sy' % str(k))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xlim(xlim)
    plt.grid()
    plt.plot(xvals, yvals1, label = str(fx1), c = 'r')
    plt.plot(xvals, yvals2, label = str(fx2), c = 'g')
    plt.plot(xvals, yvals3, label = str(fx3), c = 'b')
    plt.legend(loc = 'best')
    plt.show()

def problem_10_test():
    problem_10(0.5)

# Question: write a function that takes an aribtrary constant k and y(0) = y0, graphs unique solution to y' = ky
def problem_11(k, y0):
    fx = make_prod(
                mult_expr1 = make_const(k), 
                mult_expr2 = make_e_expr(make_prod(make_const(y0), make_pwr('x', 1.0))))
    
    xlim = [-5, 5]
    xvals = generateXValues(xlim[0], xlim[1], 1000)
    fxFunc = tof(fx)
    yvals = [fxFunc(x) for x in xvals]

    fig = plt.figure(1)
    fig.suptitle('y = %se^{%st}' % (str(y0), str(k)))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xlim(xlim)
    plt.grid()
    plt.plot(xvals, yvals, label = str(fx), c = 'r')
    plt.legend(loc = 'best')
    plt.show()


def problem_11_test():
    problem_11(3, 2)
    pass    

# problem_1_test()
# problem_2_test()
# problem_3_test()
# problem_4_test()
# problem_5_test()
# problem_6_test()
# problem_7_test()
# problem_8_test()
# problem_9_test()
# problem_10_test()
# problem_11_test()