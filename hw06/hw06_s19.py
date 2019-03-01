#!/usr/bin/python

#############################################
# module: hw06_s19.py
# Mark Allred
# A01647260
#############################################

import math
import numpy as np
import matplotlib           # Cannot produce plots without these
matplotlib.use('TkAgg')     # two lines. Remove if necessary.
import matplotlib.pyplot as plt
from const import const
from maker import make_prod, make_const, make_pwr, make_e_expr, make_plus, make_quot
from tof import tof
from deriv import deriv


## ************* Problem 1 ******************
# Function to create functional representation of 
# Ebbinghaus Retention Model
# r(t) = (100 - a) * e ^ (- lmbda * t) + a
def percent_retention_model(lmbda, a):
    assert isinstance(lmbda, const)
    assert lmbda.get_val() > 0
    assert isinstance(a, const)
    
    # Convert lmbda to a negative
    exponent = make_prod(mult_expr1 = make_const(-1 * lmbda.get_val()), mult_expr2 = make_pwr('x', 1.0))
    # Evaluate 100 - a to make const
    coefficient = make_const(100 - a.get_val())
    # Combine coefficient and e expression
    fex = make_prod(mult_expr1 = coefficient, mult_expr2 = make_e_expr(exponent))
    # Return combined expression plus a
    return make_plus(elt_expr1 = fex, elt_expr2 = a)

    

def plot_retention(lmbda, a, t0, t1):
    assert isinstance(lmbda, const)
    assert isinstance(a, const)
    assert isinstance(t0, const)
    assert isinstance(t1, const)
    
    # Create model and derivative based on values
    model = percent_retention_model(lmbda, a)
    modelDeriv = deriv(model)

    # Create functional models to evaluate points
    modelFunc = tof(model)
    modelDerivFunc = tof(modelDeriv)

    # Create x and y values for plotting
    xvals = np.linspace(t0.get_val(), t1.get_val(), 1000)
    yvals1 = np.array([modelFunc(x) for x in xvals])
    yvals2 = np.array([modelDerivFunc(x) for x in xvals])

    # Generate Plot
    fig = plt.figure(1)
    fig.suptitle('Ebbinghaus Model of Forgetting')
    plt.xlabel('t')
    plt.ylabel('prf and dprf')
    plt.xlim(t0.get_val(), t1.get_val())
    plt.grid()
    plt.plot(xvals, yvals1, label = 'prf', c = 'r')
    plt.plot(xvals, yvals2, label = 'dprf', c = 'b')
    plt.legend(loc = 'best')
    plt.show()

    

## ************* Problem 2 ******************

def plot_spread_of_disease(p, t0, p0, t1, p1, tl, tu):
    assert isinstance(p, const) and isinstance(t0, const)
    assert isinstance(p0, const) and isinstance(t1, const)
    assert isinstance(p1, const) and isinstance(tl, const)
    assert isinstance(tu, const)
    
    # Create model and derivative based on values
    model = spread_of_disease_model(p, t0, p0, t1, p1)
    modelDeriv = deriv(model)

    # Create functional models to evaluate points
    modelFunc = tof(model)
    modelDerivFunc = tof(modelDeriv)

    # Create x and y values for plotting
    xvals = np.linspace(tl.get_val(), tu.get_val(), 1000)
    yvals1 = np.array([modelFunc(x) for x in xvals])
    yvals2 = np.array([modelDerivFunc(x) for x in xvals])

    # Generate Plot
    fig = plt.figure(1)
    fig.suptitle('Spread of Disease')
    plt.xlabel('t')
    plt.ylabel('sdf and dsdf')
    plt.xlim(tl.get_val(), tu.get_val())
    plt.grid()
    plt.plot(xvals, yvals1, label = 'prf', c = 'r')
    plt.plot(xvals, yvals2, label = 'dprf', c = 'b')
    plt.legend(loc = 'best')
    plt.show()


##
# Function that returns functional representation of model
# for epidemic growth,
# f(t) = P / (1 + B * e ^ (-c * t))
def spread_of_disease_model(p, t0, p0, t1, p1):
    assert isinstance(p, const) and isinstance(t0, const)
    assert isinstance(p0, const) and isinstance(t1, const)
    
    # Additional solving complexity necessary to handle other values
    assert t0.get_val() == 0
    B = (p.get_val() / p0.get_val()) - 1
    
    # Additional solving complexity necessary to handle other values
    assert t1.get_val() == 1.0
    
    # Removing the -1 * math.log(...) because it redundant to include it
    # and then multiply c by -1 again when constructing the exponent on e
    c =  math.log( ((p.get_val() / p1.get_val()) - 1) / B)

    # Construct the model - not including -1, see above comment on deriving c
    eExpr = make_e_expr(make_prod(mult_expr1 = make_const(c), 
                                  mult_expr2 = make_pwr('x', 1.0)))
    model = make_quot(nexpr = p, 
                      dexpr = make_plus(
                                elt_expr1 = make_const(1.0),
                                elt_expr2 = make_prod(mult_expr1 = make_const(B), 
                                                      mult_expr2 = eExpr)))
    return model


## ************* Problem 3 ******************
# Displays plot for plant growth model given values on curve and lower, upper bounds
def plot_plant_growth(m, t1, x1, t2, x2, tl, tu):
    assert isinstance(m, const) and isinstance(t1, const)
    assert isinstance(x1, const) and isinstance(t2, const)
    assert isinstance(x2, const) and isinstance(tl, const)
    assert isinstance(tu, const)
    
    model = plant_growth_model(m, t1, x1, t2, x2)
    modelDeriv = deriv(model)

    # Create functional models to evaluate points
    modelFunc = tof(model)
    modelDerivFunc = tof(modelDeriv)

    # Create x and y values for plotting
    xvals = np.linspace(tl.get_val(), tu.get_val(), 1000)
    yvals1 = np.array([modelFunc(x) for x in xvals])
    yvals2 = np.array([modelDerivFunc(x) for x in xvals])

    # Generate Plot
    fig = plt.figure(1)
    fig.suptitle('Plant Growth')
    plt.xlabel('t')
    plt.ylabel('pgf and dpgf')
    plt.xlim(tl.get_val(), tu.get_val())
    plt.grid()
    plt.plot(xvals, yvals1, label = 'prf', c = 'r')
    plt.plot(xvals, yvals2, label = 'dprf', c = 'b')
    plt.legend(loc = 'best')
    plt.show()
    

##
# Returns functional representation of plant growth using a logistic growth model.
# Model assumes y(0) = 0, and only uses one of the x,y pairs to determine the model:
# y(t) = (m + 1) / (1 + m * e ^ (-c * t)) - 1
def plant_growth_model(m, t1, x1, t2, x2):
    assert isinstance(m, const) and isinstance(t1, const)
    assert isinstance(x1, const) and isinstance(x2, const)
    assert isinstance(x2, const)
    
    # Assume y(0) = 0 to solve for c
    c = math.log ((((m.get_val() + 1) / (x1.get_val() + 1) ) - 1) / m.get_val()) / t1.get_val()

    # Plus 1 to account for y(0) = 0 assumption
    num = make_const(m.get_val() + 1)
    exponent = make_prod(make_const(c), make_pwr('x', 1.0))
    coeff = m
    denom = make_plus(make_const(1.0), make_prod(coeff, make_e_expr(exponent)))
    quotient = make_quot(num, denom)
    # Minus 1 to account for y(0) = 0 assumption
    model = make_plus(quotient, make_const(-1.0))
    return model


## ************* Problem 4 ******************
# Returns functional representation of news spreading through a population
# Model: y(t) = p(1 - e^(-k * t))
def spread_of_news_model(p, k):
    assert isinstance(p, const) and isinstance(k, const)
    coeff = make_const(-1 * p.get_val())
    eExpr = make_e_expr(make_prod(mult_expr1 = make_const(-1 * k.get_val()), 
                                  mult_expr2 = make_pwr('x', 1.0)))
    return make_plus(elt_expr1 = p, elt_expr2 = make_prod(coeff, eExpr))
    

def plot_spread_of_news(p, k, tl, tu):
    assert isinstance(p, const) and isinstance(k, const)
    assert isinstance(tl, const) and isinstance(tu, const)
    
    model = spread_of_news_model(p, k)
    modelDeriv = deriv(model)

    # Create functional models to evaluate points
    modelFunc = tof(model)
    modelDerivFunc = tof(modelDeriv)

    # Create x and y values for plotting
    xvals = np.linspace(tl.get_val(), tu.get_val(), 1000)
    yvals1 = np.array([modelFunc(x) for x in xvals])
    yvals2 = np.array([modelDerivFunc(x) for x in xvals])

    # Generate Plot
    fig = plt.figure(1)
    fig.suptitle('Spread of News')
    plt.xlabel('t')
    plt.ylabel('snf and dsnf')
    plt.xlim(tl.get_val(), tu.get_val())
    plt.grid()
    plt.plot(xvals, yvals1, label = 'prf', c = 'r')
    plt.plot(xvals, yvals2, label = 'dprf', c = 'b')
    plt.legend(loc = 'best')
    plt.show()



 
