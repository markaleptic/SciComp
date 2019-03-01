#!/usr/bin/python

###########################################
# module: hw05.py
# Mark Allred
# A01647260
###########################################

# place the imports necessary for your solution here
from const import const
from maker import make_const, make_prod, make_pwr, make_e_expr, make_quot
from deriv import deriv
from tof import tof
import math as m

############################# Problem 1 ##############################

def solve_pdeq(k1, k2):
    assert isinstance(k1, const)
    assert isinstance(k2, const)
    k = k2.get_val() / k1.get_val()
    return make_e_expr(make_prod(mult_expr1 = make_const(k), 
                                 mult_expr2 = make_pwr('x', 1.0)))

def solve_pdeq_with_init_cond(y0, k):
    assert isinstance(y0, const)
    assert isinstance(k, const)
    eExpr = make_e_expr(make_prod(
                            mult_expr1 = (k), 
                            mult_expr2 = make_pwr('x', 1.0)))
    return make_prod(mult_expr1 = y0, mult_expr2 = eExpr)

############################# Problem 2 ##############################

def find_growth_model(p0, t, n):
    assert isinstance(p0, const)
    assert isinstance(t, const)
    assert isinstance(n, const)
    growthRate = m.log(n.get_val()) / t.get_val()
    growthRate = make_const(growthRate)

    expr = make_prod(mult_expr1 = p0, 
                     mult_expr2 = make_e_expr(make_prod(
                                                 mult_expr1 = growthRate, 
                                                 mult_expr2 = make_pwr('x', 1.0))))

    return expr

############################# Problem 3 ##############################

def radioactive_decay(lmbda, p0, t):
    assert isinstance(lmbda, const)
    assert isinstance(p0, const)
    assert isinstance(t, const)

    if lmbda.get_val() > 0:
        lmbda = make_const(-1 * lmbda.get_val())
    
    return make_prod(mult_expr1 = p0, 
                     mult_expr2 = make_e_expr(make_prod(mult_expr1 = lmbda, 
                                                        mult_expr2 = make_pwr('x', 1.0))))

############################# Problem 4 ##############################

def c14_carbon_dating(c14_percent):
    assert isinstance(c14_percent, const)
    assert c14_percent.get_val() <= 1.0
    decayConstant = -0.00012
    amtRemaining = m.log(c14_percent.get_val()) / decayConstant
    return make_const(m.ceil(amtRemaining))

############################# Problem 5 ##############################

def demand_elasticity(demand_eq, price):
    assert isinstance(price, const)
    numerator = make_prod(mult_expr1 = make_prod(make_const(-1.0), make_pwr('x', 1.0)),
                          mult_expr2 = deriv(demand_eq))
    denominator = demand_eq
    elasticityEq = make_quot(nexpr = numerator, dexpr = denominator)
    elasticityFunc = tof(elasticityEq)
    elasticityAtPrice = elasticityFunc(price.get_val())
    return make_const(elasticityAtPrice)
    

def is_demand_elastic(demand_eq, price):
    assert isinstance(price, const)
    if demand_elasticity(demand_eq, price).get_val() > 1:
        return True
    else:
        return False

def expected_rev_dir(demand_eq, price, price_direction):
    assert isinstance(price, const)
    assert isinstance(price_direction, const)
    assert price_direction.get_val() == 1 or \
           price_direction.get_val() == -1

    if is_demand_elastic(demand_eq, price):
        # Elastic: +1 ∆ in price -> -1 ∆ in revenue
        #          -1 ∆ in price -> +1 ∆ in revenue
        return make_const(-1.0 * price_direction.get_val())
    else:
        # Inelastic: +1 ∆ in price -> +1 ∆ in revenue
        #            -1 ∆ in price -> -1 ∆ in revenue
        return price_direction

    
    



    
