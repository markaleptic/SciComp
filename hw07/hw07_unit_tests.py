#!/usr/bin/python
# -*- coding: utf-8 -*-

#############################################################
# module: unit_tests.py
# description: unit tests for CS 3430: S19: Assignment 01
# bugs to vladimir kulyukin via canvas
##############################################################

import unittest
import math
from prod import prod
from plus import plus
from quot import quot
from const import const
from maker import make_const, make_pwr, make_const, make_plus
from maker import make_prod, make_pwr_expr, make_quot, make_e_expr
from maker import make_ln, make_absv, make_var
from tof import tof
from deriv import deriv
from deriv import logdiff
from poly12 import find_poly_1_zeros, find_poly_2_zeros
from derivtest import loc_xtrm_1st_drv_test
from derivtest import loc_xtrm_2nd_drv_test
from infl import find_infl_pnts
from antideriv import antideriv


class LogicTests(unittest.TestCase):
    def test_make_var_pass_to_make_pwr(self):
        varExpr = make_var('x')
        pwrExpr = make_pwr('x', 1.0)
        assert str(varExpr) == str(pwrExpr)

    def runTest(self):
        pass


class Assign01UnitTests(unittest.TestCase):
    def test_assgn_01_ut_01(self):
        print('\n***** Assign 01: Unit Test 01 ************')
        fex = prod(mult1=make_const(6.0),
                   mult2=make_pwr('x', 3.0))
        drv = deriv(fex)
        assert not drv is None
        drvf = tof(drv)
        assert not drvf is None
        gt = lambda x: 18*(x**2)
        err = 0.00001
        for i in range(1, 100):
            assert abs(drvf(i) - gt(i)) <= err
        print('Assign 01: Unit Test 01: pass')

    def test_assgn_01_ut_02(self):
        print('\n***** Assign 01: Unit Test 02 ************')
        fex = prod(mult1=make_const(3.0),
                   mult2=make_pwr('x', 1.0/3.0))
        drv = deriv(fex)
        assert not drv is None
        drvf = tof(drv)
        assert not drvf is None
        gt = lambda x: (x**(-2.0/3.0))
        err = 0.00001
        for i in range(1, 100):
            assert abs(drvf(i) - gt(i)) <= err
        print('Assign 01: Unit Test 02: pass')

    def test_assgn_01_ut_03(self):
        print('\n***** Assign 01: Unit Test 03 ************')
        prd = prod(mult1=make_const(2.0), mult2=make_pwr('x', 5.0))
        drv = deriv(prd)
        assert not drv is None
        drvf = tof(drv)
        assert not drvf is None
        gt = lambda x: 10*x**4
        err = 0.00001
        for i in range(-100, 100):
            assert abs(drvf(i) - gt(i)) <= err
        print('Assign 01: Unit Test 03: pass')

    def test_assgn_01_ut_04(self):
        print('\n***** Assign 01: Unit Test 04 ************')
        prd = prod(mult1=make_const(-3.0), mult2=make_pwr('x', -1.0))
        drv = deriv(prd)
        assert not drv is None
        drvf = tof(drv)
        assert not drvf is None
        gt = lambda x: 3.0*(x**(-2))
        err = 0.00001
        for i in range(-100, 0):
            assert abs(drvf(i) - gt(i)) <= err
        for i in range(1, 100):
            assert abs(drvf(i) - gt(i)) <= err
        print('Assign 01: Unit Test 04: pass')

    def test_assgn_01_ut_05(self):
        print('\n***** Assign 01: Unit Test 05 ************')
        fex1 = make_pwr('x', 3.0)
        fex2 = prod(mult1=make_const(5.0),
                    mult2=make_pwr('x', 1.0))
        p = plus(elt1=fex1, elt2=fex2)
        drv = deriv(p)
        assert not drv is None
        drvf = tof(drv)
        assert not drvf is None
        gt = lambda x: 3.0*(x**2) + 5.0
        err = 0.00001
        for i in range(-100, 100):
            assert abs(drvf(i) - gt(i)) <= err
        print('Assign 01: Unit Test 05: pass')

    def test_assgn_01_ut_06(self):
        print('\n***** Assign 01: Unit Test 06 ************')
        fex1 = prod(mult1=make_const(2.0),
                    mult2=make_pwr('x', 7.0))
        fex2 = plus(elt1=prod(mult1=make_const(-1.0),
                              mult2=make_pwr('x', 5.0)),
                    elt2=make_const(8.0))
        p = plus(elt1=fex1, elt2=fex2)
        drv = deriv(p)
        assert not drv is None
        drvf = tof(drv)
        assert not drvf is None
        gt = lambda x: 14.0*(x**6) - 5.0*(x**4)
        err = 0.00001 
        for i in range(-100, -1):
            assert abs(drvf(i) - gt(i)) <= err
        for i in range(1, 100):
            assert abs(drvf(i) - gt(i)) <= err
        print('Assign 01: Unit Test 06: pass')

    def runTest(self):
        pass

class Assign02UnitTests(unittest.TestCase):

    def test_assgn_02_ut_01(self):
        print('\n***** Assign 02: Problem 01: Unit Test 01 *****')
        f1 = make_prod(make_const(2.0),
                       make_pwr('x', 1.0))
        f2 = make_plus(f1, make_const(5.0))
        print(f2)
        z = find_poly_1_zeros(f2)
        print(z)
        f2f = tof(f2)
        err = 0.0001
        assert abs(f2f(z.get_val()) - 0.0) <= err 
        print('Assign 02: Problem 01: Unit Test 01: pass')

    def test_assgn_02_ut_02(self):
        print('\n***** Assign 02: Unit Test 02 *****')
        f1 = make_prod(make_const(3.0),
                       make_pwr('x', 1.0))
        f2 = make_plus(f1, make_const(100.0))
        print(f2)
        z = find_poly_1_zeros(f2)
        print(z)
        f2f = tof(f2)
        err = 0.0001
        assert abs(f2f(z.get_val()) - 0.0) <= err 
        print('Assign 02: Problem 01: Unit Test 02: pass')

    def test_assgn_02_ut_03(self):
        print('\n***** Assign 02: Problem 01: Unit Test 03 *****')
        f1 = make_prod(make_const(25.0),
                       make_pwr('x', 1.0))
        f2 = make_plus(f1, make_const(-1027.0))
        print(f2)
        z = find_poly_1_zeros(f2)
        print(z)
        f2f = tof(f2)
        err = 0.0001
        assert abs(f2f(z.get_val()) - 0.0) <= err 
        print('Assign 02: Problem 01: Unit Test 03: pass')

    def test_assgn_02_ut_04(self):
        print('\n***** Assign 02: Problem 01: Unit Test 04 *****')
        f0 = make_prod(make_const(0.5), make_pwr('x', 2.0))
        f1 = make_prod(make_const(6.0), make_pwr('x', 1.0))
        f2 = make_plus(f0, f1)
        poly = make_plus(f2, make_const(0.0))
        print(poly)
        zeros = find_poly_2_zeros(poly)
        for z in zeros:
            print(z)
        pf = tof(poly)
        err = 0.0001
        for z in zeros:
            assert abs(pf(z.get_val()) - 0.0) <= err 
        print('Assign 02: Problem 01: Unit Test 04: pass')

    def test_assgn_02_ut_05(self):
        print('\n***** Assign 02: Problem 01: Unit Test 05 *****')
        f0 = make_pwr('x', 2.0)
        f1 = make_pwr('x', 1.0)
        f2 = make_plus(f0, f1)
        poly = make_plus(f2, make_const(-4.0))
        print(poly)
        zeros = find_poly_2_zeros(poly)
        for z in zeros:
            print(z)
        pf = tof(poly)
        err = 0.0001
        for z in zeros:
            assert abs(pf(z.get_val()) - 0.0) <= err 
        print('Assign 02: Problem 01: Unit Test 05: pass')

    def test_assgn_02_ut_06(self):
        print('\n***** Assign 02: Problem 01: Unit Test 06 *****')
        f0 = make_pwr('x', 2.0)
        f1 = make_prod(make_const(-3.0), make_pwr('x', 1.0))
        f2 = make_plus(f0, f1)
        poly = make_plus(f2, make_const(-4.0))
        print(poly)
        zeros = find_poly_2_zeros(poly)
        for z in zeros:
            print(z)
        pf = tof(poly)
        err = 0.0001
        for z in zeros:
            assert abs(pf(z.get_val()) - 0.0) <= err 
        print('Assign 02: Problem 01: Unit Test 06: pass')

    def test_assgn_02_ut_07(self):
        print('\n***** Assign 02: Problem 01: Unit Test 07 *****')
        f0 = make_pwr('x', 2.0)
        f1 = make_prod(make_const(0.0), make_pwr('x', 1.0))
        f2 = make_plus(f0, f1)
        poly = make_plus(f2, make_const(-4.0))
        print(poly)
        zeros = find_poly_2_zeros(poly)
        for z in zeros:
            print(z)
        pf = tof(poly)
        err = 0.0001
        for z in zeros:
            assert abs(pf(z.get_val()) - 0.0) <= err 
        print('Assign 02: Problem 01: Unit Test 07: pass')

    def test_assgn_02_ut_08(self):
        print('\n***** Assign 02: Problem 01: Unit Test 08 *****')
        f0 = make_prod(make_const(6.0), make_pwr('x', 2.0))
        f1 = make_prod(make_const(11.0), make_pwr('x', 1.0))
        f2 = make_plus(f0, f1)
        poly = make_plus(f2, make_const(-35.0))
        print(poly)
        zeros = find_poly_2_zeros(poly)
        for z in zeros:
            print(z)
        pf = tof(poly)
        err = 0.0001
        for z in zeros:
            assert abs(pf(z.get_val()) - 0.0) <= err 
        print('Assign 02: Problem 01: Unit Test 08: pass')

    def test_assgn_02_ut_09(self):
        print('\n***** Assign 02: Problem 01: Unit Test 09 ************')
        f0 = make_pwr('x', 2.0)
        f1 = make_prod(make_const(0.0), make_pwr('x', 1.0))
        f2 = make_plus(f0, f1)
        poly = make_plus(f2, make_const(-48.0))
        print(poly)
        zeros = find_poly_2_zeros(poly)
        for z in zeros:
            print(z)
        pf = tof(poly)
        err = 0.0001
        for z in zeros:
            assert abs(pf(z.get_val()) - 0.0) <= err 
        print('Assign 02: Problem 01: Unit Test 09: pass')

    def test_assgn_02_ut_11(self):
        print('\n***** Assign 02: Problem 02: Unit Test 01 *****')
        f1 = make_prod(make_const(1.0/3.0), make_pwr('x', 3.0))
        f2 = make_prod(make_const(-2.0), make_pwr('x', 2.0))
        f3 = make_prod(make_const(3.0), make_pwr('x', 1.0))
        f4 = make_plus(f1, f2)
        f5 = make_plus(f4, f3)
        poly = make_plus(f5, make_const(1.0))
        print(poly)
        xtrma = loc_xtrm_1st_drv_test(poly)
        assert len(xtrma) == 2
        err = 0.0001
        for i, j in xtrma:
            print(i, str(j))
            if i == 'max':
                assert abs(j.get_x().get_val() - 1.0) <= err
                assert abs(j.get_y().get_val() - 2.33333333333) <= err
            if i == 'min':
                assert abs(j.get_x().get_val() - 3.0) <= err
                assert abs(j.get_y().get_val() - 1.0) <= err
        print('Assign 02: Problem 02: Unit Test 01: pass')

    def test_assgn_02_ut_12(self):
        print('\n***** Assign 02: Problem 02: Unit Test 02 *****')
        f1 = make_prod(make_const(27.0), make_pwr('x', 3.0))
        f2 = make_prod(make_const(-27.0), make_pwr('x', 2.0))
        f3 = make_prod(make_const(9.0), make_pwr('x', 1.0))
        f4 = make_plus(f1, f2)
        f5 = make_plus(f4, f3)
        f6 = make_plus(f5, make_const(-1.0))
        print(f6)
        xtrma = loc_xtrm_1st_drv_test(f6)
        assert xtrma is None 
        print('Assign 02: Problem 02: Unit Test 02: pass')

    def test_assgn_02_ut_13(self):
        print('\n***** Assign 02: Problem 02: Unit Test 03 *****')
        f1 = make_prod(make_const(1.0/4.0), make_pwr('x', 2.0))
        f2 = make_prod(make_const(-1.0), make_pwr('x', 1.0))
        f3 = make_plus(f1, f2)
        f4 = make_plus(f3, make_const(2.0))
        print(f4)
        xtrma = loc_xtrm_2nd_drv_test(f4)
        assert len(xtrma) == 1
        err = 0.0001
        for i, j in xtrma:
            print(i, str(j))
            if i == 'min':
                assert abs(j.get_x().get_val() - 2.0) <= err
                assert abs(j.get_y().get_val() - 1.0) <= err
        print('Assign 02: Problem 02: Unit Test 03: pass')

    def test_assgn_02_ut_14(self):
        print('\n***** Assign 02: Problem 02: Unit Test 04 *****')
        f1 = make_pwr('x', 3.0)
        f2 = make_prod(make_const(-3.0), make_pwr('x', 2.0))
        f3 = make_plus(f1, f2)
        f4 = make_plus(f3, make_const(5.0))
        print(f4)
        xtrma = loc_xtrm_2nd_drv_test(f4)
        assert len(xtrma) == 2
        err = 0.0001
        for i, j in xtrma:
            print(i, str(j))
            if i == 'max':
                assert abs(j.get_x().get_val() - 0.0) <= err
                assert abs(j.get_y().get_val() - 5.0) <= err
            if i == 'min':
                assert abs(j.get_x().get_val() - 2.0) <= err
                assert abs(j.get_y().get_val() - 1.0) <= err
        print('Assign 02: Problem 02: Unit Test 04: pass')

    def test_assgn_02_ut_15(self):
        print('\n***** Assign 02: Problem 02: Unit Test 05 *****')
        f1 = make_pwr('x', 3.0)
        f2 = make_prod(make_const(-27.0), make_pwr('x', 1.0))
        f3 = make_plus(f1, f2)
        f4 = make_plus(f3, make_const(0.0))
        print(f4)
        xtrma = loc_xtrm_2nd_drv_test(f4)
        assert len(xtrma) == 2
        err = 0.0001
        for i, j in xtrma:
            print(i, str(j))
            if i == 'max':
                assert abs(j.get_x().get_val() + 3.0) <= err
                assert abs(j.get_y().get_val() - 54.0) <= err
            if i == 'min':
                assert abs(j.get_x().get_val() - 3.0) <= err
                assert abs(j.get_y().get_val() + 54.0) <= err
        print('Assign 02: Problem 02: Unit Test 04: pass')

    def test_assgn_02_ut_16(self):
        print('\n***** Assign 02: Problem 03: Unit Test 01 *****')
        f1 = make_pwr('x', 3.0)
        f2 = make_prod(make_const(-3.0), make_pwr('x', 2.0))
        f3 = make_prod(make_const(0.0), make_pwr('x', 0.0))
        f4 = make_plus(f1, f2)
        f5 = make_plus(f4, f3)
        f6 = make_plus(f5, make_const(5.0))
        print(f6)
        ips = find_infl_pnts(f6)
        err = 0.0001
        assert len(ips) == 1
        ip = ips[0]
        assert abs(ip.get_x().get_val() - 1.0) <= err
        assert abs(ip.get_y().get_val() - 3.0) <= err
        print('Assign 02: Problem 03: Unit Test 01: pass')

    def test_assgn_02_ut_16b(self):
        print('\n***** Assign 02: Problem 03: Unit Test 02 *****')
        f1 = make_pwr('x', 3.0)
        f2 = make_prod(make_const(-3.0),
                       make_pwr('x', 1.0))
        f3 = make_plus(f1, f2)
        f4 = make_plus(f3, make_const(2.0))
        inflps = find_infl_pnts(f4)
        assert len(inflps) == 1
        ip = inflps[0]
        assert ip.get_x().get_val() == 0.0
        assert ip.get_y().get_val() == 2.0
        for ip in inflps:
            print(str(ip))
        print('Assign 02: Problem 03: Unit Test 02: pass')

    def test_assgn_02_ut_17(self):
        print('\n***** Assign 02: Problem 03: Unit Test 03 *****')
        f1 = make_prod(make_const(-1.0),
                       make_pwr('x', 3.0))
        f2 = make_prod(make_const(3.0),
                       make_pwr('x', 2.0))
        f3 = make_plus(f1, f2)
        f4 = make_plus(f3, make_const(1.0))
        inflps = find_infl_pnts(f4)
        assert len(inflps) == 1
        ip = inflps[0]
        assert ip.get_x().get_val() == 1.0
        assert ip.get_y().get_val() == 3.0
        for ip in inflps:
            print(str(ip))
        print('Assign 02: Problem 03: Unit Test 03: pass')

    def runTest(self):
        pass


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

#     def test_max_rev(self):
#         print('\n***** Max Revenue Test ************')
#         e1 = make_prod(make_const(1.0/12.0), make_pwr('x', 2.0))
#         e2 = make_prod(make_const(-10.0), make_pwr('x', 1.0))
#         sum1 = make_plus(e1, e2)
#         dmndf_expr = make_plus(sum1, make_const(300.0))
#         num_units, rev, price = maximize_revenue(dmndf_expr, constraint=lambda x: 0 <= x <= 60)
#         print('x = ', num_units.get_val())
#         print('rev = ', rev.get_val())
#         print('price = ', price.get_val())
#         print('Max Revenue Test: pass')
    
#     def test_oil_disk(self):
#         print('\n***** Implicit Differentiation Test 01 ************')
#         yt = make_prod(make_const(0.02 * math.pi),
#             make_pwr('r', 2.0))
#         print(yt)
#         dydt = dydt_given_x_dxdt(yt, make_const(150.0),
#                                 make_const(20.0))
#         assert not dydt is None
#         assert isinstance(dydt, const)
#         print(dydt)
#         print('Implicit Differentiation Test 01: pass')

#     def test_arm_tumor(self):
#         print('\n***** Implicit Differentiation Test 02 ************')
#         yt = make_prod(make_const(0.003 * math.pi),
#                     make_pwr('r', 3.0))
#         print(yt)
#         dydt = dydt_given_x_dxdt(yt, make_const(10.3), make_const(-1.75))
#         assert not dydt is None
#         assert isinstance(dydt, const)
#         print(dydt)
#         print('Implicit Differentiation Test 02: pass')

    def runTest(self):
        pass


class Assign04UnitTests(unittest.TestCase):
    def test_01(self):
        print('\n***** Test 01 ************')
        fex = make_e_expr(make_prod(make_const(5.0),
                                    make_pwr('x', 1.0)))
        print(fex)
        drv = deriv(fex)
        assert not drv is None
        print(drv)
        drvf = tof(drv)
        assert not drvf is None
        gt = lambda x: 5.0*(math.e**(5.0*x))
        for i in range(10):
            print(drvf(i), gt(i))
            assert abs(gt(i) - drvf(i)) <= 0.001
        print('Test 01: pass')

    def test_02(self):
        print('\n***** Test 02 ************')
        fex = make_e_expr(make_plus(make_pwr('x', 2.0),
                                    make_const(-1.0)))
        print(fex)
        drv = deriv(fex)
        assert not drv is None
        print(drv)
        drvf = tof(drv)
        assert not drvf is None
        gt = lambda x: 2*x*(math.e**(x**2 - 1.0))
        err = 0.0001
        for i in range(10):
            print(drvf(i), gt(i))
            assert abs(gt(i) - drvf(i)) <= err
        print('Test 02: pass')


    def test_03(self):
        print('\n***** Test 03 ************')
        fex1 = make_quot(make_const(-1.0), make_pwr('x', 1.0))
        fex2 = make_e_expr(make_plus(make_pwr('x', 1.0), fex1))
        print(fex2)
        drv = deriv(fex2)
        assert not drv is None
        print(drv)
        drvf = tof(drv)
        assert not drvf is None
        def gt_drvf(x):
            d = (x - 1.0/x)
            return (math.e**d)*(1.0 + 1.0/(x**2))
        err = 0.0001
        for i in range(1, 10):
            print(drvf(i), gt_drvf(i))
            assert abs(gt_drvf(i) - drvf(i)) <= err
        print('Test 03: pass')
    

    def test_04(self):
        print('\n***** Test 04 ************')
        n = make_prod(make_const(3.0),
                    make_e_expr(make_prod(make_const(2.0),
                                            make_pwr('x', 1.0))))
        d = make_plus(make_const(1.0), make_pwr('x', 2.0))
        fex = make_quot(n, d)
        print(fex)
        drv = deriv(fex)
        assert not drv is None
        print(drv)
        drvf = tof(drv)
        assert not drvf is None
        def gt_drvf(x):
            n = 6.0*(math.e**(2.0*x))*(x**2 - x + 1.0)
            d = (1 + x**2)**2
            return n/d
        for i in range(-10, 10):
            print (drvf(i), gt_drvf(i))
            assert abs(gt_drvf(i) - drvf(i)) <= 0.001
        print('Test 04: pass')


    def test_05(self):
        print('\n***** Test 05 ************')
        fex = make_pwr_expr(make_ln(make_pwr('x', 1.0)), 5.0)
        print(fex)
        drv = deriv(fex)
        assert not drv is None
        print(drv)
        drvf = tof(drv)
        assert not drvf is None
        gt = lambda x: (5.0*(math.log(x, math.e)**4))/x
        err = 0.0001
        for i in range(1, 5):
            print(drvf(i), gt(i))
            assert abs(gt(i) - drvf(i)) <= err
        print('Test 05: pass')

    
    def test_06(self):
        print('\n***** Test 06 ************')
        fex = make_prod(make_pwr('x', 1.0),
                        make_ln(make_pwr('x', 1.0)))
        print(fex)
        drv = deriv(fex)
        assert not drv is None
        print(drv)
        drvf = tof(drv)
        assert not drvf is None
        gt = lambda x: 1.0 + math.log(x, math.e)
        err = 0.0001
        for i in range(1, 10):
            print(drvf(i), gt(i))
        assert abs(gt(i) - drvf(i)) <= err
        print('Test 06: pass')


    def test_07(self):
        print('\n***** Test 07 ************')
        fex0 = make_prod(make_pwr('x', 1.0),
                        make_e_expr(make_pwr('x', 1.0)))
        fex = make_ln(fex0)
        print(fex)
        drv = deriv(fex)
        assert not drv is None
        print(drv)
        drvf = tof(drv)
        assert not drvf is None
        gt = lambda x: (x + 1.0)/x
        err = 0.0001
        for i in range(1, 10):
            print(drvf(i), gt(i))
            assert abs(gt(i) - drvf(i)) <= err
        for i in range(-10, -1):
            print(drvf(i), gt(i))
            assert abs(gt(i) - drvf(i)) <= 0.001
        print('Test 07: pass')



    def test_08(self):
        print('\n***** Test 08 ************')
        fex = make_ln(make_absv(make_pwr('x', 1.0)))
        print(fex)
        drv = deriv(fex)
        assert not drv is None
        print(drv)
        drvf = tof(drv)
        assert not drvf is None
        gt = lambda x: 1.0/x
        err = 0.0001
        for i in range(1, 10):
            print(drvf(i), gt(i))
            assert abs(gt(i) - drvf(i)) <= err
        print('Test 08: pass')


    def test_09(self):
        print('\n***** Test 09 ************')
        fex = make_prod(make_pwr('x', 1.0),
                        make_prod(make_plus(make_pwr('x', 1.0),
                                            make_const(1.0)),
                                make_plus(make_pwr('x', 1.0),
                                            make_const(2.0))))
        drv = logdiff(fex)
        assert not drv is None
        print(drv)
        drvf = tof(drv)
        assert not drvf is None
        def gt_drvf(x):
                z = x*(x + 1.0)*(x + 2.0)
                z2 = (1.0/x + 1.0/(x + 1.0) + 1.0/(x + 2.0))
                return z * z2
        err = 0.0001
        for i in range(1, 10):
            print(drvf(i), gt_drvf(i))
            assert abs(gt_drvf(i) - drvf(i)) <= err
        for i in range(-10, -1):
            if i == -1 or i == -2:
                continue
            print(drvf(i), gt_drvf(i))
            assert abs(gt_drvf(i) - drvf(i)) <= err
        print('Test 09: pass')


    def test_10(self):
        print('\n***** Test 10 ************')
        fex1 = make_plus(make_pwr('x', 2.0), make_const(1.0))
        fex2 = make_plus(make_pwr('x', 3.0), make_const(-3.0))
        fex3 = make_plus(make_prod(make_const(2.0),
                                make_pwr('x', 1.0)),
                        make_const(5.0))
        fex = make_prod(fex1, make_prod(fex2, fex3))
        print(fex)
        drv = logdiff(fex)
        assert not drv is None
        print(drv)
        drvf = tof(drv)
        assert not drvf is None
        def gt_drvf(x):
            z = (x**2 + 1.0)*(x**3 - 3.0)*(2*x + 5.0)
            z2 = ((2.0*x)/(x**2 + 1) + (3.0*(x**2))/(x**3 - 3.0) \
                + 2.0/(2*x + 5.0))
            return z * z2
        for i in range(1, 10):
            print(drvf(i), gt_drvf(i))
            assert abs(gt_drvf(i) - drvf(i)) <= 0.001
        print('Test 10: pass')


    def test_11(self):
        print('\n***** Test 11 ************')
        fex1 = make_pwr_expr(make_plus(make_pwr('x', 1.0),
                                    make_const(1.0)),
                            4.0)
        fex2 = make_pwr_expr(make_plus(make_prod(make_const(4.0),
                                                 make_pwr('x', 1.0)),
                                       make_const(-1.0)),
                        2.0)
        fex = make_prod(fex1, fex2)
        print(fex)
        drv = logdiff(fex)
        assert not drv is None
        print(drv)
        drvf = tof(drv)
        def gt_drvf(x):
                z1 = ((x + 1.0)**4.0) * ((4*x - 1.0)**2.0)
                z2 = (4.0/(x + 1.0)) + ( 8.0/(4*x - 1.0))
                return z1 * z2
        for i in range(0, 20):
            print(drvf(i), gt_drvf(i))
            assert abs(gt_drvf(i) - drvf(i)) <= 0.001
        print('Test 11: pass')

        
    def runTest(self):
        pass


class Assign07UnitTests(unittest.TestCase):
    def test_01(self):
        print('\n***** Test 01 ***********')
        fex = make_pwr('x', 2.0)
        print(fex)
        afex = antideriv(fex)
        assert not afex is None
        def gt(x): return (1.0/3.0)*(x**3.0)
        afexf = tof(afex)
        assert not afexf is None
        err = 0.0001
        for i in range(1, 101):
            assert abs(afexf(i) - gt(i)) <= err
        print(afex)
        print('Test 01: pass')


    def test_02(self):
        print('\n***** Test 02 ***********')
        fex = make_e_expr(make_prod(make_const(-2.0),
                                    make_pwr('x', 1.0)))
        print(fex)
        afex = antideriv(fex)
        assert not afex is None
        def gt(x): return (-0.5)*(math.e**(-2.0*x))
        afexf = tof(afex)
        assert not afexf is None
        err = 0.0001
        for i in range(0, 101):
            assert abs(afexf(i) - gt(i)) <= err
        print(afex)
        print('Test 02: pass')


    def test_03(self):
        print('\n***** Test 03 ***********')
        fex = make_pwr('x', 0.5)
        print(fex)
        afex = antideriv(fex)
        assert not afex is None
        def gt(x): return (2.0/3.0)*(x**(3.0/2.0))
        afexf = tof(afex)
        assert not afexf is None
        err = 0.0001
        for i in range(1, 101):
            assert abs(afexf(i) - gt(i)) <= err
        print(afex)
        print('Test 03: pass')


    def test_04(self):
        print('\n***** Test 04 ***********')
        fex = make_pwr('x', -2.0)
        print(fex)
        afex = antideriv(fex)
        assert not afex is None
        def gt(x): return -1.0/x
        afexf = tof(afex)
        assert not afexf is None
        err = 0.0001
        for i in range(1, 101):
            assert abs(afexf(i) - gt(i)) <= err
        print(afex)
        print('Test 04: pass')


    def test_05(self):
        print('\n***** Test 05 ***********')
        fex = make_pwr('x', -1.0)
        print(fex)
        afex = antideriv(fex)
        assert not afex is None
        afexf = tof(afex)
        assert not afexf is None
        def gt(x): return math.log(abs(x), math.e)
        err = 0.0001
        for i in range(1, 101):
            assert abs(afexf(i) - gt(i)) <= err
        for i in range(-100, 0):
            assert abs(afexf(i) - gt(i))
        print('Test 05: pass')


    def test_06(self):
        print('\n***** Test 06 ***********')
        fex1 = make_pwr('x', -3.0)
        fex2 = make_prod(make_const(7.0),
                        make_e_expr(make_prod(make_const(5.0),
                                            make_pwr('x', 1.0))))
        fex3 = make_prod(make_const(4.0),
                        make_pwr('x', -1.0))
        fex4 = make_plus(fex1, fex2)
        fex = make_plus(fex4, fex3)
        print(fex)
        afex = antideriv(fex)
        assert not afex is None
        print(afex)
        def gt(x):
            v1 = -0.5*(x**(-2.0))
            v2 = (7.0/5.0)*(math.e**(5.0*x))
            v3 = 4.0*(math.log(abs(x), math.e))
            return v1 + v2 + v3
        afexf = tof(afex)
        assert not afexf is None
        err = 0.0001
        for i in range(1, 10):
            print(afexf(i), gt(i))
            assert abs(afexf(i) - gt(i)) <= err * gt(i)
        print('Test 06: pass')


    def test_07(self):
        print('\n***** Test 07 ***********')
        fex = make_prod(make_const(4.0), make_pwr('x', 3.0))
        print(fex)
        afex = antideriv(fex)
        assert not afex is None
        print(afex)
        fexf = tof(fex)
        assert not fexf is None
        fex2 = deriv(afex)
        assert not fex2 is None
        print(fex2)
        fex2f = tof(fex2)
        assert not fex2f is None
        err = 0.0001
        for i in range(11):
            assert abs(fexf(i) - fex2f(i)) <= err
        print('Test 07: pass')


    def test_08(self):
        print('\n***** Test 08 ***********')
        fex1 = make_plus(make_prod(make_const(5.0),
                                make_pwr('x', 1.0)),
                        make_const(-7.0))
        fex = make_pwr_expr(fex1, -2.0)
        print(fex)
        afex = antideriv(fex)
        assert not afex is None
        print(afex)
        afexf = tof(afex)
        err = 0.0001
        def gt(x):
            return (-1.0/5.0)*((5*x - 7.0)**-1)
        for i in range(1, 100):
            assert abs(afexf(i) - gt(i)) <= err
        fexf = tof(fex)
        assert not fexf is None
        fex2 = deriv(afex)
        assert not fex2 is None
        print(fex2)
        fex2f = tof(fex2)
        assert not fex2f is None
        for i in range(1, 100):
            assert abs(fexf(i) - fex2f(i)) <= err
        print('Test 08: pass')


    def test_09(self):
        print('\n***** Test 09 ***********')
        fex0 = make_plus(make_pwr('x', 1.0), make_const(2.0))
        fex1 = make_pwr_expr(fex0, -1.0)
        fex = make_prod(make_const(3.0), fex1)
        print(fex)
        afex = antideriv(fex)
        err = 0.0001
        afexf = tof(afex)
        def gt(x):
            return 3.0*math.log(abs(2.0 + x), math.e)
        for i in range(1, 101):
            assert abs(afexf(i) - gt(i)) <= err
        assert not afex is None
        print(afex)
        fexf = tof(fex)
        assert not fexf is None
        fex2 = deriv(afex)
        assert not fex2 is None
        print(fex2)


    def test_10(self):
        print('\n***** Test 10 ***********')
        fex0 = make_prod(make_const(3.0), make_pwr('x', 1.0))
        fex1 = make_plus(fex0, make_const(2.0))
        fex = make_pwr_expr(fex1, 4.0)
        print(fex)
        afex = antideriv(fex)
        assert not afex is None
        print(afex)
        afexf = tof(afex)
        err = 0.0001
        def gt(x):
            return (1.0/15)*((3*x + 2.0)**5)
        for i in range(1, 10):
            assert abs(afexf(i) - gt(i)) <= err
        fexf = tof(fex)
        assert not fexf is None
        fex2 = deriv(afex)
        assert not fex2 is None
        print(fex2)
        fex2f = tof(fex2)
        assert not fex2f is None
        for i in range(1, 1000):
            assert abs(fexf(i) - fex2f(i)) <= err
        print('Test 10: pass')


    def runTest(self):
        pass

if __name__ == '__main__':
    unittest.main()