#!/usr/bin/python
# -*- coding: utf-8 -*-

#############################################################
# module: unit_tests.py
# description: unit tests for CS 3430: S19: Assignment 01
# bugs to vladimir kulyukin via canvas
##############################################################

from __future__ import print_function
import unittest
from prod import prod
from maker import make_const, make_pwr
from plus import plus
from tof import tof
from deriv import deriv
from graphdrv import graph_drv

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

    def test_assgn_01_ut_01(self):
        print('\n***** Assign 01: Unit Test 01 ************')
        prd = prod(mult1=make_const(2.0),
                   mult2=make_pwr('x', 5.0))
        graph_drv(prd, [-3.0, 3.0], [-50, 50.0])
        print('Assign 01: Unit Test 01: pass')

    def test_assgn_01_ut_02(self):
        print('\n***** Assign 01: Unit Test 02 ************')
        fex1 = make_pwr('x', 4.0)
        fex2 = make_pwr('x', 3.0)
        fex3 = make_pwr('x', 1.0)
        fex4 = plus(elt1=fex1, elt2=fex2)
        fex5 = plus(elt1=fex4, elt2=fex3)
        graph_drv(fex5, [-2.5, 2.5], [-10.0, 10.0])
        print('Assign 01: Unit Test 02: pass')

    def test_assgn_01_prob_02_ut_03(self):
        print('\n***** Assign 01: Unit Test 03 ************')
        fex1 = prod(mult1=make_const(-1.0),
                    mult2=make_pwr('x', 2.0))
        fex2 = plus(elt1=fex1, elt2=make_const(2.0))
        graph_drv(fex2, [-10, 10], [-50.0, 25.0])
        print('Assign 01: Unit Test 03: pass')

    def test_assgn_01_prob_02_ut_04(self):
        print('\n***** Assign 01: Unit Test 04 ************')
        fex1 = prod(mult1=make_const(2),
                    mult2=make_pwr('x', 2.0))
        fex2 = plus(elt1=fex1, elt2=make_const(2.0))
        graph_drv(fex2, [-10, 10], [-50.0, 50.0])
        print('Assign 01: Unit Test 04: pass')

    def runTest(self):
        pass

if __name__ == '__main__':
    unittest.main()
