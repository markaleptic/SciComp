#!/usr/bin/python

###############################################
# module: riemann.py
# Mark Allred
# A01647260
###############################################

## modify these imports as you see fit.
import numpy as np
from const import const
from antideriv import antiderivdef
from tof import tof
import matplotlib.pyplot as plt
from maker import make_const


def riemann_approx(fexpr, a, b, n, pp=0):
  """
  Returns a Const approximation of the functional expression over the 
  interval [a, b] given n subintervals for the specified Riemann 
  Approxmation method.

  returns Const

  fexpr - Functional expression to evaluate

  a - Const, lower bound

  b - Const, upper bound

  n - Const, number of intervals

  pp - Int, riemann approximation method

  pp =  0 - Riemann Midpoint
  pp = +1 - Riemann right point
  pp = -1 - Riemann left point
  """

  assert isinstance(a, const)
  assert isinstance(b, const)
  assert isinstance(n, const)
  fexprf = tof(fexpr)
  assert(fexprf) is not None
  dx = (b.get_val() - a.get_val()) / n.get_val()

  
  if pp == 0:
    return riemann_midpoint(fexprf, a, b, n, dx)
  elif pp == 1:
    return riemann_right(fexprf, a, b, n, dx)
  elif pp == -1:
    return riemann_left(fexprf, a, b, n, dx)
  else:
    print("Incorrect Partition Point provided", pp)


def riemann_midpoint(fexpr, a, b, n, dx):
  """Call riemann_approx to access this function."""

  a = a.get_val()
  xvals1 = np.array([a + i * dx for i in range(n.get_val())], dtype=np.float32)
  xvals2 = np.array([a + i * dx for i in range(1, n.get_val()+1)], dtype=np.float32) 
  assert xvals1.size == xvals2.size
  xvals = np.array([0.5 * (xvals1[i] + xvals2[i]) for i in range(xvals1.size)], dtype=np.float32)
  yvals = np.array([fexpr(x) for x in xvals], dtype=np.float32)

  return make_const(np.sum(yvals) * dx)


def riemann_left(fexpr, a, b, n, dx):
  """Call riemann_approx to access this function."""
  
  a = a.get_val()
  xvals = np.array([a + i * dx for i in range(n.get_val())], dtype=np.float32)
  yvals = np.array([fexpr(x) for x in xvals], dtype=np.float32)
  return make_const(sum(yvals) * dx)


def riemann_right(fexpr, a, b, n, dx):
  """Call riemann_approx to access this function."""

  a = a.get_val()
  xvals = np.array([a + i * dx for i in range(1, n.get_val()+1)], dtype=np.float32)
  yvals = np.array([fexpr(x) for x in xvals])
  return make_const(sum(yvals) * dx)


def riemann_approx_with_gt(fexpr, a, b, gt, n_upper, pp=0):
  """Returns a vector of 2-tuples of the interval and Const error for the specified Riemann approximation against the ground truth value.

  Returns -  List of 2-tuples, (int) Interval and (const) Error
  
  a - Const, lower bound

  b - Const, upper bound

  gt - Const, ground truth

  n_upper - Const, number of intervals to estimate

  pp - Int, riemann approximation method

  pp=0 - approximate with reimann midpoint
  pp=+1 - approximate with reimann right point
  pp=-1 - approximate with reiman left point
  """

  assert isinstance(a, const)
  assert isinstance(b, const)
  assert isinstance(gt, const)
  assert isinstance(n_upper, const)

  if n_upper.get_val() < 0:
    print("Negative upper bound provided, using absolute value...")
    n_upper = make_const(abs(n_upper.get_val()))

  # initialize empty array
  errorAndValue = [0] * n_upper.get_val()
  
  for i in range(1, n_upper.get_val()+1):
    approx = riemann_approx(fexpr, a, b, make_const(i), pp)
    errorAndValue[i-1] = (i, make_const(abs(approx.get_val() - gt.get_val())))
  
  return errorAndValue
  

def plot_riemann_error(fexpr, a, b, gt, n):
  """Plots the the error for each of the Riemann approximation methods over n subintervals.

  a - Const, lower bound

  b - Const, upper bound

  gt - Const, ground truth

  n - Const, number of intervals to estimate
  """

  assert isinstance(a, const)
  assert isinstance(b, const)
  assert isinstance(gt, const)
  assert isinstance(n, const)
  
  # Partion Points for left, mid, & right Riemann Approximation
  ppL = -1.0
  ppM =  0.0
  ppR = +1.0

  # Generate error approximations for the given expression, bounds, actual value, and upper bound on subintervals
  leftApprox  = riemann_approx_with_gt(fexpr, a, b, gt, n, ppL)
  midApprox   = riemann_approx_with_gt(fexpr, a, b, gt, n, ppM)
  rightApprox = riemann_approx_with_gt(fexpr, a, b, gt, n, ppR)
  
  # Create x-values for graph
  xvals = np.linspace(1, n.get_val()+1, n.get_val())
  # Create y-values for each error by slicing out error values for each approximation
  leftErr = [err[1].get_val() for err in leftApprox]
  midErr = [err[1].get_val() for err in midApprox]
  rightErr = [err[1].get_val() for err in rightApprox]

  fig = plt.figure(1)
  fig.suptitle('Riemann Approximation Error')
  plt.xlabel('n')
  plt.ylabel('err')
  plt.xlim(0, n.get_val())
  plt.grid()
  plt.plot(xvals, leftErr, label = 'left', c = 'g')
  plt.plot(xvals, midErr, label = 'mid', c = 'r')
  plt.plot(xvals, rightErr, label = 'right', c = 'b')
  plt.legend(loc = 'best')
  plt.show()


  