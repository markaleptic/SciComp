#!/usr/bin/python

#############################################################
# module: cs3430_s19_exam_02_unit_tests.py
# description: unit tests for CS 3430: S19: Exam 02
# you may not distribute these tests in any form.
# bugs to vladimir kulyukin via canvas
##############################################################

#uncomment the next line if you use Py2
#from __future__ import print_function
import unittest
import numpy as np
from cs3430_s19_exam_02 import test_antideriv
from cs3430_s19_exam_02 import fexpr_01, fexpr_02, fexpr_03, fexpr_04,\
     fexpr_05, fexpr_06, fexpr_07, fexpr_08, fexpr_09, fexpr_10
from cs3430_s19_exam_02 import gt_01, gt_02, gt_03, gt_04, gt_05,\
     gt_06, gt_07, gt_08, gt_09, gt_10
from maker import make_const
from cs3430_s19_exam_02 import taylor, test_taylor
from cs3430_s19_exam_02 import fexpr2_01, fexpr2_02, fexpr2_03
from cs3430_s19_exam_02 import gt21_02, gt21_03, gt22_02,\
     gt22_03, gt23_02, gt23_02, gt23_03 
from cs3430_s19_exam_02 import read_img_dir
from cs3430_s19_exam_02 import top_n_std
from cs3430_s19_exam_02 import blur_img_list
from cs3430_s19_exam_02 import fit_regression_line
from cs3430_s19_exam_02 import analyze_bee_traffic_data
from cs3430_s19_exam_02 import bell_curve_iq

class Exam01UnitTests(unittest.TestCase):

    ### ***** Exam 02: Problem 01 UTs ******
    def test_exam_02_prob_01_ut_01(self):
        print('\n***** Exam 02: Problem 01: Unit Test 01 *****')
        test_antideriv(fexpr_01, gt_01, make_const(0),
                       make_const(10), make_const(0.0001))
        print('Exam 02: Problem 01: Unit Test 01: pass')

    def test_exam_02_prob_01_ut_02(self):
        print('\n***** Exam 02: Problem 01: Unit Test 02 *****')
        test_antideriv(fexpr_02, gt_02, make_const(0),
                       make_const(10), make_const(0.0001))
        print('Exam 02: Problem 01: Unit Test 02: pass')

    def test_exam_02_prob_01_ut_03(self):
        print('\n***** Exam 02: Problem 01: Unit Test 03 *****')
        test_antideriv(fexpr_03, gt_03, make_const(0),
                       make_const(10), make_const(0.0001))
        print('Exam 02: Problem 01: Unit Test 03: pass')

    def test_exam_02_prob_01_ut_04(self):
        print('\n***** Exam 02: Problem 01: Unit Test 04 *****')
        test_antideriv(fexpr_04, gt_04, make_const(1),
                       make_const(10), make_const(0.0001))
        print('Exam 02: Problem 01: Unit Test 04: pass')

    def test_exam_02_prob_01_ut_05(self):
        print('\n***** Exam 02: Problem 01: Unit Test 05 *****')
        test_antideriv(fexpr_05, gt_05, make_const(1),
                       make_const(10), make_const(0.0001))
        print('Exam 02: Problem 01: Unit Test 05: pass')

    def test_exam_02_prob_01_ut_06(self):
        print('\n***** Exam 02: Problem 01: Unit Test 06 *****')
        test_antideriv(fexpr_06, gt_06, make_const(1),
                       make_const(5), make_const(0.0001))
        print('Exam 02: Problem 01: Unit Test 06: pass')

    def test_exam_02_prob_01_ut_07(self):
        print('\n***** Exam 02: Problem 01: Unit Test 07 *****')
        test_antideriv(fexpr_07, gt_07, make_const(0),
                       make_const(10), make_const(0.0001))
        print('Exam 02: Problem 01: Unit Test 07: pass')

    def test_exam_02_prob_01_ut_08(self):
        print('\n***** Exam 02: Problem 01: Unit Test 08 *****')
        test_antideriv(fexpr_08, gt_08, make_const(0),
                       make_const(10), make_const(0.0001))
        print('Exam 02: Problem 01: Unit Test 08: pass')

    def test_exam_02_prob_01_ut_09(self):
        print('\n***** Exam 02: Problem 01: Unit Test 09 *****')
        test_antideriv(fexpr_09, gt_09, make_const(0),
                       make_const(10), make_const(0.0001))
        print('Exam 02: Problem 01: Unit Test 09: pass')

    def test_exam_02_prob_01_ut_10(self):
        print('\n***** Exam 02: Problem 01: Unit Test 10 *****')
        test_antideriv(fexpr_10, gt_10, make_const(0),
                       make_const(10), make_const(0.0001))
        print('Exam 02: Problem 01: Unit Test 10: pass')

    ### ***** Exam 02: Problem 02 UTs ******
    def test_exam_02_prob_02_ut_01(self):
        print('\n***** Exam 02: Problem 02: Unit Test 01 *****')
        test_taylor(fexpr2_01, make_const(2.001), make_const(2),
                    make_const(0.0001), gt21_02)
        print('Exam 02: Problem 02: Unit Test 01: pass')

    def test_exam_02_prob_02_ut_02(self):
        print('\n***** Exam 02: Problem 02: Unit Test 02 *****')
        test_taylor(fexpr2_01, make_const(2.001), make_const(3),
                    make_const(0.0001), gt21_03)
        print('Exam 02: Problem 02: Unit Test 02: pass')

    def test_exam_02_prob_02_ut_03(self):
        print('\n***** Exam 02: Problem 02: Unit Test 03 *****')
        test_taylor(fexpr2_02, make_const(5.03), make_const(2),
                    make_const(0.0001), gt22_02)
        print('Exam 02: Problem 02: Unit Test 03: pass')

    def test_exam_02_prob_02_ut_04(self):
        print('\n***** Exam 02: Problem 02: Unit Test 04 *****')
        test_taylor(fexpr2_02, make_const(5.03), make_const(3),
                    make_const(0.0001), gt22_03)
        print('Exam 02: Problem 02: Unit Test 04: pass')

    def test_exam_02_prob_02_ut_05(self):
        print('\n***** Exam 02: Problem 02: Unit Test 05 *****')
        test_taylor(fexpr2_03, make_const(4.002), make_const(2),
                    make_const(0.0001), gt23_02)
        print('Exam 02: Problem 02: Unit Test 05: pass')

    def test_exam_02_prob_02_ut_06(self):
        print('\n***** Exam 02: Problem 02: Unit Test 06 *****')
        test_taylor(fexpr2_03, make_const(4.002), make_const(3),
                    make_const(0.0001), gt23_03)
        print('Exam 02: Problem 02: Unit Test 06: pass')

    ### ***** Exam 02: Problem 03 UTs ******
    def test_exam_02_prob_03_ut_01(self):
        print('\n***** Exam 02: Problem 03: Unit Test 01 *****')
        il = read_img_dir('.png', 'img/')
        assert len(il) == 98
        top_5 = top_n_std(il, 5, c='B')
        err = 0.0001
        img = top_5[0][0]
        mean = top_5[0][1]
        std = top_5[0][2]
        assert img == 'img/1b_bee_10.png'
        assert abs(mean - 160.12475555555557) <= err
        assert abs(std - 81.66040227197152) <= err
        for ip, mean, std in top_5:
            print(ip, mean, std)
        print('Exam 02: Problem 03: Unit Test 01: pass')

    def test_exam_02_prob_03_ut_02(self):
        print('\n***** Exam 02: Problem 03: Unit Test 02 *****')
        il = read_img_dir('.png', 'img/')
        assert len(il) == 98
        top_5 = top_n_std(il, 5, c='G')
        err = 0.0001
        img = top_5[0][0]
        mean = top_5[0][1]
        std = top_5[0][2]
        assert img == 'img/1b_bee_09.png'
        assert abs(mean - 141.78577777777778) <= err
        assert abs(std - 74.551843684269841) <= err
        for ip, mean, std in top_5:
            print(ip, mean, std)
        print('Exam 02: Problem 03: Unit Test 02: pass')

    def test_exam_02_prob_03_ut_03(self):
        print('\n***** Exam 02: Problem 03: Unit Test 03 *****')
        il = read_img_dir('.png', 'img/')
        assert len(il) == 98
        top_5 = top_n_std(il, 5, c='R')
        err = 0.0001
        img = top_5[0][0]
        mean = top_5[0][1]
        std = top_5[0][2]
        assert img == 'img/2b_bee_17.png'
        assert abs(mean - 199.68876543209876) <= err
        assert abs(std - 73.525401978483472) <= err
        for ip, mean, std in top_5:
            print(ip, mean, std)
        print('Exam 02: Problem 03: Unit Test 03: pass')

    def test_exam_02_prob_03_ut_04(self):
        print('\n***** Exam 02: Problem 03: Unit Test 04 *****')
        il = read_img_dir('.png', 'img/')
        assert len(il) == 98
        top_5 = top_n_std(il, 5, c='R')
        err = 0.0001
        img = top_5[0][0]
        mean = top_5[0][1]
        std = top_5[0][2]
        assert img == 'img/2b_bee_17.png'
        assert abs(mean - 199.68876543209876) <= err
        assert abs(std - 73.525401978483472) <= err
        for ip, mean, std in top_5:
            print(ip, mean, std)
        print('Exam 02: Problem 03: Unit Test 04: pass')

    def test_exam_02_prob_03_ut_05(self):
        print('\n***** Exam 02: Problem 03: Unit Test 05 *****')
        il = read_img_dir('.png', 'img/')
        bil = blur_img_list(il, 5)
        assert len(il) == 98
        top_5 = top_n_std(il, 5, c='G')
        err = 0.0001
        img = top_5[0][0]
        mean = top_5[0][1]
        std = top_5[0][2]
        assert img == 'img/1b_bee_09.png'
        assert abs(mean - 141.78577777777778) <= err
        assert abs(std - 74.551843684269841) <= err
        for ip, mean, std in top_5:
            print(ip, mean, std)
        print('Exam 02: Problem 03: Unit Test 05: pass')

    ### ***** Exam 02: Problem 04 UTs ******
    def test_exam_02_prob_04_ut_01(self):
        print('\n***** Exam 02: Problem 04: Unit Test 01 *****')
        x = np.array([1, 2, 3, 4, 5])
        y = np.array([2, 3, 4, 5, 6])
        rlf = fit_regression_line(x, y)
        assert rlf(1) == 2.0
        assert rlf(2) == 3.0
        assert rlf(3) == 4.0
        assert rlf(4) == 5.0
        assert rlf(10) == 11.0
        assert rlf(101) == 102.0
        print('Exam 02: Problem 04: Unit Test 01: pass')

    '''
***** Exam 02: Problem 04: Unit Test 02 *****
Upward Bee Traffic Data Report:
least squares error: 1.22702998091
sp.polyfit 2 error:  0.994272306456
sp.polyfit 3 error:  0.990574466368
sp.polyfit 10 error: 0.692368644818
Exam 02: Problem 04: Unit Test 02: pass
    '''
    def test_exam_02_prob_04_ut_02(self):
        print('\n***** Exam 02: Problem 04: Unit Test 02 *****')
        csv_fp = 'csv/192_168_4_5-2018-07-01_08-00-10.csv'
        analyze_bee_traffic_data(csv_fp, d='u')
        print('Exam 02: Problem 04: Unit Test 02: pass')

    '''
***** Exam 02: Problem 04: Unit Test 03 *****
Downward Bee Traffic Data Report:
least squares error: 9.43468027068
sp.polyfit 2 error:  9.2110371501
sp.polyfit 3 error:  6.52138839221
sp.polyfit 10 error: 5.03400458642
Exam 02: Problem 04: Unit Test 03: pass
    '''
    def test_exam_02_prob_04_ut_03(self):
        print('\n***** Exam 02: Problem 04: Unit Test 03 *****')
        csv_fp = 'csv/192_168_4_5-2018-07-01_08-00-10.csv'
        analyze_bee_traffic_data(csv_fp, d='d')
        print('Exam 02: Problem 04: Unit Test 03: pass')

    '''
***** Exam 02: Problem 04: Unit Test 04 *****
Lateral Bee Traffic Data Report:
least squares error: 3.52368055327
sp.polyfit 2 error:  3.4497548972
sp.polyfit 3 error:  3.43564839326
sp.polyfit 10 error: 2.54908883554
Exam 02: Problem 04: Unit Test 04: pass
    '''
    def test_exam_02_prob_04_ut_04(self):
        print('\n***** Exam 02: Problem 04: Unit Test 04 *****')
        csv_fp = 'csv/192_168_4_5-2018-07-01_08-00-10.csv'
        analyze_bee_traffic_data(csv_fp, d='l')
        print('Exam 02: Problem 04: Unit Test 04: pass')

    ### ***** Exam 02: Problem 05 UTs ******
    def test_exam_02_prob_05_ut_01(self):
        print('\n***** Exam 02: Problem 05: Unit Test 01 *****')
        err = 0.0001
        p = bell_curve_iq(120, 126, r='s', n=6)
        print(p)
        assert abs(p - 5.356847165747042) <= err
        print('Exam 02: Problem 05: Unit Test 01: pass')

    def test_exam_02_prob_05_ut_02(self):
        print('\n***** Exam 02: Problem 05: Unit Test 02 *****')
        err = 0.0001
        p = bell_curve_iq(120, 126, r='m', n=6)
        print(p)
        assert abs(p - 5.355950711154588) <= err
        print('Exam 02: Problem 05: Unit Test 02: pass')

    def test_exam_02_prob_05_ut_03(self):
        print('\n***** Exam 02: Problem 05: Unit Test 03 *****')
        err = 0.0001
        p = bell_curve_iq(120, 126, r='t', n=6)
        print(p)
        assert abs(p - 5.358646430197745) <= err
        print('Exam 02: Problem 05: Unit Test 03: pass')

    def test_exam_02_prob_05_ut_04(self):
        print('\n***** Exam 02: Problem 05: Unit Test 04 *****')
        err = 0.0001
        p = bell_curve_iq(20, 120, r='s', n=200)
        print(p)
        assert abs(p - 89.43499414198169) <= err
        print('Exam 02: Problem 05: Unit Test 04: pass')

    def test_exam_02_prob_05_ut_05(self):
        print('\n***** Exam 02: Problem 05: Unit Test 05 *****')
        err = 0.0001
        p = bell_curve_iq(20, 120, r='m', n=200)
        print(p)
        assert abs(p - 89.43592303771317) <= err
        print('Exam 02: Problem 05: Unit Test 05: pass')

    def test_exam_02_prob_05_ut_06(self):
        print('\n***** Exam 02: Problem 05: Unit Test 06 *****')
        err = 0.0001
        p = bell_curve_iq(20, 120, r='t', n=200)
        print(p)
        assert abs(p - 89.43313586163396) <= err
        print('Exam 02: Problem 05: Unit Test 06: pass')
    
    def runTest(self):
        pass

if __name__ == '__main__':
    unittest.main()
