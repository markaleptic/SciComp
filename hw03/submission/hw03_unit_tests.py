#!/usr/bin/python

#############################################################
# module: hw02_unit_tests.py
# description: unit tests for CS 3430: S19: Assignment 02
# bugs to vladimir kulyukin via canvas
##############################################################

#uncomment the next line if you use Py2
#from __future__ import print_function
import unittest
from prod import prod
from plus import plus
from quot import quot
from const import const
from maker import make_const, make_pwr, make_const, make_plus
from maker import make_prod, make_pwr_expr, make_quot, make_e_expr
from tof import tof
from deriv import deriv
from poly12 import find_poly_1_zeros, find_poly_2_zeros
from derivtest import loc_xtrm_1st_drv_test
from derivtest import loc_xtrm_2nd_drv_test
from hw03 import maximize_revenue
from hw03 import dydt_given_x_dxdt
import math


class Assign03UnitTests(unittest.TestCase):
    def test_assgn_03_q1_t1(self):
        print('\n***** Assign 03: Problem 01: Unit Test 01 *****')
        e1 = make_plus(make_pwr('x', 1.0), make_const(1.0))
        e2 = make_pwr('x', 3.0)
        e3 = make_prod(make_const(5.0), make_pwr('x', 1.0))
        e4 = make_plus(e2, e3)
        e5 = make_plus(e4, make_const(2.0))
        e6 = make_prod(e1, e5)
        # 1) print the expression we just constructed
        print('-- function expression is:\n')
        print(e6)
        # 2) differentiate and make sure that it not None
        drv = deriv(e6)
        assert not drv is None
        print('-- derivative is:\n')
        print(e6)
        # 3) convert drv into a function
        e6f = tof(drv)
        assert not e6f is None
        # steps 2) and 3) can be combined into tof(deriv(e6)).
        # 4) construct the ground truth function
        gt = lambda x: 4.0*(x**3) + 3*(x**2) + 10.0*x + 7.0
        # 5) compare the ground gruth with what we got in
        # step 3) on an appropriate number range.
        print('\n Comparison with ground truth:\n')
        err = 0.00001
        for i in range(10):
            print(e6f(i), gt(i))
            assert abs(e6f(i) - gt(i)) <= err
        print('Assign 03: Problem 01: Unit Test 01: pass')
    
    def test_assgn_03_q1_t2(self):
        print('\n***** Assign 03: Problem 01: Unit Test 02 *****')
        e1 = make_prod(make_const(2.0), make_pwr('x', 4.0))
        e2 = make_prod(make_const(-1.0), make_pwr('x', 1.0))
        e3 = make_plus(e1, e2)
        e4 = make_plus(e3, make_const(1.0))
        e5 = make_prod(make_const(-1.0), make_pwr('x', 5.0))
        e6 = make_plus(e5, make_const(1.0))
        e7 = make_prod(e4, e6)
        print('-- function expression is:\n')
        print(e7)
        drv = deriv(e7)
        assert not drv is None
        print('\n-- derivative is:\n')
        print(drv)
        e7f = tof(drv)
        assert not e7f is None
        gt = lambda x: -18.0*(x**8) + 6.0*(x**5) - 5.0*(x**4) +  8.0*(x**3) - 1.0
        err = 0.00001
        print('\n--comparison with ground truth:\n')
        for i in range(10):
            print(e7f(i), gt(i))
            assert abs(e7f(i) - gt(i)) <= err
        print('Assign 03: Problem 01: Unit Test 02: pass')

    def test_assgn_03_q1_t3(self):
        print('\n***** Assign 03: Problem 01: Unit Test 03 *****')
        q = make_quot(make_plus(make_pwr('x', 1.0),
                                make_const(11.0)),
                    make_plus(make_pwr('x', 1.0), make_const(-3.0)))
        pex = make_pwr_expr(q, 3.0)
        print('-- function expression is:\n')
        print(pex)
        pexdrv = deriv(pex)
        assert not pexdrv is None
        print('\n-- derivative is:\n')
        print(pexdrv)
        pexdrvf = tof(pexdrv)
        assert not pexdrvf is None
        gt = lambda x: -42.0*(((x + 11.0)**2)/((x - 3.0)**4))
        err = 0.001
        print('\n--comparison with ground truth:\n')
        for i in range(10):
            if i != 3.0:
                print(pexdrvf(i), gt(i))
                assert abs(pexdrvf(i) - gt(i)) <= err
        print('Assign 03: Problem 01: Unit Test 03: pass')

    def test_max_rev(self):
        print('\n***** Max Revenue Test ************')
        e1 = make_prod(make_const(1.0/12.0), make_pwr('x', 2.0))
        e2 = make_prod(make_const(-10.0), make_pwr('x', 1.0))
        sum1 = make_plus(e1, e2)
        dmndf_expr = make_plus(sum1, make_const(300.0))
        num_units, rev, price = maximize_revenue(dmndf_expr, constraint=lambda x: 0 <= x <= 60)
        print('x = ', num_units.get_val())
        print('rev = ', rev.get_val())
        print('price = ', price.get_val())
        print('Max Revenue Test: pass')
    
    def test_oil_disk(self):
        print('\n***** Implicit Differentiation Test 01 ************')
        yt = make_prod(make_const(0.02 * math.pi),
            make_pwr('r', 2.0))
        print(yt)
        dydt = dydt_given_x_dxdt(yt, make_const(150.0),
                                make_const(20.0))
        assert not dydt is None
        assert isinstance(dydt, const)
        print(dydt)
        print('Implicit Differentiation Test 01: pass')

    def test_arm_tumor(self):
        print('\n***** Implicit Differentiation Test 02 ************')
        yt = make_prod(make_const(0.003 * math.pi),
                    make_pwr('r', 3.0))
        print(yt)
        dydt = dydt_given_x_dxdt(yt, make_const(10.3), make_const(-1.75))
        assert not dydt is None
        assert isinstance(dydt, const)
        print(dydt)
        print('Implicit Differentiation Test 02: pass')

    def runTest(self):
        pass

if __name__ == '__main__':
    unittest.main()