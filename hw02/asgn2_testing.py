from var import var
from const import const
from pwr import pwr
from prod import prod
from plus import plus
from maker import make_const, make_prod, make_plus, make_pwr, make_pwr_expr
from tof import tof, const_tof, pwr_tof, prod_tof, plus_tof
from deriv import deriv, const_deriv, prod_deriv, pwr_deriv, var_deriv, plus_deriv
from poly12 import find_poly_1_zeros, find_poly_2_zeros, getConstant, firstOrderCoeff, secondOrderCoeff
from derivtest import loc_xtrm_1st_drv_test, loc_xtrm_2nd_drv_test
from infl import find_infl_pnts
import math



##########################
#  ASSIGNMENT 2 TESTING  #
##########################

# def test_00():
# 	f1 = make_prod(make_const(2.0),
# 					make_pwr('x', 1.0))
# 	f2 = make_plus(f1, make_const(5.0))
# 	z = find_poly_1_zeros(f2)
# 	isinstance(z, const)
# 	print (z)

# 	from tof import tof
# 	f = tof(f2)
# 	assert f(z.get_val()) == 0.0
# test_00()

# def test_01():
#     print("\n\nTest 1\n")
#     f1 = make_prod(make_const(3.0), make_pwr('x', 1.0))
#     f2 = make_plus(f1, make_const(100.0))
#     print (f2)
#     z = find_poly_1_zeros(f2)
#     f2f = tof(f2)
#     assert f2f(z.get_val()) == 0.0
#     print (str(z))
# test_01()

# def test_02():
#     print("\n\nTest 2\n")
#     f0 = make_prod(make_const(0.5), make_pwr('x', 2.0))
#     f1 = make_prod(make_const(6.0), make_pwr('x', 1.0))
#     f2 = make_plus(f0, f1)
#     poly = make_plus(f2, make_const(0.0))
#     print(poly)
#     zeros = find_poly_2_zeros(poly)
#     for c in zeros:
#         print (c)
#     pf = tof(poly)
#     for c in zeros:
#         assert abs(pf(c.get_val()) - 0.0) <= 0.0001
# test_02()

# def test_03():
#     print("\n\nTest 3\n")
#     f1 = make_prod(make_const(1.0/3.0), make_pwr('x', 3.0))
#     f2 = make_prod(make_const(-2.0), make_pwr('x', 2.0))
#     f3 = make_prod(make_const(3.0), make_pwr('x', 1.0))
#     f4 = make_plus(f1, f2)
#     f5 = make_plus(f4, f3)
#     poly = make_plus(f5, make_const(1.0))
#     print ('f(x) = ', poly)
#     xtrma = loc_xtrm_1st_drv_test(poly)
#     for i, j in xtrma:
#         print (i, str(j))
# test_03()

# def test_04():
#     print("\n\nTest 4\n")
#     f1 = make_prod(make_const(27.0), make_pwr('x', 3.0))
#     f2 = make_prod(make_const(-27.0), make_pwr('x', 2.0))
#     f3 = make_prod(make_const(9.0), make_pwr('x', 1.0))
#     f4 = make_plus(f1, f2)
#     f5 = make_plus(f4, f3)
#     f6 = make_plus(f5, make_const(-1.0))
#     print('f(x) = ', f6)
#     drv = deriv(f6)
#     assert not drv is None
#     print ('f\'(x) = ', drv)
#     xtrma = loc_xtrm_1st_drv_test(f6)
#     assert xtrma is None
# test_04()

# def test_05():
#     print("\n\nTest 5\n")
#     f1 = prod(mult1=make_const(1.0/4.0),
#               mult2=make_pwr('x', 2.0))
#     f2 = prod(mult1=make_const(-1.0),
#               mult2=make_pwr('x', 1.0))
#     f3 = plus(elt1=f1, elt2=f2)
#     f4 = plus(elt1=f3, elt2=make_const(2.0))
#     print (f4)
#     xtrma = loc_xtrm_2nd_drv_test(f4)
#     for i, j in xtrma:
#         print (i, str(j))
#     assert len(xtrma) == 1 and \
#            xtrma[0][1].get_x().get_val() == 2.0 and \
#            xtrma[0][1].get_y().get_val() == 1.0
# test_05()

# def test_06():
#     print("\n\nTest 6\n")
#     f1 = make_pwr('x', 3.0)
#     f2 = make_prod(make_const(-3.0), make_pwr('x', 2.0))
#     f3 = make_plus(f1, f2)
#     f4 = make_plus(f3, make_prod(make_const(0.0), make_pwr('x', 1.0)))
#     poly = make_plus(f4, make_const(5.0))
#     print (poly)
#     infls = find_infl_pnts(poly)
#     for ip in infls:
#         print (str(ip))
# test_06()

# def test_assgn_02_ut_06():
# 	print('\n***** Assign 02: Problem 01: Unit Test 06 *****')
# 	f0 = make_pwr('x', 2.0)
# 	f1 = make_prod(make_const(-3.0), make_pwr('x', 1.0))
# 	f2 = make_plus(f0, f1)
# 	poly = make_plus(f2, make_const(-4.0))
# 	print(poly)
# 	zeros = find_poly_2_zeros(poly)
# 	for z in zeros:
# 			print(z)
# 	pf = tof(poly)
# 	err = 0.0001
# 	for z in zeros:
# 			assert abs(pf(z.get_val()) - 0.0) <= err 
# 	print('Assign 02: Problem 01: Unit Test 06: pass')
# test_assgn_02_ut_06()

def test_assgn_02_ut_14():
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
test_assgn_02_ut_14()