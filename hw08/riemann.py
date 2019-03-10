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
  '''
  pp=0 - approximate with reimann midpoint
  pp=+1 - approximate with reimann right point
  pp=-1 - approximate with reiman left point
  '''
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
  a = a.get_val()
  xvals1 = np.array([a + i * dx for i in range(n.get_val())])
  xvals2 = np.array([a + i * dx for i in range(1, n.get_val()+1)]) 
  xvals = np.array([(0.5 * (xvals1[i] + xvals2[i]) for i in range(n.get_val()))])
  yvals = np.array([fexpr(x) for x in xvals])
  return sum(yvals) * dx


def riemann_left(fexpr, a, b, n, dx):
  a = a.get_val()
  xvals = np.array([a + i * dx for i in range(n.get_val())])
  yvals = np.array([fexpr(x) for x in xvals])
  return sum(yvals) * dx


def riemann_right(fexpr, a, b, n, dx):
  a = a.get_val()
  xvals = np.array([a + i * dx for i in range(1, n.get_val()+1)])
  yvals = np.array([fexpr(x) for x in xvals])
  return sum(yvals) * dx


def riemann_approx_with_gt(fexpr, a, b, gt, n_upper, pp=0):
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
    approx = riemann_approx(a, b, make_const(i), pp)
    errorAndValue[i] = (i, abs(approx - gt))
  
  return errorAndValue
  

def plot_riemann_error(fexpr, a, b, gt, n):
  assert isinstance(a, const)
  assert isinstance(b, const)
  assert isinstance(gt, const)
  assert isinstance(n, const)
  # your code here