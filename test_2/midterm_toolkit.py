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
from maker import make_pwr_expr
from deriv import deriv
from tof import tof
from antideriv import antideriv, antiderivdef
from hw08_s19 import amplify_grayscale_blur_img_dir
import numpy as np
from scipy import stats
import cv2
import math as m


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


def grayscale_images_in_dir(ftype, in_img_dir):
    '''
    Function grayscales each image in a directory with the given file type

    ftype - A string specifiying thefFile type for image, e.g. '.jpg', '.png'.

    in_img_dir - String directory location for the given images, e.g. '/home/vladimir/images/'.
    '''
    amplify_grayscale_blur_img_dir(ftype=ftype, in_img_dir=in_img_dir, kz=0, c='b', amount=0, appendTitle='_gray')


def split_channel_stats(filePath):
    '''
    Function splits an image into color channels and computes the mean, median, 
    mode, and standard deviation for each color channel. Returns a list of 5-tuples
    that includes the color channel, average, median, mode, and standard deviation
    of that channel. List order is Blue, Green, and then Red.

    filePath - String representing the path to the file
    '''
    
    # Read in file
    imgArr = cv2.imread(filePath)
    assert imgArr is not None

    # Split into channels 
    b,g,r = cv2.split(imgArr)
    channels = [b, g, r]
    colorStats = []

    # Compute statistics and append the tuple to return list
    for color in channels:
        avg = np.mean(color)    # Default is whole array, not an axis
        med = np.median(color)  # Default is whole array, not an axis
        mod = stats.mode(color, axis=None) # Default is each axis, axis=None -> whole array
        sd  = np.std(color)     # Default is whole array, not an axis
        colorStats.append( (color, avg, med, mod, sd) ) # Append tuple
    
    return colorStats


def grayscale_blur_and_stats(filePath, blurSize=3):
    '''
    Function grayscales and blurs a specific image then computes statistics on the image. 
    Returns tuple of the image array, average, median, mode, and standard deviation.

    filePath - String representing the path to the file

    blurSize - Odd positive integer specifying the size of a mean blur filter.
    '''
    
    # Read in image
    imgArr = cv2.imread(filePath)
    assert imgArr is not None
    
    # Grayscale and blur image
    grayImg = cv2.cvtColor(imgArr, cv2.COLOR_RGB2GRAY)
    blurImg = cv2.blur(grayImg, (blurSize, blurSize))
    
    # Compute statistics
    avg = np.mean(blurImg)    # Default is whole array, not an axis
    med = np.median(blurImg)  # Default is whole array, not an axis
    mod = stats.mode(blurImg, axis=None) # Default is each axis, axis=None -> whole array
    sd  = np.std(blurImg)     # Default is whole array, not an axis

    return (blurImg, avg, med, mod, sd)

def amplify_and_display(filePath, color, amount):
    '''
    Amplifies a color channel within specific image then displays both the 
    amplified and original image.

    filePath - String representing the path to the file

    color - String / char representing the color channel to amplify

    amount - Integer specifying the amount to amplify
    '''

    # Read in image
    imgArr = cv2.imread(filePath)
    assert imgArr is not None
    
    # Split channels for amplication
    b,g,r = cv2.split(imgArr)

    # Amplify specified color
    if color=='b' or color=='B':
        b+=amount
    elif color=='g' or color=='G':
        g+=amount
    elif color=='r' or color=='R':
        r+=amount
    else:
        print("Invalid color provided. Exiting function.")
        return

    # Combine channels to create image
    amplifiedImage = cv2.merge([b,g,r])
    # Show original and amplified image
    cv2.imshow(filePath, imgArr)
    cv2.imshow("Amplified", amplifiedImage)

    cv2.waitKey()
    cv2.destroyAllWindows()


def net_change(marginalRevExpr, pl1, pl2):
    assert isinstance(pl1, const)
    assert isinstance(pl2, const)

    revenueNetChange = antiderivdef(expr=marginalRevExpr, a=pl1, b=pl2)
    return make_const(revenueNetChange) # NOT SURE IF WE NEED TO RETURN CONST?


def taylor_poly(fexpr, a, n):
    assert isinstance(a, const)
    assert isinstance(n, const)

    taylorFunc = nthTaylor(fexpr, a, n, 0)
    for i in range(1, n.get_val()+1):
        fexpr = deriv(fexpr)
        nextTaylor = nthTaylor(fexpr, a, n, i)
        taylorFunc = make_plus(elt_expr1=taylorFunc, elt_expr2=nextTaylor)
    print(taylorFunc)
    return tof(taylorFunc)


def nthTaylor(expr, a, n, i):
    exprFunc = tof(expr)
    exprAtA = exprFunc(a.get_val())
    frac = exprAtA / m.factorial(i)
    
    xMinusA = make_plus(elt_expr1=make_pwr('x', 1.0),
                        elt_expr2=make_const(-1 * a.get_val()))
    nthtaylor = make_prod(mult_expr1=make_const(frac),
                          mult_expr2=make_pwr_expr(expr=xMinusA, deg=i))
    return nthtaylor
    


