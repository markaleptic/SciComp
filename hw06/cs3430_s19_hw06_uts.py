#!/usr/bin/python

#############################################################
# module: cs3430_s19_hw06_uts.py
# description: unit tests for CS 3430: S19: Assignment 06
# bugs to vladimir kulyukin via canvas
##############################################################

import unittest
import math
from maker import make_const, make_quot, make_pwr, make_plus, make_prod
from tof import tof
from hw06_s19 import percent_retention_model, plot_retention
from hw06_s19 import spread_of_disease_model, plot_spread_of_disease
from hw06_s19 import plant_growth_model, plot_plant_growth
from hw06_s19 import spread_of_news_model, plot_spread_of_news
from deriv import deriv

class Assign06UnitTests(unittest.TestCase):

    ### ************* HW06: Problem 01 UTs *******************************
    def test_assign_06_prob_01_ut_01(self):
        print('\n***** Assign 06: Problem 01: Unit Test 01 *****')
        lmbda, a = make_const(0.5), make_const(15.0)
        tl, tu = make_const(0.0), make_const(50.0)
        prm = percent_retention_model(lmbda, a)
        assert not prm is None
        print(prm)
        prmf = tof(prm)
        assert not prmf is None
        gt = lambda t: 85.0 * (math.e**(-0.5*t)) + 15.0
        err = 0.0001
        for t in range(100):
            assert abs(gt(t) - prmf(t)) <= err
        plot_retention(lmbda, a, tl, tu)
        print('Assign 06: Problem 01: Unit Test 01: pass')

    def test_assign_06_prob_01_ut_02(self):
        print('\n***** Assign 06: Problem 01: Unit Test 02 *****')
        lmbda, a = make_const(0.215), make_const(10.0)
        tl, tu = make_const(0.0), make_const(50.0)
        prm = percent_retention_model(lmbda, a)
        assert not prm is None
        print(prm)
        prmf = tof(prm)
        assert not prmf is None
        gt = lambda t: 90.0 * (math.e**(-0.215*t)) + 10.0
        err = 0.0001
        for t in range(100):
            assert abs(gt(t) - prmf(t)) <= err
        plot_retention(lmbda, a, tl, tu)
        print('Assign 06: Problem 01: Unit Test 02: pass')

    def test_assign_06_prob_01_ut_03(self):
        print('\n***** Assign 06: Problem 01: Unit Test 03 *****')
        lmbda, a = make_const(0.71), make_const(33.33)
        tl, tu = make_const(0.0), make_const(50.0)
        prm = percent_retention_model(lmbda, a)
        assert not prm is None
        print(prm)
        prmf = tof(prm)
        assert not prmf is None
        gt = lambda t: 66.67 * (math.e**(-0.71*t)) + 33.33
        err = 0.0001
        for t in range(100):
            assert abs(gt(t) - prmf(t)) <= err
        plot_retention(lmbda, a, tl, tu)
        print('Assign 06: Problem 01: Unit Test 03: pass')

    ### ************* HW06: Problem 02 UTs *******************************

    def test_assign_06_prob_02_ut_01(self):
        print('\n***** Assign 06: Problem 02: Unit Test 01 *****')
        p = make_const(500000.0)
        t0, p0 = make_const(0.0), make_const(200.0)
        t1, p1 = make_const(1.0), make_const(500.0)
        sdm = spread_of_disease_model(p, t0, p0, t1, p1)
        assert not sdm is None
        print(sdm)
        sdmf = tof(sdm)
        assert not sdmf is None
        gt = lambda t: 500000.0/(1.0 + 2499.0*(math.e**(-0.916891152186*t)))
        err = 0.0001
        for t in range(100):
            assert abs(gt(t) - sdmf(t)) <= err
        tl, tu = make_const(0.0), make_const(10.0)
        plot_spread_of_disease(p, t0, p0, t1, p1, tl, tu)
        print('Assign 06: Problem 02: Unit Test 01: pass')

    def test_assign_06_prob_02_ut_02(self):
        print('\n***** Assign 06: Problem 02: Unit Test 02 *****')
        p = make_const(250000.0)
        t0, p0 = make_const(0.0), make_const(100.0)
        t1, p1 = make_const(2.0), make_const(400.0)
        sdm = spread_of_disease_model(p, t0, p0, t1, p1)
        assert not sdm is None
        print(sdm)
        sdmf = tof(sdm)
        assert not sdmf is None
        gt = lambda t: 250000.0/(1.0 + 2499.0*(math.e**(-0.693747781233*t)))
        err = 0.0001
        for t in range(100):
            assert abs(gt(t) - sdmf(t)) <= err
        tl, tu = make_const(0.0), make_const(10.0)
        plot_spread_of_disease(p, t0, p0, t1, p1, tl, tu)
        print('Assign 06: Problem 02: Unit Test 02: pass')

    def test_assign_06_prob_02_ut_03(self):
        print('\n***** Assign 06: Problem 02: Unit Test 03 *****')
        p = make_const(350000.0)
        t0, p0 = make_const(0.0), make_const(11.0)
        t1, p1 = make_const(3.0), make_const(312.0)
        sdm = spread_of_disease_model(p, t0, p0, t1, p1)
        assert not sdm is None
        print(sdm)
        sdmf = tof(sdm)
        assert not sdmf is None
        gt = lambda t: 350000.0/(1.0 + 31817.1818182*(math.e**(-1.11532277069*t)))
        err = 0.0001
        for t in range(100):
            assert abs(gt(t) - sdmf(t)) <= err
        tl, tu = make_const(0.0), make_const(10.0)
        plot_spread_of_disease(p, t0, p0, t1, p1, tl, tu)
        print('Assign 06: Problem 02: Unit Test 03: pass')

    ### ************* HW06: Problem 03 UTs *******************************

    def test_assign_06_prob_03_ut_01(self):
        print('\n***** Assign 06: Problem 03: Unit Test 01 *****')
        m = make_const(55.0)
        t0, h0 = make_const(9.0), make_const(8.0)
        t1, h1 = make_const(25.0), make_const(48.0)
        pgm = plant_growth_model(m, t0, h0, t1, h1)
        assert not pgm is None
        print(pgm)
        pgmf = tof(pgm)
        assert not pgmf is None
        err = 0.0001
        gt = lambda t: 55.0/(1.0 + 5.875*(math.e**(-0.230999807618*t)))
        assert abs(pgmf(0.0) - h0.get_val()) <= err
        assert abs(pgmf(t1.get_val()-t0.get_val()) - h1.get_val()) <= err
        for t in range(100):
            assert abs(gt(t) - pgmf(t)) <= err
        tl, tu = make_const(9.0), make_const(50.0)
        plot_plant_growth(m, t0, h0, t1, h1, tl, tu)
        print('Assign 06: Problem 03: Unit Test 01: pass')

    def test_assign_06_prob_03_ut_02(self):
        print('\n***** Assign 06: Problem 03: Unit Test 02 *****')
        m = make_const(70.0)
        t0, h0 = make_const(15.0), make_const(11.5)
        t1, h1 = make_const(30.0), make_const(57.23)
        pgm = plant_growth_model(m, t0, h0, t1, h1)
        assert not pgm is None
        print(pgm)
        pgmf = tof(pgm)
        assert not pgmf is None
        err = 0.0001
        gt = lambda t: 70.0/(1.0 + 5.08695652174*(math.e**(-0.20844395235*t)))
        assert abs(pgmf(0.0) - h0.get_val()) <= err
        assert abs(pgmf(t1.get_val()-t0.get_val()) - h1.get_val()) <= err
        for t in range(100):
            assert abs(gt(t) - pgmf(t)) <= err
        tl, tu = make_const(11.0), make_const(55.0)
        plot_plant_growth(m, t0, h0, t1, h1, tl, tu)
        print('Assign 06: Problem 03: Unit Test 02: pass')

    def test_assign_06_prob_03_ut_03(self):
        print('\n***** Assign 06: Problem 03: Unit Test 03 *****')
        m = make_const(120.0)
        t0, h0 = make_const(21.0), make_const(17.35)
        t1, h1 = make_const(32.0), make_const(71.34)
        pgm = plant_growth_model(m, t0, h0, t1, h1)
        assert not pgm is None
        print(pgm)
        pgmf = tof(pgm)
        assert not pgmf is None
        err = 0.0001
        gt = lambda t: 120.0/(1.0 + 5.91642651297*(math.e**(-0.196393861786*t)))
    
        assert abs(pgmf(0.0) - h0.get_val()) <= err
        assert abs(pgmf(t1.get_val()-t0.get_val()) - h1.get_val()) <= err
        
        for t in range(100):
            assert abs(gt(t) - pgmf(t)) <= err
        tl, tu = make_const(21.0), make_const(55.0)
        plot_plant_growth(m, t0, h0, t1, h1, tl, tu)
        print('Assign 06: Problem 03: Unit Test 03: pass')


    ### ************* HW06: Problem 04 UTs *******************************

    def test_assign_06_prob_04_ut_01(self):
        print('\n***** Assign 06: Problem 04: Unit Test 01 *****')
        p = make_const(50000.0)
        k = make_const(0.3)
        snm = spread_of_news_model(p, k)
        assert not snm is None
        print(snm)
        snmf = tof(snm)
        assert not snmf is None
        err = 0.0001
        dsn = deriv(snm)
        dsnf = tof(dsn)
        assert abs(dsnf(0.0) - 15000.0) <= err
        assert abs(dsnf(10.0) - 746.806025518) <= err
        assert abs(dsnf(30.0) - 1.8511470613) <= err
        print('Assign 06: Problem 04: Unit Test 01: pass')

    def test_assign_06_prob_04_ut_02(self):
        print('\n***** Assign 06: Problem 04: Unit Test 02 *****')
        p = make_const(50000.0)
        k = make_const(0.3)
        snm = spread_of_news_model(p, k)
        assert not snm is None
        print(snm)
        snmf = tof(snm)
        assert not snmf is None
        err = 0.0001
        gt = lambda t: 50000.0*(1.0 + (-1.0*(math.e**(-0.3*t))))
        for t in range(100):
            assert abs(gt(t) - snmf(t)) <= err
        tl, tu = make_const(0.0), make_const(50.0)
        plot_spread_of_news(p, k, tl, tu)
        print('Assign 06: Problem 04: Unit Test 02: pass')

    def test_assign_06_prob_04_ut_03(self):
        print('\n***** Assign 06: Problem 04: Unit Test 03 *****')
        p = make_const(100000.0)
        k = make_const(0.275)
        snm = spread_of_news_model(p, k)
        assert not snm is None
        print(snm)
        snmf = tof(snm)
        assert not snmf is None
        err = 0.0001
        gt = lambda t: 100000.0*(1.0 + (-1.0*(math.e**(-0.275*t))))
        for t in range(100):
            assert abs(gt(t) - snmf(t)) <= err
        tl, tu = make_const(0.0), make_const(50.0)
        plot_spread_of_news(p, k, tl, tu)
        print('Assign 06: Problem 04: Unit Test 03: pass')

    def runTest(self):
        pass

if __name__ == '__main__':
    unittest.main()
