#!/usr/bin/python

########################################
# module: cs3430_s19_hw11.py
# Mark Allred
# A01642760
########################################

## add your imports here
import math
from PIL import Image
# import Image
import sys
import os
import numpy as np
import cv2
from deriv import deriv
from tof import tof
from const import const
from var import var
from pwr import pwr
from maker import make_const, make_pwr, make_prod, make_quot
from maker import make_plus, make_ln, make_absv
from maker import make_pwr_expr, make_e_expr
from plus import plus
from prod import prod

################# Problem 1 (1 point) ###################

def nra(poly_fexpr, g, n):
    assert isinstance(g, const)
    assert isinstance(n, const)
    assert poly_fexpr is not None

    fexpr_func = tof(poly_fexpr)
    assert fexpr_func is not None

    poly_deriv = deriv(poly_fexpr)
    deriv_func = tof(poly_deriv)
    assert deriv_func is not None

    old_guess = g.get_val()
    new_guess = 0

    for i in range(n.get_val()):
        new_guess = old_guess - (fexpr_func(old_guess) / deriv_func(old_guess))
        old_guess = new_guess

    return make_const(new_guess)


################# Unit Tests for Problem 1 ###################

def nra_ut_01():
    ''' Approximating x^2 - 2 = 0. '''
    fexpr = make_plus(make_pwr('x', 2.0),
                      make_const(-2.0))
    print(nra(fexpr, make_const(1.0), make_const(10000)))

def nra_ut_02():
    ''' Approximating x^2 - 3 = 0. '''
    fexpr = make_plus(make_pwr('x', 2.0),
                      make_const(-3.0))
    print(nra(fexpr, make_const(1.0), make_const(10000)))

def nra_ut_03():
    ''' Approximating x^2 - 5 = 0. '''
    fexpr = make_plus(make_pwr('x', 2.0),
                      make_const(-5.0))
    print(nra(fexpr, make_const(1.0), make_const(10000)))

def nra_ut_04():
    ''' Approximating x^2 - 7 = 0. '''
    fexpr = make_plus(make_pwr('x', 2.0),
                      make_const(-7.0))
    print(nra(fexpr, make_const(1.0), make_const(10000)))

def nra_ut_05():
    ''' Approximating e^-x = x^2. '''
    fexpr = make_e_expr(make_prod(make_const(-1.0),
                                  make_pwr('x', 1.0)))
    fexpr = make_plus(fexpr,
                      make_prod(make_const(-1.0),
                                make_pwr('x', 2.0)))
    print(nra(fexpr, make_const(1.0), make_const(10000)))

def nra_ut_06():
    ''' Approximating 11^{1/3}.'''
    fexpr = make_pwr('x', 3.0)
    fexpr = make_plus(fexpr,
                      make_const(-11.0))
    print(nra(fexpr, make_const(1.0), make_const(10000)))

def nra_ut_07():
    ''' Approximating 6^{1/3}.'''
    fexpr = make_pwr('x', 3.0)
    fexpr = make_plus(fexpr,
                      make_const(-6.0))
    print(nra(fexpr, make_const(1.0), make_const(10000)))

def nra_ut_08():
    ''' Approximating x^3 + 2x + 2. '''
    fexpr = make_pwr('x', 3.0)
    fexpr = make_plus(fexpr,
                      make_prod(make_const(2.0),
                                make_pwr('x', 1.0)))
    fexpr = make_plus(fexpr, make_const(2.0))
    print(nra(fexpr, make_const(1.0), make_const(10000)))

def nra_ut_09():
    ''' Approximating x^3 + x - 1. '''
    fexpr = make_pwr('x', 3.0)
    fexpr = make_plus(fexpr, make_pwr('x', 1.0))
    fexpr = make_plus(fexpr, make_const(-1.0))
    print(nra(fexpr, make_const(1.0), make_const(10000)))

def nra_ut_10():
    ''' Approximating e^(5-x) = 10 - x. '''
    fexpr = make_e_expr(make_plus(make_const(5.0),
                                  make_prod(make_const(-1.0),
                                            make_pwr('x', 1.0))))
    fexpr = make_plus(fexpr, make_pwr('x', 1.0))
    fexpr = make_plus(fexpr, make_const(-10.0))
    print(nra(fexpr, make_const(1.0), make_const(10000)))


# =================== Problem 2 (4 points) ===================
BLACK = 0
WHITE = 255

def ht_detect_lines(img_fp, magn_thresh=20, spl=20):
    assert os.path.isfile(img_fp)
    image_arr = cv2.imread(img_fp)
    img_shape = image_arr.shape
    
    # Image Array for image with edges colored white and nonedges colored black
    image_bw_edges = np.zeros((img_shape[0] - 1, img_shape[1] - 1))

    # Hough Accumulator Construction
    theta_ubound = 181 # 180 degrees + 1 to account for range(n) yielding n-1 rather than n.
    rho_ubound   = int(math.sqrt(img_shape[0] ** 2 + img_shape[1] ** 2))
    hough_table  = np.zeros((rho_ubound, theta_ubound)) # (theta_ubound, rho_ubound))
    convert_to_degrees = np.pi / 180    # np.cos / sin default to radians

    # Iterate over the pixels in the image ignoring borders for calculations
    for row in range(1, image_arr.shape[0] - 1):
        for col in range(1, image_arr.shape[1] - 1):
            
            # Calculate change in luminosity about a pixel -> above to below and left to right of the pixel.
            dy = luminosity(rgb=image_arr[row - 1, col]) - luminosity(rgb=image_arr[row + 1, col])
            dx = luminosity(rgb=image_arr[row, col - 1]) - luminosity(rgb=image_arr[row, col + 1])
            gradient = pixel_gradient(dy, dx)
            
            # Determine if the gradient (change in luminosity) is above the edge threshold.
            if gradient >= magn_thresh:
                # Set pixel color in image with edges colored white
                image_bw_edges[row, col] = WHITE

                # Conduct accumulator array voting
                for theta in range(theta_ubound):
                    rho = int(row * np.cos(theta * convert_to_degrees) + col * np.sin(theta * convert_to_degrees))
                    hough_table[rho, theta] += 1 # hough_table[theta, rho] += 1


    # Iterate over accumulator values and place lines on the image if the vote is above the threshold
    image_with_lines = image_arr[:]     # Create separate image to hold lines

    for theta in range(theta_ubound):
        for rho in range(rho_ubound):
            if hough_table[rho, theta] > spl:   # if hough_table[theta, rho] > spl:
                b = np.cos(theta * convert_to_degrees) 
                a = np.sin(theta * convert_to_degrees)
                x0 = a * rho
                y0 = b * rho
                x1 = int(x0 + 1000 * (-b))
                y1 = int(y0 + 1000 * (a))
                x2 = int(x0 - 1000 * (-b))
                y2 = int(y0 - 1000 * (a))
                cv2.line(image_with_lines, (x1, y1), (x2, y2), (255, 0, 0), 2)

    return (image_arr, image_with_lines, image_bw_edges, hough_table)


def pixel_gradient(dy, dx):
    """Returns gradient for the given pixel mask's change in luminosity."""

    return math.sqrt((dy ** 2) + (dx ** 2))


def luminosity(rgb, rcoeff=0.2126, gcoeff=0.7152, bcoeff=0.0722):
    """Returns grayscale value a BGR 3-tuple."""

    return rcoeff*rgb[2]+gcoeff*rgb[1]+bcoeff*rgb[0]

################ Unit Tests for Problem 2 ####################
##        
## I used Image for edge detection and numpy image representation
## to draw lines. Hence, I am using cv2.imwrite to save the
## image with drawn line (lnimg) and image.save to save the image
## with the edges. Feel free to modify but keep the signatures
## of these tests the same.

def ht_test_abstract(img_fp, magn_thresh, spl):
    img, lnimg, edimg, ht = ht_detect_lines(img_fp, magn_thresh=magn_thresh, spl=spl)
    ht = cv2.equalizeHist(ht.astype(np.uint8))  # Creates image of Houghtable with equalized light
    fileparts = img_fp.split('.')
    if len(fileparts) != 2:
        print("Unable to save image files. Please use absolute file paths for test.")
        print("File path provided: " + img_fp)
        return

    img_path = fileparts[0]
    ftype = fileparts[1]

    # Write all the new images to the path and clear memory
    cv2.imwrite(img_path + '_ln.' + ftype, lnimg)
    cv2.imwrite(img_path + '_ed.' + ftype, edimg)
    cv2.imwrite(img_path + '_ht.' + ftype, ht)
    del img
    del lnimg
    del edimg
    del ht

def ht_test_01(img_fp, magn_thresh=20, spl=150):
    ht_test_abstract(img_fp, magn_thresh=magn_thresh, spl=spl)

def ht_test_02(img_fp, magn_thresh=100, spl=190):
    ht_test_abstract(img_fp, magn_thresh=magn_thresh, spl=spl)

def ht_test_03(img_fp, magn_thresh=150, spl=110):
    ht_test_abstract(img_fp, magn_thresh=magn_thresh, spl=spl)

def ht_test_04(img_fp, magn_thresh=50, spl=200):
    ht_test_abstract(img_fp, magn_thresh=magn_thresh, spl=spl)

def ht_test_05(img_fp, magn_thresh=35, spl=100):
    ht_test_abstract(img_fp, magn_thresh=magn_thresh, spl=spl)

def ht_test_06(img_fp, magn_thresh=35, spl=100):
    ht_test_abstract(img_fp, magn_thresh=magn_thresh, spl=spl)

def ht_test_07(img_fp, magn_thresh=15, spl=180):
    ht_test_abstract(img_fp, magn_thresh=magn_thresh, spl=spl)

def ht_test_08(img_fp, magn_thresh=20, spl=450):
    ht_test_abstract(img_fp, magn_thresh=magn_thresh, spl=spl)

def ht_test_09(img_fp, magn_thresh=30, spl=400):
    ht_test_abstract(img_fp, magn_thresh=magn_thresh, spl=spl)

def ht_test_10(img_fp, magn_thresh=10, spl=250):
    ht_test_abstract(img_fp, magn_thresh=magn_thresh, spl=spl)

def ht_test_11(img_fp, magn_thresh=10, spl=210):
    ht_test_abstract(img_fp, magn_thresh=magn_thresh, spl=spl)

def ht_test_12(img_fp, magn_thresh=5, spl=205):
    ht_test_abstract(img_fp, magn_thresh=magn_thresh, spl=spl)
    
if __name__ == '__main__':
    # nra_ut_01()
    # nra_ut_02()
    # nra_ut_03()
    # nra_ut_04()
    # nra_ut_05()
    # nra_ut_06()
    # nra_ut_07()
    # nra_ut_08()
    # nra_ut_09()
    # nra_ut_10()
    # ht_test_01('img_test/EdgeImage_01.jpg')
    # ht_test_02('img_test/EdgeImage_02.jpg')
    # ht_test_03('img_test/EdgeImage_03.jpg')
    ht_test_04('img_test/envelope.jpeg')
    # ht_test_05('img_test/horline.png')
    # ht_test_06('img_test/verline.png')
    # ht_test_07('img_test/cross.png')
    # ht_test_08('img_test/tiles.jpeg')
    # ht_test_09('img_test/kitchen.jpeg')
    # ht_test_10('img_test/road01.png')
    # ht_test_11('img_test/road02.png')
    # ht_test_12('img_test/road03.png')