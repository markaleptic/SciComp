#!/usr/bin/python

#########################################
# module: hw07_s19.py
# Mark Allred
# A01647260
#########################################

import math
import numpy as np
import argparse
import cv2
import sys
import os
import re

## uses these command line options if you want to run your program
## in a command window.
#ap = argparse.ArgumentParser()
#ap.add_argument('-id', '--imgdir', required = True, help = 'image directory')
#ap.add_argument('-ft', '--ftype', required = True, help = 'file type (e.g., .png)')
#args = vars(ap.parse_args())

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

##
# Function returns list of 2-tuples. Each tuple contains full path to image and np 
# 2darray of said image. Function takes file types in the form of '.jpg' and
# directory to traverse for finding files.
def read_img_dir(ftype, imgdir):
    filesAndImages = []
    for file in generate_file_names(ftype, imgdir):
        imageArr = cv2.imread(file)
        filesAndImages.append( (file, imageArr))
    return filesAndImages


def getImageAndPath(i, imglst):
    '''
    Function returns i-th image path and image array
    '''
    # Get location of file
    imgLoc = imglst[i][0]
    # Get image np array
    imgArr = imglst[i][1]
    return imgLoc, imgArr


def grayscale(i, imglst):
    '''
    Function displays original and grayscaled image
    '''

    # Get location of file for title of image and image array
    imgLoc, imgArr = getImageAndPath(i, imglst)
    
    # Convert image to grayscale
    grayImage = cv2.cvtColor(imgArr, cv2.COLOR_RGB2GRAY)

    # Show color image
    cv2.imshow(imgLoc, imgArr)
    # Show grayscaled image
    cv2.imshow('Grayscaled', cv2.cvtColor(grayImage, cv2.COLOR_GRAY2RGB))


def split_merge(i, imglst):
    '''
    Function displays and splits an image into rgb color channels and displays each 
    color channel in that color.
    '''
    # Get location of file for title of image and image array
    imgLoc, imgArr = getImageAndPath(i, imglst)

    # Split image into channels
    b,g,r = cv2.split(imgArr)
    # Create np.zeros arrays for merging with each color chanel
    zeros = np.zeros(imgArr.shape[:2], dtype='uint8')
    # Merge zeros with each color channel to display single color image
    b = cv2.merge([b,zeros,zeros])
    g = cv2.merge([zeros,g,zeros])
    r = cv2.merge([zeros,zeros,r])

    # Show original full image
    cv2.imshow(imgLoc, imgArr)

    # Show color channel images with their color as title.
    cv2.imshow("Blue",b)
    cv2.imshow("Green",g)
    cv2.imshow("Red",r)


def amplify(i, imglst, c, amount):
    '''
    Function displays an image and a color amplifed version based on passed in color and 
    amplifcation amount.
    '''
    # Get location of file for title of image and image array
    imgLoc, imgArr = getImageAndPath(i, imglst)
    
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
    # Show original and amplified image
    cv2.imshow(imgLoc, imgArr)
    cv2.imshow("Amplified", amplifiedImage)


## here is main for you to test your implementations.
## remember to destroy all windows after you are done.
if __name__ == '__main__':
    # Convert to unittests
    # Unit test 1
    imglist = read_img_dir('.jpg', '.')
    print("Length: ", len(imglist))
    print(imglist[0][0])
    print(imglist[0][1])
    print(imglist[0][1].shape)
    
    grayscale(0, imglist)
    split_merge(0, imglist)
    amplify(0, imglist, 'b', 200)
    cv2.waitKey()
    cv2.destroyAllWindows()
