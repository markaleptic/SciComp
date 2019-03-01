from var import var
from const import const
from pwr import pwr
from prod import prod
from plus import plus
from maker import make_const, make_pwr, make_pwr_expr
from tof import tof, const_tof, pwr_tof, prod_tof, plus_tof
from deriv import deriv, const_deriv, prod_deriv, pwr_deriv, var_deriv, plus_deriv
from graphdrv import graph_drv
import math



########################
#  ASSIGNMENT TESTING  #
########################
# TODO convert into unittests

# Example 1
fex = make_pwr("x", 1.0)
print(fex)
drv = deriv(fex)
print(drv)

# Example 2
fex = make_pwr('z', 5)
print(fex)
drv = deriv(fex)
print(drv)

# Example 3
fex = make_pwr_expr(make_pwr('x', 2.0), 2.0)
print(fex)
drv = deriv(fex)
print(drv)

# Example 4
fex = prod(mult1=make_const(5.0), mult2=make_pwr('x', 2.0))
drv = deriv(fex)
print(drv)

# Example 5
fex = prod(mult1=make_pwr('x', 2.0), mult2=make_const(5.0))
drv = deriv(fex)
print(drv)

# Example 6
prd = prod(mult1=make_const(5.0),
               mult2=make_pwr('x', 10.0))
fex = make_pwr_expr(prd, 4.0)
drv = deriv(fex)
print(drv)

# Example 7
fex = make_pwr_expr(plus(elt1=make_pwr('x', 3.0),
                             elt2=make_const(3.0)), 4.0)
drv = deriv(fex)
print(drv)

# Example 8
fex = plus(elt1 = make_pwr('x', 2.0), 
           elt2 = plus(elt1 = make_pwr('x', 1.0),
                       elt2 = make_const(-100.0)))
drv = deriv(fex)
print(drv)

# Example 9
fex = plus(elt1 = make_pwr('x', 2.0), 
           elt2 = plus(elt1 = make_pwr('x', 1.0), 
                        elt2 = make_const(-100.0)))
tf = tof(fex)

poop = lambda x: x**2.0 + x - 100.0
for i in range(1000):
    assert poop(i) == tf(i)
print("Test passes")


# Example 10
fex = prod(mult1=make_const(5.0), mult2=make_pwr('x', 2.0))
f = lambda x: 5.0*(x**2.0)
tf = tof(fex)
def test():
    for i in range(1000):
        assert f(i) == tf(i)
    print('test passed')
test()

# Example 11
prd = prod(mult1=make_const(2.0),
           mult2=make_pwr('x', 5.0))
graph_drv(prd, [-3.0, 3.0], [-50.0, 50.0])

# Example 12
fex1 = make_pwr('x', 4.0)
fex2 = make_pwr('x', 3.0)
fex3 = make_pwr('x', 1.0)
fex4 = plus(elt1=fex1, elt2=fex2)
fex5 = plus(elt1=fex4, elt2=fex3)
graph_drv(fex5, [-2.5, 2.5], [-10.0, 10.0])