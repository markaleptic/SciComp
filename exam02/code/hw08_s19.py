#!/usr/bin/python

#########################################
# module: hw08_s19.py
# Mark Allred
# A01647260
#########################################

### modify these as you see fit.
import math
import numpy as np
import argparse
import cv2
import sys
import os
import re


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


def read_img_dir(ftype, imgdir):
    '''
    Function returns list of 2-tuples. Each tuple contains full path to image and np 
    2d array of said image. Function takes file types in the form of '.jpg' and
    directory to traverse for finding files.
    '''
    filesAndImages = []
    for file in generate_file_names(ftype, imgdir):
        imageArr = cv2.imread(file)
        filesAndImages.append( (file, imageArr))
    return filesAndImages


def amplify(imgArr, c, amount):
    '''
    Function amplifies the specified image by amount in the given color c channel
    '''
    # Split channels for amplication
    b,g,r = cv2.split(imgArr)

    # Amplify specified color
    if c=='b' or c=='B':
        b+=amount
    elif c=='g' or c=='G':
        g+=amount
    elif c=='r' or c=='R':
        r+=amount
    else:
        print("Invalid color provided. Exiting function.")
        return
    # Combine channels to create image
    amplifiedImage = cv2.merge([b,g,r])
    
    return amplifiedImage


def amplify_grayscale_blur_img_dir(ftype, in_img_dir, kz, c, amount, appendTitle='_blur'):
    '''
    Function reads in all the images in the given directory with the specified file type, amplifies
    the given color channel, grayscales the image, blurs the image using the square mean filter sized kz, 
    and writes the new image to file with the original title plus the appendTitle.

    ftype - A string specifiying thefFile type for image, e.g. '.jpg', '.png'.

    in_img_dir - String directory location for the given images, e.g. '/home/vladimir/images/'.

    kz - Odd positive integer specifying the size of a mean blur filter.

    c - A string specifying the channel (i.e., ’b’, ’g’, or ’c’)

    amount - Non-negative integer specifying the amount of amplification on the specified channel

    appendTitle - String specifiying the title to append to the original images file name.
    '''
    
    pathAndImages = read_img_dir(ftype, in_img_dir)

    for imageTple in pathAndImages:
        # create new image path including _blur before file extension
        imagePath = imageTple[0]
        newImagePath = imagePath[:-len(ftype)]
        newImagePath += appendTitle + ftype
        # Amplify image channel, grayscale, and perform mean blur
        imageArr = imageTple[1]
        imageArr = amplify(imageArr, c, amount)
        imageArr = cv2.cvtColor(imageArr, cv2.COLOR_RGB2GRAY)
        imageArr = cv2.blur(imageArr, (kz, kz))
        # Save image in new path
        cv2.imwrite(newImagePath, imageArr)

if __name__ == '__main__':
    # Convert to unittests
    # Unit test 1
    amplify_grayscale_blur_img_dir('.jpg', './images',3,'g', 10)