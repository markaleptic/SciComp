#!/usr/bin/python

#####################################
# module: antideriv.py
# Mark Allred
# A01647260
#####################################

from maker import make_pwr, make_pwr_expr, make_const, make_e_expr
from maker import make_ln, make_quot, make_prod, make_plus, make_absv

def antideriv(i):
    ## CASE 1: i is a constant
    if isinstance(i, const):
        ## your code
        pass
    ## CASE 2: i is a pwr
    elif isinstance(i, pwr):
        b = i.get_base()
        d = i.get_deg()
        ## CASE 2.1: b is var and d is constant.
        if isinstance(b, var) and isinstance(d, const):
            ## your code here
            pass
        ## CASE 2.2: b is e
        elif is_e_const(b):
            ## your code here
            pass
        ## CASE 2.3: b is a sum
        elif isinstance(b, plus):
            ## your code here
            pass 
        else:
            raise Exception('antideriv: unknown case')
    ### CASE 3: i is a sum, i.e., a plus object.
    elif isinstance(i, plus):
        return make_plus(elt_expr1 = antideriv(i.get_elt1()), elt_expr2 = antideriv(i.get_elt1()))

    ### CASE 4: is is a product, i.e., prod object,
    ### where the 1st element is a constant.
    elif isinstance(i, prod):
        ## your code here
        pass
    else:
        raise Exception('antideriv: unknown case')

                     
            
def lnIntegral():
    return make_ln(make_absv(make_pwr('x', 1)))  
    
