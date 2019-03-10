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
  assert xvals1.size == xvals2.size
  xvals = np.array([0.5 * (xvals1[i] + xvals2[i]) for i in range(xvals1.size)])
  yvals = np.array([fexpr(x) for x in xvals])

  return make_const(np.sum(yvals) * dx)


def riemann_left(fexpr, a, b, n, dx):
  a = a.get_val()
  xvals = np.array([a + i * dx for i in range(n.get_val())])
  yvals = np.array([fexpr(x) for x in xvals])
  return make_const(sum(yvals) * dx)


def riemann_right(fexpr, a, b, n, dx):
  a = a.get_val()
  xvals = np.array([a + i * dx for i in range(1, n.get_val()+1)])
  yvals = np.array([fexpr(x) for x in xvals])
  return make_const(sum(yvals) * dx)


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
    approx = riemann_approx(fexpr, a, b, make_const(i), pp)
    errorAndValue[i-1] = (i, make_const(abs(approx.get_val() - gt.get_val())))
  
  return errorAndValue
  

def plot_riemann_error(fexpr, a, b, gt, n):
  assert isinstance(a, const)
  assert isinstance(b, const)
  assert isinstance(gt, const)
  assert isinstance(n, const)
  
  ppL = -1.0
  ppM =  0.0
  ppR = +1.0

  leftApprox  = riemann_approx_with_gt(fexpr, a, b, gt, n, ppL)
  midApprox   = riemann_approx_with_gt(fexpr, a, b, gt, n, ppM)
  rightApprox = riemann_approx_with_gt(fexpr, a, b, gt, n, ppR)
  
  xvals = np.linspace(1, n.get_val()+1, n.get_val())
  leftErr = [err[1].get_val() for err in leftApprox]
  print(leftErr)
  midErr = [err[1].get_val() for err in midApprox]
  print(midErr)
  rightErr = [err[1].get_val() for err in rightApprox]
  print(rightErr)

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


  