#!/usr/bin/python


####################################
# module: deriv.py
# Mark Allred
# A01647260
####################################

from var import var
from const import const
from pwr import pwr
from prod import prod
from plus import plus
from quot import quot
from ln import ln
from absv import absv
from maker import make_const, make_prod, make_pwr, make_pwr_expr
from maker import make_quot, make_e_expr, make_var, make_plus
from maker import make_e_expr, make_ln
from simplify import simplify


##
# Wrapper to direct expressions to the
# requisite derivative function, then 
# simplify the expression.
def deriv(expr):
    if isinstance(expr, const):
        return simplify(const_deriv(expr))
    elif isinstance(expr, pwr):
        return simplify(pwr_deriv(expr))
    elif isinstance(expr, prod):
        return simplify(prod_deriv(expr))
    elif isinstance(expr, plus):
        return simplify(plus_deriv(expr))
    elif isinstance(expr, quot):
        return simplify(quot_deriv(expr))
    elif isinstance(expr, var):
        return simplify(var_deriv(expr))
    elif isinstance(expr, ln):
        return simplify(ln_deriv(expr))
    elif isinstance(expr, absv):
        return simplify(absv_deriv(expr))
    else:
        raise Exception('deriv:' + str(expr))


##
# Returns a zero const object
def const_deriv(c = make_const(1.0)):
    assert isinstance(c, const)
    return make_const(val = 0.0)


##
# Returns a const of the derivative of a single variable
def var_deriv(x):
    assert isinstance(x, var)
    return make_const(val = 1.0)


##
# Returns a plus object representing the derivative of 
# an addition expression by taking the derivative of the s
# ubexpressions.
def plus_deriv(s):
    assert isinstance(s, plus)
    a = s.get_elt1()
    b = s.get_elt2()
    # Decompose expression and recompose with the derivatives of each component
    return make_plus(elt_expr1 = deriv(a), elt_expr2 = deriv(b))


##
# Returns the derivative of a power (exponent) expression
def pwr_deriv(expr):
    assert isinstance(expr, pwr)

    base = expr.get_base()
    deg  = expr.get_deg()

    if isinstance(base, const) and isinstance(deg, const):
        return make_const(val = 0.0)
    elif isinstance(base, var) and isinstance(deg, const):
        degVal = deg.get_val()
        return make_prod(
            mult_expr1 = deg,
            mult_expr2 = make_pwr_expr(base, degVal - 1.0)
        )
    elif isinstance(deg, const):
        degVal = deg.get_val()
        return make_prod(
            mult_expr1 = make_prod(
                            mult_expr1 = deg,
                            mult_expr2 = make_pwr_expr(base, degVal - 1.0)
                        ),
            mult_expr2 = deriv(base)
        )
    elif isinstance(base, const):
        return make_prod(
                mult_expr1 = deriv(deg),
                mult_expr2 = expr
        )
    elif not isinstance(base, const) and not isinstance(deg, const):
        return make_prod(
            mult_expr1 = deriv(expr.get_deg()),
            mult_expr2 = expr.get_base()
        )
    
    else:
        raise Exception('pwr_deriv case 1: ' + str(expr))


##
# Wrapper for implementation of the product rule
def product_rule_deriv(exprA, exprB):
    return make_plus(
            make_prod(
                mult_expr1 = deriv(exprA),
                mult_expr2 = exprB
            ),
            make_prod(
                mult_expr1 = exprA,
                mult_expr2 = deriv(exprB)
            )
    )
    

##
# Returns the derivative of a product expression using the product rule
def prod_deriv(expr):
    assert isinstance(expr, prod)
    mult1 = expr.get_mult1()
    mult2 = expr.get_mult2()

    # Attempt early exit by looking for const values
    if isinstance(mult1, const) and isinstance(mult2, const):
        return make_const(val = 0.0)
    elif isinstance(mult1, const) or isinstance(mult2, const):
        if isinstance(mult1, const):
            return make_prod(mult_expr1 = mult1,
                             mult_expr2 = deriv(mult2)
                            )
        elif isinstance(mult2, const):
            return make_prod(mult_expr1 = mult2,
                             mult_expr2 = deriv(mult1)
                            )
        else:
            raise Exception('prod_deriv case 1: ' + str(expr))
    # Early exit failed, return product rule
    elif not isinstance(mult1, const) and not isinstance(mult2, const):
        return product_rule_deriv(mult1, mult2)
    else:
        raise Exception('prod_deriv case 2: ' + str(expr))


##
# Returns the derivative of a quotient expression using the quotient rule
def quot_deriv(expr):
    assert isinstance(expr, quot)

    num = expr.get_num()
    denom = expr.get_denom()

    if isinstance(num, const) and isinstance(denom, const):
        return make_const(val = 0)
    # Simplification of Quotient Rule given the numerator is a constant
    elif isinstance(num, const):
        return make_quot(
            make_prod(
                make_const(val = -1 * num.get_val()),
                deriv(denom)
            ),
            make_pwr_expr(denom, 2)
        )
    # Simplification of Quotient Rule given the denominator is a constant
    elif isinstance(denom, const):
        return make_quot(nexpr = deriv(num), dexpr = denom)
    # Return Quotient Rule
    elif not isinstance(num, const) and not isinstance(denom, const):
        fPrime = deriv(num)
        gPrime = deriv(denom)

        numDeriv = make_plus(
                        make_prod(mult_expr1 = denom, mult_expr2 = fPrime),
                        make_prod(mult_expr1 = make_prod(mult_expr1 = make_const(val = -1), mult_expr2 = num), 
                                  mult_expr2 = gPrime)
        )
        denomDeriv = make_pwr_expr(expr = denom, deg = 2)
        return make_quot(nexpr = numDeriv, dexpr = denomDeriv)
    else:
        raise Exception('quot_deriv: case 1: ' + str(expr))


##
# Returns the derivative of a logarithmic expression using the power rule
def ln_deriv(expr):
    assert isinstance(expr, ln)
    return make_prod(
        mult_expr1 = make_quot(nexpr = make_const(val = 1.0), dexpr = expr.get_expr()),
        mult_expr2 = deriv(expr.get_expr())
    )


##
# Returns the derivative of an absolute expression by square rooting the square of the internal expression
def absv_deriv(expr):
    assert isinstance(expr, absv)
    # Absolute values are equivalent to squaring and taking the square root of
    # whatever is inside the absolute value function. The derivative can then 
    # be easily computed by passing it back up to the wrapper. 
    #
    # e.g. |f(x)| = sqrt( ( f(x) )^2 )

    fx = expr.get_expr()
    expr = make_pwr_expr(
            expr = make_pwr_expr(fx, make_const(2.0)),
            deg = make_const(1.0 / 2.0)
    )

    return deriv(expr)


##
# Returns derivative of complex expression via logarithmic differentiation
def logdiff(expr):
    assert isinstance(expr, prod)
    logExpr = getLog(expr)
    return make_prod(mult_expr1 = expr, mult_expr2 = deriv(logExpr))


##
# Returns the fully expanded log of an expression
def getLog(expr):
    # Return decomposed expression where ln(a^b) = b * ln(a)
    if isinstance(expr, pwr) and not isinstance(expr.get_deg(), const):
        return make_prod(
                mult_expr1 = expr.get_deg(), 
                mult_expr2 = make_ln(expr.get_base()))
    # Return ln of the expression
    elif not isinstance(expr, prod):
        return make_ln(expr)
    # Return expansion of a log'd expression: ln(a * b) = ln(a) + ln(b)
    else:
        return make_plus(
                elt_expr1 = getLog(expr.get_mult1()), 
                elt_expr2 = getLog(expr.get_mult2()))
    