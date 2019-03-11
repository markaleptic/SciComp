#!/usr/bin/python

##################################
# module: antideriv.py
# Mark Allred
# A01647260
##################################


## modify these as you see fit.
from prod import prod
from plus import plus
from quot import quot
from const import const
from pwr import pwr
from var import var
from maker import make_pwr, make_pwr_expr, make_const, make_e_expr
from maker import make_ln, make_quot, make_prod, make_plus, make_absv
from consts import is_e_const, is_pi_const, is_zero_const
from deriv import deriv
from ispwr import is_pwr_0, is_pwr_1
from simplify import simplify
from tof import tof


def antideriv(i):
   return simplify(indeffiniteIntegral(i))
   
def indeffiniteIntegral(i):
    ## CASE 1: i is a constant
    if isinstance(i, const):
        return make_prod(mult_expr1=i,mult_expr2=make_pwr('x', 1.0))
    
    ## CASE 2: i is a pwr
    elif isinstance(i, pwr):
        b = i.get_base()
        d = i.get_deg() 

        ## CASE 2.1: b is var and d is constant.
        if isinstance(b, var) and isinstance(d, const):
            # Check for ln integral
            if d.get_val() == -1.0:
                return lnIntegral()

            # Determine new degree power
            newDeg = d.get_val() + 1
            
            # Place 1 / new degree in front of expression
            assert newDeg != 0
            coeff = 1 / newDeg
            coeff = make_const(coeff)
            
            # Create power expression with new power 
            newVar = make_pwr_expr(b, newDeg)

            return make_prod(mult_expr1 = coeff, mult_expr2 = newVar)

        ## CASE 2.2: b is e
        elif is_e_const(b):
            # perform u substitution
            u = d
            du = deriv(u)
            dx = make_quot(nexpr = make_const(1.0), dexpr = du)
            return make_prod(mult_expr1 = dx, mult_expr2 = i)

        ## CASE 2.3: b is a sum
        elif isinstance(b, plus):
            # simplifying assumption, TODO
            assert isinstance(d, const)
            
            # perform u substitution on sum expression
            u = b
            du = deriv(u)
            dx = make_quot(nexpr = make_const(1.0), dexpr = du)

            # Determine new degree power
            newDeg = d.get_val() + 1
            
            # Check if ln-integral
            if newDeg == 0:
                return make_prod(mult_expr1=dx, mult_expr2=lnIntegral(b))

            # Place 1 / new degree in front of expression
            assert newDeg != 0
            coeff = 1 / newDeg
            coeff = make_const(coeff)

            # Combined u substitution and front expression
            coeff = make_prod(mult_expr1=coeff, mult_expr2=dx)

            # Create sum expression with new power 
            newVar = make_pwr_expr(b, newDeg)
            return make_prod(mult_expr1=coeff, mult_expr2=newVar)
        else:
            raise Exception('antideriv: unknown case')
            
    ### CASE 3: i is a sum, i.e., a plus object.
    elif isinstance(i, plus):
        return make_plus(elt_expr1 = antideriv(i.get_elt1()), elt_expr2 = antideriv(i.get_elt2()))

    ### CASE 4: is is a product, i.e., prod object,
    ### where the 1st element is a constant.
    elif isinstance(i, prod):
        return make_prod(mult_expr1 = i.get_mult1(), mult_expr2 = antideriv(i.get_mult2()))
    else:
        raise Exception('antideriv: unknown case')


##
# Return ln |expr| for ease of reading in antideriv
def lnIntegral(expr = make_pwr('x', 1.0)):
    return make_ln(make_absv(expr))


##
# Return definite integral of expression from a to b
def antiderivdef(expr, a, b):
    assert isinstance(a, const)
    assert isinstance(b, const)
    
    integral = antideriv(expr)
    assert integral is not None

    integralf = tof(integral)
    assert integralf is not None

    definite = integralf(b.get_val()) - integralf(a.get_val())
    return make_const(definite)