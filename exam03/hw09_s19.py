#!/usr/bin/python

####################################
# module: hw09_s19.py
# Mark Allred
# A01647260
####################################

import os
import sys
import csv
# import matplotlib
# matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np


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

def display_csv_file(csv_file_path):
    '''
    print contents of a csv file passed to the function row by row.
    '''
    with open(csv_file_path, 'r') as instream:
        reader = csv.reader(instream, delimiter = ",")
        for row in reader:
            print(row)

def read_csv_file(csv_file_path):
    '''
    Convert csv file into dictionary with seconds as keys and 
    (up, down, lateral) tuple movements as value.
    '''
    fd = {}
    with open(csv_file_path, 'r') as instream:
        reader = csv.reader(instream, delimiter = ",")
        next(reader) #to skip the header
        for row in reader:
            secs, up, down, lat = int(row[0]), float(row[1]), \
                                  float(row[2]), float(row[3])
            fd[secs] = (up, down, lat)
    return fd

def plot_bee_traffic(csv_fp):
    '''
    Plots upward, downward, and lateral movements over time (seconds).
    '''
    data = read_csv_file(csv_file_path=csv_fp)
    
    # Generate plotting values
    xvals = list(data.keys())
    yUpMove      = [data[key][0] for key in data]
    yDownMove    = [data[key][1] for key in data]
    yLateralMove = [data[key][2] for key in data]

    # Generate plot
    fig = plt.figure(1)
    
    fig.suptitle('Bee traffic for %s' % csv_fp)
    plt.grid()
    plt.xlabel('t (seconds)')
    plt.ylabel('moving bees')
    plt.plot(xvals, yUpMove, label='upward', c='r')
    plt.plot(xvals, yDownMove, label='downward', c='g')
    plt.plot(xvals, yLateralMove, label='lateral', c='b')
    plt.legend(loc='best')
    plt.show()


def sp_approx(f, a, b, n):
    '''
    Simpsons Rule approximation for area under a curve. Returns estimated area.
    
    f - Anonymous / lambda function to evaluate a given x value

    a - Lower bound, float

    b - Upper bound, float

    n - Number of intervals, float
    '''
    dx = (b - a) / n
    xvals = np.array([a + i * dx for i in range(n + 1)], dtype=np.float32)
    yvals = np.zeros(n+1, dtype=np.float32)
    for i in range(n + 1):
        if i == 0 or i == n:
            yvals[i] = f(xvals[i])
        elif i % 2 == 0:
            yvals[i] = 2 * f(xvals[i])
        elif i % 2 == 1:
            yvals[i] = 4 * f(xvals[i])
        else:
            print("%d error" % i)
    approx = np.sum(yvals) * (dx / 3.0)
    return approx


def bee_traffic_estimate(t, md='u', fd={}):
  assert md == 'u' or md == 'd' or md == 'l'
  vals = fd.get(int(t))
  if vals is None:
    return None
  elif md == 'u':
    return vals[0]
  elif md == 'd':
    return vals[1]
  elif md == 'l':
    return vals[2]

def make_bee_traffic_estimator(fd, md):
  assert md == 'u' or md == 'd' or md == 'l'
  return lambda t: bee_traffic_estimate(t, md=md, fd=fd)


def bee_traffic_stats(fd):
    '''
    Takes a dictionary returned by read_csv_file and returns 
    three directional bee traffic level approximations by 
    using sp_approx to integrate the appropriate functions 
    over the interval [5, 28] with a partition of 23 
    subintervals
    '''
    up_bte = make_bee_traffic_estimator(fd, 'u')
    down_bte = make_bee_traffic_estimator(fd, 'd')
    lat_bte = make_bee_traffic_estimator(fd, 'l')
    return (sp_approx(up_bte, 5, 28, 23), 
            sp_approx(down_bte, 5, 28, 23), 
            sp_approx(lat_bte, 5, 28, 23))

def getDirEstimates(csv_dir, sortCol=1):
    '''
    Takes path to .csv files and generates up, down, and lateral estimates for each file.
    Determines absolute difference between upward and downward movement. Return 5-tuples 
    of file path, up, down, late, and gap. Dataframe is sorted in ascending order by gap.
    '''
    # Initialize empty np array
    fileEstimates = np.empty([0, 5], dtype=object)

    # Create estimates and append to np array
    for file in generate_file_names('.csv', csv_dir):
        fd = read_csv_file(file)
        up, down, lat = bee_traffic_stats(fd=fd)
        gap = abs(up - down)
        rowData = np.array([[file, up, down, lat, gap]], dtype=object)
        fileEstimates = np.append(fileEstimates, rowData, axis=0)

    # Sort array by gap values in ascending order
    fileEstimates = fileEstimates[fileEstimates[:,sortCol].argsort()]

    return fileEstimates


def find_smallest_up_down_gap_file(csv_dir):
    gapCol = 4
    df = getDirEstimates(csv_dir=csv_dir, sortCol=gapCol)
    minRow = tuple(df[0])   # Select min (sorted array so first) element
    return minRow


def find_largest_up_down_gap_file(csv_dir):
    gapCol = 4
    df = getDirEstimates(csv_dir=csv_dir, sortCol=gapCol)
    maxRow = tuple(df[-1])  # Select max (sorted array so last) element
    return maxRow

############################

def find_max_up_file(csv_dir):
    upCol = 1
    df = getDirEstimates(csv_dir=csv_dir, sortCol=upCol)
    maxRow = df[-1]   # Select max (sorted array so last) element
    maxRow = maxRow[:-1]  # Remove gap value from array to return 4-tuple
    return tuple(maxRow)

def find_min_up_file(csv_dir):
    upCol = 1
    df = getDirEstimates(csv_dir=csv_dir, sortCol=upCol)
    minRow = df[0]    # Select min (sorted array so first) element
    minRow = minRow[:-1]  # Remove gap value from array to return 4-tuple
    return tuple(minRow)

###########################

def find_max_down_file(csv_dir):
    downCol = 2
    df = getDirEstimates(csv_dir=csv_dir, sortCol=downCol)
    maxRow = df[-1]   # Select max (sorted array so last) element
    maxRow = maxRow[:-1]  # Remove gap value from array to return 4-tuple
    return tuple(maxRow)

def find_min_down_file(csv_dir):
    downCol = 2
    df = getDirEstimates(csv_dir=csv_dir, sortCol=downCol)
    minRow = df[0]    # Select min (sorted array so first) element
    minRow = minRow[:-1]  # Remove gap value from array to return 4-tuple
    return tuple(minRow)

############################

def find_max_lat_file(csv_dir):
    latCol = 3
    df = getDirEstimates(csv_dir=csv_dir, sortCol=latCol)
    maxRow = df[-1]   # Select max (sorted array so last) element
    maxRow = maxRow[:-1]  # Remove gap value from array to return 4-tuple
    return tuple(maxRow)

def find_min_lat_file(csv_dir):
    latCol = 3
    df = getDirEstimates(csv_dir=csv_dir, sortCol=latCol)
    minRow = df[0]    # Select min (sorted array so first) element
    minRow = minRow[:-1]  # Remove gap value from array to return 4-tuple
    return tuple(minRow)


  
