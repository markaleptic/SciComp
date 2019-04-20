#!/usr/bin/python

###################################
# module: linprog.py
# YOUR NAME
# YOUR A#
###################################

## your imports
'''
from line_eq import line_eq
from maker import make_line_eq
from maker import make_var, make_const, make_prod
from maker import make_pwr, make_plus
from maker import make_point2d
from const import const
from var import var
from prod import prod
from pwr import pwr
from poly12 import is_pwr_1
from plus import plus
from tof import tof
import sys
'''


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
  ## your code here
  pass
    
### a few tests

def test_01():
  ln1 = make_line_eq(make_var('y'), make_const(1.0))
  ln2 = make_line_eq(make_var('x'), make_const(1.0))
  assert is_const_line(ln1)
  assert is_const_line(ln2)
  print(line_intersection(ln1, ln2))

def test_02():
  ln1 = make_line_eq(make_var('y'), make_const(2.0))
  ln2 = make_line_eq(make_var('y'), make_plus(make_pwr('x', 1.0),
                                              make_const(-6.0)))
  print(line_intersection(ln1, ln2))
  print(line_intersection(ln2, ln1))

def test_03():
  ln1 = make_line_eq(make_var('y'), make_const(-2.0))
  ln2 = make_line_eq(make_var('y'), make_plus(make_pwr('x', 1.0),
                                              make_const(10.0)))
  print(line_intersection(ln1, ln2))
  print(line_intersection(ln2, ln1))

def test_04():
  ln1 = make_line_eq(make_var('y'), make_const(2.0))
  ln2 = make_line_eq(make_var('y'), make_plus(make_prod(make_const(2.0),
                                                        make_pwr('x', 1.0)),
                                              make_const(-6.0)))
  print(line_intersection(ln1, ln2))
  print(line_intersection(ln2, ln1))

def test_05():
  ln1 = make_line_eq(make_var('y'), make_pwr('x', 1.0))
  ln2 = make_line_eq(make_var('y'), make_prod(make_const(2.0),
                                              make_pwr('x', 1.0)))
  ln3 = make_line_eq(make_var('y'), make_plus(make_prod(make_const(3.0),
                                                        make_pwr('x', 1.0)),
                                              make_const(-10.0)))
  print(get_line_coeffs(ln1))
  print(get_line_coeffs(ln2))
  print(get_line_coeffs(ln3))

def test_06():
  ln1 = make_line_eq(make_var('y'), make_pwr('x', 1.0))
  ln2 = make_line_eq(make_var('y'), make_plus(make_prod(make_const(-1.0),
                                                        make_pwr('x', 1.0)),
                                              make_const(6.0)))
  print(line_intersection(ln1, ln2))

def test_07():
  ln1 = make_line_eq(make_var('y'), make_plus(make_prod(make_const(-1.0/5.0),
                                                        make_pwr('x', 1.0)),
                                              make_const(10.0)))
  ln2 = make_line_eq(make_var('y'), make_plus(make_prod(make_const(1.0/5.0),
                                                        make_pwr('x', 1.0)),
                                              make_const(5.0)))
  print(line_intersection(ln1, ln2))

def test_08():
  ln1 = make_line_eq(make_var('y'), make_const(1.0))
  ln2 = make_line_eq(make_var('y'), make_plus(make_prod(make_const(-1.0),
                                                        make_pwr('x', 1.0)),
                                              make_const(6.0)))
  print(line_intersection(ln1, ln2))

def test_09():
  ln1 = make_line_eq(make_var('y'), make_const(5.0))
  ln2 = make_line_eq(make_var('y'), make_plus(make_prod(make_const(-1.0),
                                                        make_pwr('x', 1.0)),
                                              make_const(6.0)))
  print(line_intersection(ln1, ln2))

def maximize_obj_fun(f, corner_points):
  ## your code here
  pass

def minimize_obj_fun(f, corner_points):
  ## your code here
  pass

def test_10():
  f1 = lambda x, y: 2*x + y
  corner_points = [make_point2d(1, 1),
                   make_point2d(1, 5),
                   make_point2d(5, 1)]
  print(maximize_obj_fun(f1, corner_points))              
  f2 = lambda x, y: x - 2*y
  print(minimize_obj_fun(f2, corner_points))
  
### more tests

def test_11():
  ln1 = make_line_eq(make_var('x'), make_const(1.0))
  ln2 = make_line_eq(make_var('y'), make_prod(make_const(0.5),
                                             make_pwr('x', 1.0)))
  print(line_intersection(ln1, ln2))
  ln3 = make_line_eq(make_var('y'), make_plus(make_prod(make_const(-3.0/4),
                                                        make_pwr('x', 1.0)),
                                              make_const(3.0)))
  print(line_intersection(ln1, ln3))
  print(line_intersection(ln2, ln3))


def test_12():
  ln1 = make_line_eq(make_var('x'), make_const(0.0))
  ln2 = make_line_eq(make_var('y'), make_const(0.0))
  ln3 = make_line_eq(make_var('y'), make_plus(make_prod(make_const(-4.0/3),
                                                        make_pwr('x', 1.0)),
                                              make_const(160.0)))
  ln4 = make_line_eq(make_var('y'), make_plus(make_prod(make_const(-0.5),
                                                        make_pwr('x', 1.0)),
                                              make_const(120.0)))
  print(ln1)
  print(ln3)
  print(line_intersection(ln1, ln3))
  print(ln2)
  print(ln3)
  print(line_intersection(ln2, ln3))
  print(line_intersection(ln3, ln4))

## write your answer to problem 1a as x, y, mv
def opt_prob_1a():
  ## your code here
  pass

## write your answer to problem 1b as x, y, mv
def opt_prob_1b():
  ## your code here
  pass

## write your answer to problem 1c as x, y, mv
def opt_prob_1c():
  ## your code here
  pass
  

                                              
  
  


