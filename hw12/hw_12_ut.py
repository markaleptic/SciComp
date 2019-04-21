import unittest
from const import const
from maker import make_var, make_const, make_pwr, make_plus, make_prod, make_line_eq, make_point2d
from line_eq import line_eq
from poly12 import is_const_line, get_line_coeffs
from point2d import point2d
from linprog import line_intersection, maximize_obj_fun, minimize_obj_fun

class Assign12(unittest.TestCase):
    def test_01(self):
        print("\n**** Test 1 ****")
        ln1 = make_line_eq(make_var('y'), make_const(1.0))
        ln2 = make_line_eq(make_var('x'), make_const(1.0))
        print(ln1)
        print(ln2)
        assert is_const_line(ln1)
        assert is_const_line(ln2)
        intersection = line_intersection(ln1, ln2)
        print("Intersection:", intersection)
        gt_values = point2d(make_const(1.0), make_const(1.0))
        err = 0.0001
        assert abs(intersection.get_x().get_val() - gt_values.get_x().get_val()) <= err
        assert abs(intersection.get_y().get_val() - gt_values.get_y().get_val()) <= err
        print("**** Test Passed ****\n")

    def test_02a(self):
        print("\n**** Test 2a ****")
        ln1 = make_line_eq(make_var('y'), make_const(2.0))
        ln2 = make_line_eq(make_var('y'), make_plus(make_pwr('x', 1.0),
                                                    make_const(-6.0)))
        print(ln1)
        print(ln2)

        intersection = line_intersection(ln1, ln2)
        print("Intersection point", intersection)
        gt_values = point2d(make_const(8.0), make_const(2.0))
        err = 0.0001
        assert abs(intersection.get_x().get_val() - gt_values.get_x().get_val()) <= err
        assert abs(intersection.get_y().get_val() - gt_values.get_y().get_val()) <= err
        print("**** Test Passed ****\n")

    def test_02b(self):
        print("\n**** Test 2b ****")
        ln1 = make_line_eq(make_var('y'), make_const(2.0))
        ln2 = make_line_eq(make_var('y'), make_plus(make_pwr('x', 1.0),
                                                    make_const(-6.0)))
        print(ln1)
        print(ln2)

        intersection = line_intersection(ln2, ln1)
        print("Intersection point", intersection)
        gt_values = point2d(make_const(8.0), make_const(2.0))
        err = 0.0001
        assert abs(intersection.get_x().get_val() - gt_values.get_x().get_val()) <= err
        assert abs(intersection.get_y().get_val() - gt_values.get_y().get_val()) <= err
        print("**** Test Passed ****\n")

    def test_03a(self):
        print("\n**** Test 3a ****")
        ln1 = make_line_eq(make_var('y'), make_const(-2.0))
        ln2 = make_line_eq(make_var('y'), make_plus(make_pwr('x', 1.0),
                                                    make_const(10.0)))
        print(ln1)
        print(ln2)
        intersection = line_intersection(ln1, ln2)
        print("Intersection point", intersection)
        gt_values = point2d(make_const(-12.0), make_const(-2.0))
        err = 0.0001
        assert abs(intersection.get_x().get_val() - gt_values.get_x().get_val()) <= err
        assert abs(intersection.get_y().get_val() - gt_values.get_y().get_val()) <= err

        print("**** Test Passed ****\n")

    def test_03b(self):
        print("\n**** Test 3b ****")
        ln1 = make_line_eq(make_var('y'), make_const(-2.0))
        ln2 = make_line_eq(make_var('y'), make_plus(make_pwr('x', 1.0),
                                                    make_const(10.0)))
        print(ln1)
        print(ln2)
        intersection = line_intersection(ln2, ln1)
        print("Intersection point", intersection)
        gt_values = point2d(make_const(-12.0), make_const(-2.0))
        err = 0.0001
        assert abs(intersection.get_x().get_val() - gt_values.get_x().get_val()) <= err
        assert abs(intersection.get_y().get_val() - gt_values.get_y().get_val()) <= err

        print("**** Test Passed ****\n")

    def test_04(self):
        print("\n**** Test 4 ****")
        ln1 = make_line_eq(make_var('y'), make_const(2.0))
        ln2 = make_line_eq(make_var('y'), make_plus(make_prod(make_const(2.0),
                                                                make_pwr('x', 1.0)),
                                                    make_const(-6.0)))
        print(ln1)
        print(ln2)
        intersection = line_intersection(ln2, ln1)
        print("Intersection point", intersection)
        gt_values = point2d(make_const(4.0), make_const(2.0))
        err = 0.0001
        assert abs(intersection.get_x().get_val() - gt_values.get_x().get_val()) <= err
        assert abs(intersection.get_y().get_val() - gt_values.get_y().get_val()) <= err
        print("**** Test Passed ****\n")

    def test_05(self):
        print("\n**** Test 5 ****")
        ln1 = make_line_eq(make_var('y'), make_pwr('x', 1.0))
        ln2 = make_line_eq(make_var('y'), make_prod(make_const(2.0),
                                                    make_pwr('x', 1.0)))
        ln3 = make_line_eq(make_var('y'), make_plus(make_prod(make_const(3.0),
                                                                make_pwr('x', 1.0)),
                                                    make_const(-10.0)))
        print(ln1)
        print(ln2)
        print(ln3)

        print("\nLine Coefficients")
        print("Line 1:", get_line_coeffs(ln1))
        print("Line 2:", get_line_coeffs(ln2))
        print("Line 3:", get_line_coeffs(ln3))

        print("\nIntersection Points")
        intersection = line_intersection(ln1, ln2)
        print("Intersection point, ln1 & ln2", intersection)
        gt_values = point2d(make_const(0.0), make_const(0.0))
        err = 0.0001
        assert abs(intersection.get_x().get_val() - gt_values.get_x().get_val()) <= err
        assert abs(intersection.get_y().get_val() - gt_values.get_y().get_val()) <= err

        intersection = line_intersection(ln2, ln3)
        print("Intersection point, ln2 & ln3", intersection)
        gt_values = point2d(make_const(10.0), make_const(20.0))
        err = 0.0001
        assert abs(intersection.get_x().get_val() - gt_values.get_x().get_val()) <= err
        assert abs(intersection.get_y().get_val() - gt_values.get_y().get_val()) <= err
        
        intersection = line_intersection(ln1, ln3)
        print("Intersection point, ln1 & ln3", intersection)
        gt_values = point2d(make_const(5.0), make_const(5.0))
        err = 0.0001
        assert abs(intersection.get_x().get_val() - gt_values.get_x().get_val()) <= err
        assert abs(intersection.get_y().get_val() - gt_values.get_y().get_val()) <= err

        print("**** Test Passed ****\n")

    def test_06(self):
        print("\n**** Test 6 ****")
        ln1 = make_line_eq(make_var('y'), make_pwr('x', 1.0))
        ln2 = make_line_eq(make_var('y'), make_plus(make_prod(make_const(-1.0),
                                                                make_pwr('x', 1.0)),
                                                    make_const(6.0)))
        print(ln1)
        print(ln2)

        intersection = line_intersection(ln1, ln2)
        print("Intersection point", intersection)
        gt_values = point2d(make_const(3.0), make_const(3.0))
        err = 0.0001
        assert abs(intersection.get_x().get_val() - gt_values.get_x().get_val()) <= err
        assert abs(intersection.get_y().get_val() - gt_values.get_y().get_val()) <= err

        print("**** Test Passed ****\n")

    def test_07(self):
        print("\n**** Test 7 ****")
        ln1 = make_line_eq(make_var('y'), make_plus(make_prod(make_const(-1.0/5.0),
                                                                make_pwr('x', 1.0)),
                                                    make_const(10.0)))
        ln2 = make_line_eq(make_var('y'), make_plus(make_prod(make_const(1.0/5.0),
                                                                make_pwr('x', 1.0)),
                                                    make_const(5.0)))
        print(ln1)
        print(ln2)
        intersection = line_intersection(ln1, ln2)
        print("Intersection point", intersection)
        gt_values = point2d(make_const(12.5), make_const(7.5))
        err = 0.0001
        assert abs(intersection.get_x().get_val() - gt_values.get_x().get_val()) <= err
        assert abs(intersection.get_y().get_val() - gt_values.get_y().get_val()) <= err
        print("**** Test Passed ****\n")

    def test_08(self):
        print("\n**** Test 8 ****")
        ln1 = make_line_eq(make_var('y'), make_const(1.0))
        ln2 = make_line_eq(make_var('y'), make_plus(make_prod(make_const(-1.0),
                                                                make_pwr('x', 1.0)),
                                                    make_const(6.0)))
        print(ln1)
        print(ln2)

        intersection = line_intersection(ln1, ln2)
        print("Intersection point", intersection)
        gt_values = point2d(make_const(5.0), make_const(1.0))
        err = 0.0001
        assert abs(intersection.get_x().get_val() - gt_values.get_x().get_val()) <= err
        assert abs(intersection.get_y().get_val() - gt_values.get_y().get_val()) <= err
        
        print("**** Test Passed ****\n")

    def test_09(self):
        print("\n**** Test 9 ****")
        ln1 = make_line_eq(make_var('y'), make_const(5.0))
        ln2 = make_line_eq(make_var('y'), make_plus(make_prod(make_const(-1.0),
                                                                make_pwr('x', 1.0)),
                                                    make_const(6.0)))
        print(ln1)
        print(ln2)
        
        intersection = line_intersection(ln1, ln2)
        print("Intersection point", intersection)
        gt_values = point2d(make_const(1), make_const(5.0))
        err = 0.0001
        assert abs(intersection.get_x().get_val() - gt_values.get_x().get_val()) <= err
        assert abs(intersection.get_y().get_val() - gt_values.get_y().get_val()) <= err

        print("**** Test Passed ****\n")

    def test_10(self):
        print("\n**** Test 10 ****")
        f1 = lambda x, y: 2*x + y
        corner_points = [make_point2d(1, 1),
                        make_point2d(1, 5),
                        make_point2d(5, 1)]
        print(maximize_obj_fun(f1, corner_points))              
        f2 = lambda x, y: x - 2*y
        print(minimize_obj_fun(f2, corner_points))
        print("**** Test Passed ****\n")
        
        ### more tests

    def test_11(self):
        print("\n**** Test 11 ****")
        ln1 = make_line_eq(make_var('x'), make_const(1.0))
        ln2 = make_line_eq(make_var('y'), make_prod(make_const(0.5),
                                                    make_pwr('x', 1.0)))
        print(line_intersection(ln1, ln2))
        ln3 = make_line_eq(make_var('y'), make_plus(make_prod(make_const(-3.0/4),
                                                                make_pwr('x', 1.0)),
                                                    make_const(3.0)))
        print(line_intersection(ln1, ln3))
        print(line_intersection(ln2, ln3))
        print("**** Test Passed ****\n")


    def test_12(self):
        print("\n**** Test 12 ****")
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
        print("**** Test Passed ****\n")
        
    def runTest(self):
        pass

#TODO incorporate these:
"""
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
"""

if __name__ == '__main__':
    unittest.main()


