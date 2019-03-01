#!/usr/bin/python

###########################################
# module: graph_drv.py
# Mark Allred
# A01647260
###########################################

from var import var
from const import const
from pwr import pwr
from prod import prod
from deriv import deriv
from plus import plus
from tof import tof
from maker import make_pwr, make_const, make_pwr_expr
from deriv import deriv
from tof import tof
import numpy as np
import matplotlib           # Cannot produce plots without these
matplotlib.use('TkAgg')     # two lines. Remove if necessary.
import matplotlib.pyplot as plt
import math

def graph_drv(fexpr, xlim, ylim):
    # Verify length of plot parameters
    assert len(xlim) == 2
    assert len(ylim) == 2

    # Convert mathematical expressions to functional expressions
    drv = deriv(fexpr)
    f1 = tof(fexpr)
    f2 = tof(drv)

    # Generate plot points for plots
    xvals = np.linspace(xlim[0], xlim[1], 1000)
    yvals1 = np.array([f1(x) for x in xvals])
    yvals2 = np.array([f2(x) for x in xvals])

    # Generate Plot
    fig = plt.figure(1)
    fig.suptitle('Function and its Derivative')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.grid()
    plt.plot(xvals, yvals1, label = 'y = f(x)', c = 'r')
    plt.plot(xvals, yvals2, label = 'y = \'f(x)', c = 'g')
    plt.legend(loc = 'best')
    plt.show()