import re

#########################################
# module: ispwr.py
# Mark Allred
# A01647260
#########################################


##
# Returns whether an expression is a first
# order polynomial. 
# 
# Converts the expression to a string, and
# analyzes the expression using regular 
# expressions
def is_pwr_1(expr):
    strExpr = str(expr)
    # Check if expression contains square or cube
    matches = re.search(r'x\^2\.0|x\^3\.0', strExpr)
    if matches is not None:
        return False
    
    # Check if expression contains single power or 'x'
    matches = re.search(r'x\^1\.0|x', strExpr)
    if matches is None:
        return False
    return True


##
# Returns whether an expression is a second
# order polynomial. 
# 
# Converts the expression to a string, and 
# analyzes the expression using regular 
# expressions
def is_pwr_2(expr):
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