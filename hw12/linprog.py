#!/usr/bin/python

###################################
# module: linprog.py
# Mark Allred
# A01647260
###################################

## your imports

from maker import make_line_eq
from line_eq import line_eq
from poly12 import is_const_line, get_line_coeffs, getConstant
from point2d import point2d
from maker import make_var, make_const, make_prod, make_pwr, make_plus
from maker import make_point2d
from const import const
from var import var
from prod import prod
from pwr import pwr
from ispwr import is_pwr_1
from plus import plus
from tof import tof
import sys



### sample line equations
lneq1 = make_line_eq(make_var('y'),
                     make_const(2))
lneq2 = make_line_eq(make_var('y'),
                     make_var('x'))
lneq3 = make_line_eq(make_var('y'),
                     make_var('y'))
lneq4 = make_line_eq(make_var('y'),
                     make_prod(make_const(2.0),
                               make_pwr('x', 1.0)))
lneq5 = make_line_eq(make_var('y'),
                     make_prod(make_const(5.0),
                               make_pwr('y', 1.0)))
lneq6 = make_line_eq(make_var('y'),
                     make_plus(make_prod(make_const(5.0),
                                         make_pwr('x', 1.0)),
                               make_const(4.0)))
lneq7 = make_line_eq(make_var('y'),
                     make_plus(make_prod(make_const(5.0),
                                         make_pwr('y', 1.0)),
                               make_const(4.0)))
lneq8 = make_line_eq(make_var('y'),
                     make_plus(make_prod(make_const(3.0),
                                         make_pwr('x', 1.0)),
                               make_const(-4.0)))


def line_intersection(lneq1, lneq2):
  """Returns Point2d (x,y) coordinate pair where the two line equations intersect, or None"""
  
  # y1 = Ax + B and y2 = Cx + D ==> x = (D - B) / (A - C)
  
  assert isinstance(lneq1, line_eq)
  assert isinstance(lneq2, line_eq)

  if is_const_line(lneq1) and is_const_line(lneq2):
    y = make_const(getConstant(lneq1.get_rhs()))
    x = make_const(getConstant(lneq2.get_rhs()))
    return point2d(x, y)

  A, B = get_line_coeffs(lneq1)
  C, D = get_line_coeffs(lneq2)

  if A - C == 0:
    return None

  x = (D - B) / (A - C)

  y1Func = tof(lneq1.get_rhs())
  y2Func = tof(lneq2.get_rhs())
  y1 = y1Func(x)
  y2 = y2Func(x)
  error = 0.0001
  assert abs(y1 - y2) <= error

  return point2d(make_const(x), make_const(y1))


def maximize_obj_fun(f, corner_points):
  """Returns the (x,y) point and value that maximizes the passed in function from the list of corner_points"""
  maxPoint = None
  maxVal = None

  for point in corner_points:
    assert isinstance(point, point2d)
    x = point.get_x().get_val()
    y = point.get_y().get_val()
    val = f(x, y)
    if maxVal is None or val > maxVal:
      maxPoint = point
      maxVal = val
  
  return maxPoint, maxVal

def minimize_obj_fun(f, corner_points):
  """Returns the (x,y) point and value that minimizes the passed in function from the list of corner_points"""
  minPoint = None
  minVal = None

  for point in corner_points:
    assert isinstance(point, point2d)
    x = point.get_x().get_val()
    y = point.get_y().get_val()
    val = f(x, y)
    if minVal is None or val < minVal:
      minPoint = point
      minVal = val
  
  return minPoint, minVal


## write your answer to problem 1a as x, y, mv
## Answer: x=5, y=1, mv=11.0
def opt_prob_1a():
  print("\nOptimization Problem 1a")
  f = lambda x, y: 2*x + y
  ln1 = make_line_eq('y',make_const(1.0))
  ln2 = make_line_eq('x',make_const(1.0))
  ln3 = make_line_eq('y', make_plus(make_const(6), make_prod(make_const(-1.0), make_pwr('x', 1.0))))
  
  intersection1 = line_intersection(ln1, ln2)
  intersection2 = line_intersection(ln3, ln1)
  intersection3 = line_intersection(ln3, ln2)

  maxPoint, maxVal = maximize_obj_fun(f, [intersection1, 
                                          intersection2, 
                                          intersection3])

  print("Max Point", maxPoint)
  print("Max Value", maxVal)



## write your answer to problem 1b as x, y, mv
## Answer: x=0, y=2.0 , mv=2.0
def opt_prob_1b():
  print("\nOptimization Problem 1b")
  f = lambda x, y: (1/2)*x + y
  ln1 = make_line_eq('y',make_const(2.0))
  ln2 = make_line_eq('x',make_const(0))
  ln3 = make_line_eq('y', make_pwr('x', 1.0))
  ln4 = make_line_eq('y', make_plus(make_const(6), make_prod(make_const(-1.0), make_pwr('x', 1.0))))
  
  intersection1 = line_intersection(ln1, ln2)
  intersection2 = line_intersection(ln2, ln4)
  intersection3 = line_intersection(ln3, ln4)
  intersection4 = line_intersection(ln1, ln3)

  minPoint, minVal = minimize_obj_fun(f, [intersection1, 
                                          intersection2, 
                                          intersection3,
                                          intersection4])

  print("Min Point", minPoint)
  print("Min Value", minVal)

## write your answer to problem 1c as x, y, mv
## Answer: x=7.5, y=7.5, mv=7.5
def opt_prob_1c():
  print("\nOptimization Problem 1c")
  f = lambda x, y: 3*x - 2*y
  
  ln1 = make_line_eq('y', make_prod(make_const(-1.0), make_pwr('x', 1.0)))
  ln2 = make_line_eq('y', make_pwr('x', 1.0))
  ln3 = make_line_eq('y', make_plus(make_prod(make_const(1/2), make_pwr('x', 1.0)), make_const(15/4)))

  intersection1 = line_intersection(ln1, ln2)
  intersection2 = line_intersection(ln2, ln3)
  intersection3 = line_intersection(ln1, ln3)

  maxPoint, maxVal = maximize_obj_fun(f, [intersection1, 
                                          intersection2, 
                                          intersection3])

  print("Max Point", maxPoint)
  print("Max Value", maxVal)
  

if __name__ == '__main__':
  opt_prob_1a()
  opt_prob_1b()
  opt_prob_1c()