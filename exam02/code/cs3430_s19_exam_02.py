#!/usr/bin/python

#############################################################
# module: cs3430_s19_exam_02.py
# Mark Allred
# A01647260
##############################################################

## add/modify the imports as needed
from const import const
from maker import make_const, make_plus, make_prod, make_pwr, make_e_expr, make_pwr_expr
import numpy as np
import matplotlib.pyplot as plt
import math
import os
import cv2
import csv
import scipy as sp

from antideriv import antideriv, antiderivdef
from tof import tof
from midterm_toolkit import taylor_poly
from deriv import deriv
from defintegralapprox import midpoint_rule, trapezoidal_rule, simpson_rule

# ************* Problem 1 (3 points) **********************

fexpr_01 = make_pwr('x', 2.0)
fexpr_02 = make_e_expr(make_prod(make_const(-2.0),
                                 make_pwr('x', 1.0)))
fexpr_03 = make_pwr('x', 0.5)
fexpr_04 = make_pwr('x', -2.0)
fexpr_05 = make_pwr('x', -1.0)
fexpr_06 = make_plus(make_pwr('x', -3.0),
                     make_prod(make_const(7.0),
                               make_e_expr(make_prod(make_const(5.0),
                                                     make_pwr('x', 1.0)))))
fexpr_06 = make_plus(fexpr_06, make_prod(make_const(4.0), make_pwr('x', -1.0)))
fexpr_07 = make_prod(make_const(4.0), make_pwr('x', 3.0))
fexpr_08 = make_plus(make_prod(make_const(5.0),
                               make_pwr('x', 1.0)),
                     make_const(-7.0))
fexpr_08 = make_pwr_expr(fexpr_08, -2.0)
fexpr_09 = make_prod(make_const(3.0), make_pwr_expr(make_plus(make_const(2.0),
                                                              make_pwr('x', 1.0)),
                                                    -1.0))
fexpr_10 = make_plus(make_prod(make_const(3.0), make_pwr('x', 1.0)),
                     make_const(2.0))
fexpr_10 = make_pwr_expr(fexpr_10, 4.0)

gt_01 = lambda x: (1.0/3.0)*(x**3)
gt_02 = lambda x: -0.5*(math.e**(-2*x))
gt_03 = lambda x: (2.0/3.0)*(x**1.5)
gt_04 = lambda x: -1.0/x
gt_05 = lambda x: math.log(x, math.e)
gt_06 = lambda x: -0.5*(x**-2.0) + (7.0/5.0)*(math.e**(5.0*x)) + 4*math.log(abs(x), math.e)
gt_07 = lambda x: x**4
gt_08 = lambda x: -0.2*(5.0*x - 7.0)**-1.0
gt_09 = lambda x: 3*math.log(abs(2.0 + x), math.e)
gt_10 = lambda x: 1.0/15*(3.0*x + 2.0)**5.0

# this is your unit test for problem 1.
def test_01():
    test_antideriv(fexpr_01, gt_01, make_const(0), make_const(10), make_const(0.0001))
    test_antideriv(fexpr_02, gt_02, make_const(0), make_const(10), make_const(0.0001))
    test_antideriv(fexpr_03, gt_03, make_const(0), make_const(10), make_const(0.0001))
    test_antideriv(fexpr_04, gt_04, make_const(1), make_const(10), make_const(0.0001))
    test_antideriv(fexpr_05, gt_05, make_const(1), make_const(10), make_const(0.0001))
    test_antideriv(fexpr_06, gt_06, make_const(1), make_const(5), make_const(0.0001))
    test_antideriv(fexpr_07, gt_07, make_const(0), make_const(10), make_const(0.0001))
    test_antideriv(fexpr_08, gt_08, make_const(0), make_const(10), make_const(0.0001))
    test_antideriv(fexpr_09, gt_09, make_const(0), make_const(10), make_const(0.0001))
    test_antideriv(fexpr_10, gt_10, make_const(0), make_const(10), make_const(0.0001))

def test_antideriv(fexpr, gt, lwr, uppr, err):
    assert isinstance(lwr, const)
    assert isinstance(uppr, const)
    assert isinstance(err, const)
    
    integral = antideriv(fexpr)
    assert integral is not None
    print(integral)

    integralFunc = tof(integral)

    for x in range(lwr.get_val(), uppr.get_val()):
        assert abs(integralFunc(x) - gt(x)) <= err.get_val()
        print(integralFunc(x),',', gt(x))

# ************* Problem 2 (3 points) **********************

def taylor(fexpr, a, n):
    assert isinstance(a, const)
    assert isinstance(n, const)
    return taylor_poly(fexpr, a, n)

# 3 function expressiosn for problem 2.
fexpr2_01 = make_prod(make_pwr('x', 1.0),
                      make_e_expr(make_pwr('x', 1.0)))
fexpr2_02 = make_plus(make_pwr('x', 4.0),
                      make_pwr('x', 1.0))
fexpr2_02 = make_plus(fexpr2_02, make_const(1.0))
fexpr2_03 = make_pwr_expr(make_plus(make_const(5.0),
                                    make_prod(make_const(-1.0),
                                              make_pwr('x', 1.0))),
                          -1.0)

# 3 gt functions for problem 2.
def gt21_02(x):
    ''' ground truth for 2nd taylor of fexpr2_01. '''
    f0 = tof(fexpr2_01)
    f1 = tof(deriv(fexpr2_01))
    f2 = tof(deriv(deriv(fexpr2_01)))
    return f0(2.0) + f1(2.0)*(x - 2.0) + (f2(2.0)/2)*(x - 2.0)**2

def gt21_03(x):
    ''' ground truth for 3rd taylor for fexpr2_01. '''
    f0 = tof(fexpr2_01)
    f1 = tof(deriv(fexpr2_01))
    f2 = tof(deriv(deriv(fexpr2_01)))
    f3 = tof(deriv(deriv(deriv(fexpr2_01))))
    return f0(2.0) + f1(2.0)*(x-2.0) + (f2(2.0)/2)*(x - 2.0)**2 + \
           (f3(2.0)/6)*(x - 2.0)**3

def gt22_02(x):
    ''' ground truth for 2nd taylor for fexpr2_02. '''
    f0 = tof(fexpr2_02)
    f1 = tof(deriv(fexpr2_02))
    f2 = tof(deriv(deriv(fexpr2_02)))
    return f0(5.0) + f1(5.0)*(x - 5.0) + (f2(5.0)/2)*(x-5.0)**2

def gt22_03(x):
    ''' ground truth for 3rd taylor for fexpr2_02. '''
    f0 = tof(fexpr2_02)
    f1 = tof(deriv(fexpr2_02))
    f2 = tof(deriv(deriv(fexpr2_02)))
    f3 = tof(deriv(deriv(deriv(fexpr2_02))))
    return f0(5.0) + f1(5.0)*(x-5.0) + (f2(5.0)/2)*(x-5.0)**2 + \
           (f3(5.0)/6)*(x - 5.0)**3

def gt23_02(x):
    ''' ground truth for 2nd taylor for fexpr_03. '''
    f0 = tof(fexpr2_03)
    f1 = tof(deriv(fexpr2_03))
    f2 = tof(deriv(deriv(fexpr2_03)))
    return f0(4.0) + f1(4.0)*(x - 4.0) + (f2(4.0)/2)*(x-4.0)**2

def gt23_03(x):
    ''' ground truth for 3rd taylor for fexpr_03. '''
    f0 = tof(fexpr2_03)
    f1 = tof(deriv(fexpr2_03))
    f2 = tof(deriv(deriv(fexpr2_03)))
    f3 = tof(deriv(deriv(deriv(fexpr2_03))))
    return f0(4.0) + f1(4.0)*(x-4.0) + (f2(4.0)/2)*(x-4.0)**2 + \
           (f3(4.0)/6)*(x-4.0)**3

def test_taylor(fexpr, x, n, err, gt):
    assert isinstance(x, const)
    assert isinstance(n, const)
    assert isinstance(err, const)
    
    taylorPolynomial = taylor(fexpr, x, n)
    print(taylorPolynomial)
    x = x.get_val()
    print("Ground Truth Value:", gt(x))
    assert abs(taylorPolynomial(x) - gt(x)) <= err.get_val()
           
# this is the unit test for problem 2.   
def test_02():
    test_taylor(fexpr2_01, make_const(2.001), make_const(2), make_const(0.0001), gt21_02)
    test_taylor(fexpr2_01, make_const(2.001), make_const(3), make_const(0.0001), gt21_03)
    test_taylor(fexpr2_02, make_const(5.03), make_const(2), make_const(0.0001), gt22_02)
    test_taylor(fexpr2_02, make_const(5.03), make_const(3), make_const(0.0001), gt22_03)
    test_taylor(fexpr2_03, make_const(4.002), make_const(2), make_const(0.0001), gt23_02)
    test_taylor(fexpr2_03, make_const(4.002), make_const(3), make_const(0.0001), gt23_03)

# ************* Problem 3 (3 points) **********************

## change this variable accordingly if you need to use it.
IMGDIR = 'exam02/img/'

def generate_file_names(ftype, rootdir):
    '''
    recursively walk dir tree beginning from rootdir
    and generate full paths to all files that end with ftype.
    sample call: generate_file_names('.jpg', /home/pi/images/')
    '''
    for path, dirlist, filelist in os.walk(rootdir):
        for file_name in filelist:
            if not file_name.startswith('.') and \
               file_name.endswith(ftype):
                yield os.path.join(path, file_name)
        for d in dirlist:
            generate_file_names(ftype, d)

def read_img_dir(ftype, imgdir):
    '''
    takes a file type (e.g., '.jpg') and a directory of images
    (e.g., /home/pi/images/') and returns a list of 2-tuples. In
    each 2-tuple, the first element is the full path to an image
    (e.g., /home/pi/images/img01.jpg') and the second is the numpy
    matrix of that image obtained with cv2.imread().
    '''
    imglst = []
    print(imgdir)
    for imgp in generate_file_names(ftype, imgdir):
        imglst.append((imgp, cv2.imread(imgp)))
    return imglst

def top_n_std(imglist, n, c='B'):
    images = []
    

    for imgTuple in imglist:
        imgPath = imgTuple[0]
        imgArr  = imgTuple[1]
        b, g, r = cv2.split(imgArr)

        if c=='b' or c=='B':
            color = b
        elif c=='g' or c=='G':
            color = g
        elif c=='r' or c=='R':
            color = r
        else:
            print("Invalid color provided. Exiting function.")
            return

        avg = np.mean(color)
        sd  = np.std(color)
        images.append( (imgPath, avg, sd) )

    images = sorted(images, key=lambda tup:tup[2])
    return images[-n]


def blur_img_list(imglist, kz):
    kernelBlur = np.ones((kz,kz),np.float32) / (kz*kz)

    for imgTuple in imglist:
        imgArr = imgTuple[1]
        blurImg = cv2.filter2D(imgArr, -1, kernelBlur)
        imgTuple[1] = blurImg

    return imglist

# ************* Problem 4 (4 points) **********************
"""
### use this definition if you're in Py2. For Py3, use the
### commented out definition below.
def read_bee_traffic_csv_file(csv_file_path):
    '''
    Takes a bee traffic csv file path and returns 4 numpy
vectors. The first vector contains the time readinds in
seconds (i.e., the firs column values); the second vector
-- the float estimates of the upward bee traffic;
the third vector -- the float estimates of the downward bee
traffic, and the fourth -- the float estimates of the lateral bee
traffic.
    '''
    secsv, upv, downv, latv = [], [], [], []
    with open(csv_file_path, 'r') as instream:
        reader = csv.reader(instream, delimiter = ",")
        reader.next() #to skip the header
        for row in reader:
            secs, up, down, lat = int(row[0]), float(row[1]), \
                                  float(row[2]), float(row[3])
            secsv.append(secs)
            upv.append(up)
            downv.append(down)
            latv.append(lat)
    return np.array(secsv), np.array(upv),\
           np.array(downv), np.array(latv)

"""

def read_bee_traffic_csv_file(csv_file_path):
    '''
    Takes a bee traffic csv file path and returns 4 numpy
vectors. The first vector contains the time readinds in
seconds (i.e., the firs column values); the second vector
-- the float estimates of the upward bee traffic;
the third vector -- the float estimates of the downward bee
traffic, and the fourth -- the float estimates of the lateral bee
traffic.
    '''
    secsv, upv, downv, latv = [], [], [], []
    with open(csv_file_path, 'r') as instream:
        reader = csv.reader(instream, delimiter = ",")
        next(reader) #to skip the header
        for row in reader:
            secs, up, down, lat = int(row[0]), float(row[1]), \
                                  float(row[2]), float(row[3])
            secsv.append(secs)
            upv.append(up)
            downv.append(down)
            latv.append(lat)
    return np.array(secsv), np.array(upv),\
           np.array(downv), np.array(latv)


### change this variable accordingly.
csv_dir = 'exam02/csv/'
csv_fp_01 = csv_dir + '192_168_4_5-2018-07-01_08-00-10.csv'

def error(f, x, y):
    return sp.sum((f(x) - y) ** 2)

def fit_regression_line(x, y):
    f = sp.poly1d(sp.polyfit(x, y, 1))
    

def analyze_bee_traffic_data(csv_fp, d='u'):
    data = sp.genfromtxt(csv_fp, delimiter=',')

    # Filter based on the direction - easier here than filtering after split
    data = [row for row in data if d in row[1]]

    # Split data into x,y vectors
    x = data[:,0] 
    y = data[:,1]

    # Remove any NaN's
    if sp.sum(sp.isnan(y)) > 0: 
        x = x[~sp.isnan(y)]
        y = y[~sp.isnan(y)]

    # Fit models
    pcoeffs1, error1 = sp.polyfit(x, y, 1)
    pcoeffs2, error2 = sp.polyfit(x, y, 2)
    pcoeffs3, error3 = sp.polyfit(x, y, 3)
    pcoeffs10, error10 = sp.polyfit(x, y, 10)

    f1 = sp.poly1d(sp.polyfit(x, y, 1))
    f2 = sp.poly1d(sp.polyfit(x, y, 2))
    f3 = sp.poly1d(sp.polyfit(x, y, 3))
    f10 = sp.poly1d(sp.polyfit(x, y, 10))

    # Print Error report
    print("Bee Traffic Data Report in direction", d)
    print("Least Squares:", error(f1, x, y))
    print("sp.polyfit 2 error", error2)
    print("sp.polyfit 3 error", error3)
    print("sp.polyfit 10 error", error10)

    
    xvals = sp.linspace(0, x[-1], 1000)
    plt.scatter(x, y)
    plt.plot(xvals, f1(xvals))
    plt.plot(xvals, f2(xvals))
    plt.plot(xvals, f3(xvals))
    plt.plot(xvals, f10(xvals))




# ************* Problem 5 (2 points) **********************

def bell_curve_iq(a, b, r='m', n=2):
    coef = make_const(1 / (16 * math.sqrt(2 * math.pi)))
    eCoef = make_const(-1/2)
    eExpr = make_pwr_expr(expr=make_prod(mult_expr1=make_const(1/16),
                                         mult_expr2=make_plus(elt_expr1=make_pwr('x', 1.0), 
                                                    elt_expr2=make_const(-100))), 
                          deg=make_const(2.0))
    eExpr = make_prod(mult_expr1=eCoef, mult_expr2=eExpr)
    expr = make_prod(mult_expr1=coef, mult_expr2=eExpr)

    if r == 'm' or r == 'M':
        return midpoint_rule(expr, a, b, n)
    elif r == 's' or r == 'S':
        return simpson_rule(expr, a, b, n)
    elif r == 't' or r == 'T':
        return trapezoidal_rule(expr, a, b, n)
    else:
        print("Invalid estimation rule:",r )
        return




if __name__ == '__main__':
    test_01()
    test_02()

    
