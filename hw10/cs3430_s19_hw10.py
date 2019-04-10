#!/usr/bin/python

import math
from PIL import Image 
# import Image


#######################################################
# module: cs3430_s19_hw10.py
# Mark Allred
# A01647260
########################################################

##################### Problem 1 (4 points) ####################
WHITE = 255 # Edge Pixel
BLACK = 0   # Non-edge Pixel

## a function to convert an rgb 3-tuple to a grayscale value.
def luminosity(rgb, rcoeff=0.2126, gcoeff=0.7152, bcoeff=0.0722):
    return rcoeff*rgb[0]+gcoeff*rgb[1]+bcoeff*rgb[2]

def save_gd_edges(input_fp, output_fp, magn_thresh=20):
    input_image  = Image.open(input_fp)
    output_image = gd_detect_edges(input_image, magn_thresh=magn_thresh)
    output_image.save(output_fp)
    del input_image
    del output_image

def gd_detect_edges(rgb_img, magn_thresh=20):
    """Return image array with edge pixels in white and non-edge pixels in black based on the magnitude threshold."""
    
    img_edges = Image.new("L", rgb_img.size, color=BLACK)
   
    # Iterate over the pixels in the image ignoring borders
    for row in range(1, rgb_img.size[0] - 1):
        for col in range(1, rgb_img.size[1] - 1):
            
            # Calculate change in luminosity from above to below and left to right of the pixel.
            dy = luminosity(rgb=rgb_img.getpixel((row - 1, col))) - luminosity(rgb=rgb_img.getpixel((row + 1, col)))
            dx = luminosity(rgb=rgb_img.getpixel((row, col - 1))) - luminosity(rgb=rgb_img.getpixel((row, col + 1)))
            
            # Determine if the gradient (change in luminosity) is above the edge threshold.
            if pixel_gradient(dy, dx) >= magn_thresh:
                img_edges.putpixel((row, col), WHITE)

    return img_edges

def pixel_gradient(dy, dx):
    """Returns gradient for the given pixel mask's change in luminosity."""

    return math.sqrt((dy ** 2) + (dx ** 2))

###################### Problem 2 (1 point) #####################

def cosine_sim(img1, img2):
    """Returns Cosine Similiarity measure for the two images."""

    assert img1.size == img2.size

    # If either of the images are RGB, convert them to grayscale
    img1, img2 = convert_if_rgb(img1, img2)

    num_sum = 0
    denom_img1_sum = 0
    denom_img2_sum = 0

    for row in range(img1.size[0]):
        for col in range(img1.size[1]):
            img1_pixel_val = img1.getpixel((row, col))
            img2_pixel_val = img2.getpixel((row, col))
                
            num_sum += (img1_pixel_val * img2_pixel_val)
            denom_img1_sum += (img1_pixel_val ** 2)
            denom_img2_sum += (img2_pixel_val ** 2)

    return num_sum / (math.sqrt(denom_img1_sum) * math.sqrt(denom_img2_sum))

def test_cosine_sim(img_fp1, img_fp2):
    img1 = Image.open(img_fp1)
    img2 = Image.open(img_fp2)
    sim = cosine_sim(img1, img2)
    del img1
    del img2
    print(img_fp1, img_fp2)
    print(sim)

def euclid_sim(img1, img2):
    """Returns the Euclidean Distance Measure for the two images."""

    assert img1.size == img2.size

    # If either of the images are RGB, convert them to grayscale
    img1, img2 = convert_if_rgb(img1, img2)
    
    # Calculates sumf of squared differences in the pixel values
    img_diff_sum_of_squares = 0
    for row in range(img1.size[0]):
        for col in range(img1.size[1]):
            img_diff_sum_of_squares += (img1.getpixel((row, col)) - img2.getpixel((row, col))) ** 2

    # Return Euclidean Distance
    return math.sqrt(img_diff_sum_of_squares)


def test_euclid_sim(img_fp1, img_fp2):
    img1 = Image.open(img_fp1)
    img2 = Image.open(img_fp2)
    sim = euclid_sim(img1, img2)
    del img1
    del img2
    print(img_fp1, img_fp2)
    print(sim)

def jaccard_sim(img1, img2):
    """Returns Jaccard similarity coefficient for the two images."""

    assert img1.size == img2.size

    # If either of the images are RGB, convert them to grayscale
    img1, img2 = convert_if_rgb(img1, img2)
    
    # Create empty sets to add dynamically
    img1_set = set()
    img2_set = set()

    # Add pixel values to set - set Object maintains uniqueness of items in set
    for row in range(img1.size[0]):
        for col in range(img1.size[1]):
            img1_set.add(img1.getpixel((row, col)))
            img2_set.add(img2.getpixel((row, col)))

    return len(img1_set.intersection(img2_set)) / len(img1_set.union(img2_set))


def test_jaccard_sim(img_fp1, img_fp2):
    img1 = Image.open(img_fp1)
    img2 = Image.open(img_fp2)
    sim = jaccard_sim(img1, img2)
    del img1
    del img2
    print(img_fp1, img_fp2)
    print(sim)

# Keeping it DRY
def convert_if_rgb(img1, img2):
    """Returns grayscaled images if the images are RGB"""
    is_rgb = isinstance(img1.getpixel((0,0)), tuple) or \
             isinstance(img2.getpixel((0,0)), tuple)
    if is_rgb:
        img1 = img1.convert("L")
        img2 = img2.convert("L")

    return img1, img2


def test_01():
    save_gd_edges('img/1b_bee_01.png', 'img/1b_bee_01_ed.png', magn_thresh=20)
    save_gd_edges('img/1b_bee_10.png', 'img/1b_bee_10_ed.png', magn_thresh=20)
    save_gd_edges('img/2b_nb_10.png', 'img/2b_nb_10_ed.png', magn_thresh=20)
    save_gd_edges('img/2b_nb_21.png', 'img/2b_nb_21_ed.png', magn_thresh=20)
    save_gd_edges('img/elephant.jpg', 'img/elephant_ed.jpg', magn_thresh=20)
    save_gd_edges('img/output11885.jpg', 'img/output11885_ed.jpg', magn_thresh=20)
    save_gd_edges('img/2b_nb_09.png', 'img/2b_nb_09_ed.png', magn_thresh=20)
    save_gd_edges('img/output11884.jpg', 'img/output11884_ed.jpg', magn_thresh=20)


## testing the PIL/PILLOW installation
def test_02():
    img = Image.open('img/1b_bee_01.png').convert('LA')
    img2 = img.save('img/1b_bee_01_gray.png')
    del img
    del img2
    
def test_03():
    test_cosine_sim('img/2b_nb_09_ed.png', 'img/2b_nb_09_ed.png')
    test_cosine_sim('img/2b_nb_09_ed.png', 'img/2b_nb_10_ed.png')
    test_cosine_sim('img/output11884_ed.jpg', 'img/output11885_ed.jpg')
    test_cosine_sim('img/output11885_ed.jpg', 'img/output11884_ed.jpg')

def test_04():
    test_euclid_sim('img/2b_nb_10_ed.png', 'img/2b_nb_10_ed.png')
    test_euclid_sim('img/2b_nb_09_ed.png', 'img/2b_nb_10_ed.png')
    test_euclid_sim('img/2b_nb_10_ed.png', 'img/2b_nb_09_ed.png')

def test_05():
    test_jaccard_sim('img/2b_nb_10_ed.png', 'img/2b_nb_10_ed.png')
    test_jaccard_sim('img/2b_nb_09_ed.png', 'img/2b_nb_10_ed.png')
    test_jaccard_sim('img/2b_nb_10_ed.png', 'img/2b_nb_09_ed.png')
    test_jaccard_sim('img/output11885_ed.jpg', 'img/output11884_ed.jpg')
    test_jaccard_sim('img/output11884_ed.jpg', 'img/output11885_ed.jpg')


if __name__ == '__main__':
    print("Test 1: ")
    test_01()
    print("Test 1 complete, proceeding to test 2")
    test_02()
    print("Test 2 complete, proceeding to test 3")
    test_03()
    print("Test 3 complete, proceeding to test 4")
    test_04()
    print("Test 4 complete, proceeding to test 5")
    test_05()
    print("Test 5 complete. All tests complete.")

