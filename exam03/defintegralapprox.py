#!/usr/bin/python

######################################
# module: defintegralapprox.py
# Mark Allred
# A01647260
######################################

# modify these as you see fit.
import numpy as np
from const import const
from maker import make_plus, make_e_expr, make_prod, make_const, make_pwr, make_pwr_expr
from tof import tof
from riemann import riemann_approx
import matplotlib.pyplot as plt

 
def midpoint_rule(fexpr, a, b, n):
  """Returns Const Midpoint Rule (Riemann Midpoint) approximation for the functional expression over [a,b] with n subintervals.
  
  returns - Const Midpoint Rule approximation

  fexpr - Functional expression to evaluate

  a - Const, lower bound

  b - Const, upper bound

  n - Const, number of intervals
  """
  
  assert isinstance(a, const)
  assert isinstance(b, const)
  assert isinstance(n, const)
  return riemann_approx(fexpr, a, b, n, 0)


def trapezoidal_rule(fexpr, a, b, n):
  """Returns Const Trapezoidal Rule approximation for the functional expression over [a,b] with n subintervals.
  
  returns - Const Trapezoidal Rule approximation

  fexpr - Functional expression to evaluate

  a - Const, lower bound

  b - Const, upper bound

  n - Const, number of intervals
  """

  assert isinstance(a, const)
  assert isinstance(b, const)
  assert isinstance(n, const)

  a = a.get_val()
  b = b.get_val()
  n = n.get_val()
  
  fexprf = tof(fexpr)
  assert fexprf is not None
  dx = (b - a) / n
  xvals = np.array([a + i * dx for i in range(n+1)], dtype=np.float32)

  # Every element but the first and last are doubled
  yvals = np.array([2.0 * fexprf(x) for x in xvals], dtype=np.float32)
  yvals[0] = yvals[0] / 2
  yvals[-1] = yvals[-1] / 2

  return make_const(np.sum(yvals) * (dx / 2.0))



def simpson_rule(fexpr, a, b, n):
  """Returns Const Simpson Rule approximation for the functional expression over [a,b] with n subintervals.
  
  returns - Const Simpson Rule approximation

  fexpr - Functional expression to evaluate

  a - Const, lower bound

  b - Const, upper bound

  n - Const, number of intervals
  """
  assert isinstance(a, const)
  assert isinstance(b, const)
  assert isinstance(n, const)

  a = a.get_val()
  b = b.get_val()
  n = n.get_val()
  
  fexpr = tof(fexpr)
  assert fexpr is not None

  dx = (b - a) / n
  xvals = np.array([a + i * dx for i in range(n + 1)], dtype=np.float32)
  
  yvals = np.zeros(n + 1, dtype=np.float32)

  for i in range(n + 1):
    if i == 0 or i == n:
      yvals[i] = fexpr(xvals[i])
    elif i % 2 == 0:
      yvals[i] = 2 * fexpr(xvals[i])
    elif i % 2 == 1:
      yvals[i] = 4 * fexpr(xvals[i])
    else:
      print("%d error" % i)

  return make_const(np.sum(yvals) * (dx / 3.0))