#!/usr/bin/python

import argparse
import cv2
import sys
import os
import re
## use import pickle in Py3.
#import cPickle as pickle
import pickle

################################
# module: hist_image_index.py
# Mark Allred
# A01647260
################################


## indexing dictionary.
HIST_INDEX = {}

def hist_index_img(imgp, color_space, bin_size=8):
    print("indexing", imgp.split('/')[-1])
    image = cv2.imread(imgp)
    assert image is not None

    if color_space.lower() == 'rgb' or color_space.lower() == 'bgr':
        hist = cv2.calcHist([image], [0, 1, 2], None, [bin_size, bin_size, bin_size], [0, 256, 0, 256, 0, 256])
        norm_hist = cv2.normalize(hist, hist).flatten()
        HIST_INDEX[imgp] = norm_hist
        del hist
        del norm_hist
    elif color_space.lower() == 'hsv':
        image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        hist = cv2.calcHist([image], [0, 1, 2], None, [bin_size, bin_size, bin_size], [0, 180, 0, 256, 0, 256])
        norm_hist = cv2.normalize(hist, hist).flatten()
        HIST_INDEX[imgp] = norm_hist
        del hist
        del norm_hist
    else:
        print("Incorrect color space provided", color_space)

    print(imgp.split('/')[-1], "indexed")
  

def hist_index_img_dir(imgdir, color_space, bin_size, pick_file):
    print(imgdir)
    for image in os.listdir(imgdir):
        if image.endswith('.JPG') or image.endswith('.png') or image.endswith('.jpg') or image.endswith('.jpeg'):
            hist_index_img(imgdir + image, color_space, bin_size)
    histFile = open(pick_file,'ab')
    pickle.dump(HIST_INDEX, histFile)
    histFile.close()
    print('indexing finished')


## ========================= Image Indexing Tests =====================
  
## change these as you see fit.
## IMGDIR is the directory where the images to be indexed are saved.
## PICDIR is the directory where pickled dictionaries are saved.
IMGDIR = '/Users/mark/Documents/School/15-Spring 2019/Python/Homework/hw12/images/'
PICDIR = '/Users/mark/Documents/School/15-Spring 2019/Python/Homework/hw12/pickles/'

def test_01():
    HIST_INDEX = {}
    hist_index_img_dir(IMGDIR, 'rgb', 8, PICDIR + 'rgb_hist8.pck')

def test_02(): 
    HIST_INDEX = {}
    hist_index_img_dir(IMGDIR, 'rgb', 16, PICDIR + 'rgb_hist16.pck')

def test_03():
    HIST_INDEX = {}
    hist_index_img_dir(IMGDIR, 'hsv', 8, PICDIR + 'hsv_hist8.pck')

def test_04():
    HIST_INDEX = {}
    hist_index_img_dir(IMGDIR, 'hsv', 16, PICDIR + 'hsv_hist16.pck')


if __name__ == '__main__':
    # test_01()
    # test_02()
    test_03()
    test_04()