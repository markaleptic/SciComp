#!/usr/bin/python

import argparse
import cv2
import sys
import os
import re
## use import pickle in Py3.
import cPickle as pickle

################################
# module: hist_image_index.py
# YOUR NAME
# YOUR A#
################################


## indexing dictionary.
HIST_INDEX = {}

def hist_index_img(imgp, color_space, bin_size=8):
  ## your code here
  pass

def hist_index_img_dir(imgdir, color_space, bin_size, pick_file):
  print(imgdir)
  ## your code here
  print('indexing finished')


## ========================= Image Indexing Tests =====================
  
## change these as you see fit.
## IMGDIR is the directory where the images to be indexed are saved.
## PICDIR is the directory where pickled dictionaries are saved.
IMGDIR = '/home/vladimir/teaching/CS3430/S19/hw/hw12f/hist_indexing/images/'
PICDIR = '/home/vladimir/teaching/CS3430/S19/hw/hw12f/hist_indexing/picks/'

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
  pass


