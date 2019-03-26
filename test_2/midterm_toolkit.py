#############################################################
# module: midterm_toolkit.py
# Mark Allred
# A01647260
##############################################################

from prod import prod
from plus import plus
from quot import quot
from const import const
from maker import make_const, make_prod, make_quot, make_pwr, make_plus
from deriv import deriv
from tof import tof

def demand_elasticity_function(demand_curve=None, returnPyFunc=False):
    '''
    Creates and returns the Elasticity of Demand function 
    for a given demand_curve. Returns a functional
    representation by default or a Python function if
    returnPyFunc = True.

    demand_curve - functional representation of a demand curve, f(p)

    returnPyFunc - Function returns Functional Representation if False, Python function if True
    '''

    assert demand_curve is not None

    # E(p) = (-p * f'(p)) / f(p)
    numerator = make_prod(mult_expr1 = make_prod(make_const(-1.0), make_pwr('x', 1.0)),
                          mult_expr2 = deriv(demand_curve))
    denominator = demand_curve
    demand_elasticity = make_quot(nexpr = numerator, dexpr = denominator)

    if returnPyFunc:
        demand_elasticity = tof(demand_elasticity)
    return demand_elasticity


def demand_elasticity(demand_curve, price):
    '''
    Returns const object representing the elasticity of demand 
    at the price for the given demand cuve.
    
    demand_curve - functional representation of a demand curve, f(p)

    price - const object representing the price demanded
    '''
    assert demand_curve is not None
    assert isinstance(price, const)
    elasticityFunc = demand_elasticity_function(demand_curve=demand_curve, 
                                                returnPyFunc=True)
    elasticity = elasticityFunc(price.get_val())
    return make_const(elasticity)

def is_demand_elastic(demand_curve, price):
    '''
    Returns Boolean whether the quantity demanded is elastic or inelastic

    demand_curve - functional representation of a demand curve, f(p)

    price - const object representing the price demanded
    '''
    assert isinstance(price, const)
    if demand_elasticity(demand_curve, price).get_val() > 1:
        return True
    else:
        return False



