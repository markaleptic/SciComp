import unittest
import numpy as np
from exam_toolkit import fit_regression_line, bell_curve_iq

class ExamToolKitTests(unittest.TestCase):
    def test_exam_02_prob_04_ut_01(self):
        print('\n***** Exam 02: Problem 04: Unit Test 01 *****')
        x = np.array([1, 2, 3, 4, 5])
        print(type(x))
        y = np.array([2, 3, 4, 5, 6])
        rlf = fit_regression_line(x, y)
        assert rlf(1) == 2.0
        assert rlf(2) == 3.0
        assert rlf(3) == 4.0
        assert rlf(4) == 5.0
        assert rlf(10) == 11.0
        assert rlf(101) == 102.0
        print('Exam 02: Problem 04: Unit Test 01: pass')

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