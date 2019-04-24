
#########################################
# module: ispwr.py
# Mark Allred
# A01647260
#########################################

import re

def is_pwr_0(expr):
    pass

def is_pwr_1(expr):
    """
    Returns whether an expression is a first order polynomial. Assumes a polynomial in the form, 
    Ax^2.0 + Bx^1.0 + C, 
    is passed to the function.
    """

    # Convert expression to a string, and analyzes the expression using regular expressions to save computation time
    strExpr = str(expr)
    matches = re.search(r'x\^2\.0|x\^3\.0', strExpr)
    if matches is not None:
        return False
    
    # Check if expression contains single power or 'x'
    matches = re.search(r'x\^1\.0|x', strExpr)
    if matches is None:
        return False
    return True

def is_pwr_2(expr):
    """
    Returns whether an expression is a second order polynomial. Assumes a polynomial in the form, 
    Ax^2.0 + Bx^1.0 + C, 
    is passed to the function.
    """
    # Convert expression to a string, and analyzes the expression using regular expressions to save computation time
    strExpr = str(expr)
    # Check if expression contains cube
    matches = re.search(r'x\^3\.0', strExpr)
    if matches is not None:
        return False

    # Check if expression contains square
    matches = re.findall(r'x\^2\.0', strExpr)
    if matches is None:
        return False
    return True