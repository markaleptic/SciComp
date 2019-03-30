#!/usr/bin/python
# -*- coding: utf-8 -*-

#############################################################
# module: unit_tests.py
##############################################################


import unittest
from hw09_s19 import display_csv_file, read_csv_file, plot_bee_traffic, sp_approx
from hw09_s19 import bee_traffic_stats, find_smallest_up_down_gap_file
from hw09_s19 import find_largest_up_down_gap_file, find_max_up_file, find_min_up_file
from hw09_s19 import find_max_down_file, find_min_down_file, find_max_lat_file, find_min_lat_file
from hw09_s19 import getDirEstimates

class Assign09UnitTests(unittest.TestCase):
    def test_01(self):
        print('\n***** Test 01 *****')
        display_csv_file('bee_traffic_estimates/192_168_4_5-2018-07-01_08-00-10.csv')
        print('Test 01: pass')

    def test_02(self):
        print('\n***** Test 02 *****')
        #plot_bee_traffic('bee_traffic_estimates/192_168_4_5-2018-07-01_08-00-10.csv')
        print('Test 02: pass')

    def test_03(self):
        print('\n***** Test 03 *****')
        print(sp_approx(lambda x: x**2, 0, 2, 10))
        print('Test 03: pass')

    def test_04(self):
        print('\n***** Test 04 *****')
        print(sp_approx(lambda x: x**3, 1, 5, 100))
        print('Test 04: pass')

    def test_05(self):
        print('\n***** Test 05 *****')
        fd = read_csv_file('bee_traffic_estimates/192_168_4_5-2018-07-02_16-30-10.csv')
        stats = bee_traffic_stats(fd)
        print(stats)
        gt = (40.47142857141933, 56.028571428527336, 27.357142857131997)
        err = 0.001
        for i in range(len(stats)):
            assert abs(stats[i] - gt[i]) <= err
        print('Test 05: pass')

    def test_06(self):
        print('\n***** Test 06 *****')
        fd = read_csv_file('bee_traffic_estimates/192_168_4_5-2018-07-01_14-00-10.csv')
        stats = bee_traffic_stats(fd)
        print(stats)
        gt = (38.048677248690325, 36.675132275122, 27.971428571415665)
        err = 0.001
        for i in range(len(stats)):
            assert abs(stats[i] - gt[i]) <= err
        print('Test 06: pass')

    def test_07(self):
        print('\n***** Test 07 *****')
        fd = read_csv_file('bee_traffic_estimates/192_168_4_5-2018-07-01_18-00-10.csv')
        stats = bee_traffic_stats(fd)
        print(stats)
        gt = (24.505820105825652, 22.737566137565995, 24.006349206362394)
        err = 0.001
        for i in range(len(stats)):
            assert abs(stats[i] - gt[i]) <= err
        print('Test 07: pass')

    def test_08(self):
        print('\n***** Test 08 *****')
        csv_dir = 'bee_traffic_estimates'
        df = getDirEstimates(csv_dir)
        for row in df:
            print(row[0], '\t', row[1], '\t', row[2], '\t', row[3], '\t', row[4])
        print('Test 08: pass')

    def test_09(self):
        print('\n***** Test 09 *****')
        csv_dir = 'bee_traffic_estimates'
        print(find_smallest_up_down_gap_file(csv_dir=csv_dir))
        print('Test 09: pass')
    
    def test_10(self):
        print('\n***** Test 10 *****')
        csv_dir = 'bee_traffic_estimates'
        fp, u, d, l, g = find_largest_up_down_gap_file(csv_dir=csv_dir)
        print(fp, u, d, l, g)
        plot_bee_traffic(fp)
        print('Test 10: pass')

    def test_11(self):
        print('\n***** Test 11 *****')
        csv_dir = 'bee_traffic_estimates'
        fp, u, d, l = find_max_up_file(csv_dir)
        print(fp, u, d, l)
        plot_bee_traffic(fp)
        print('Test 11: pass')

    def test_12(self):
        print('\n***** Test 12 *****')
        csv_dir = 'bee_traffic_estimates'
        fp, u, d, l = find_min_up_file(csv_dir)
        print(fp, u, d, l)
        plot_bee_traffic(fp)
        print('Test 12: pass')

    def test_13(self):
        print('\n***** Test 13 *****')
        csv_dir = 'bee_traffic_estimates'
        fp, u, d, l = find_max_down_file(csv_dir)
        print(fp, u, d, l)
        plot_bee_traffic(fp)
        print('Test 13: pass')
    
    def test_14(self):
        print('\n***** Test 14 *****')
        csv_dir = 'bee_traffic_estimates'
        fp, u, d, l = find_min_down_file(csv_dir)
        print(fp, u, d, l)
        plot_bee_traffic(fp)
        print('Test 14: pass')

    def test_15(self):
        print('\n***** Test 15 *****')
        csv_dir = 'bee_traffic_estimates'
        fp, u, d, l = find_max_lat_file(csv_dir)
        print(fp, u, d, l)
        plot_bee_traffic(fp)
        print('Test 15: pass')
    
    def test_16(self):
        print('\n***** Test 16 *****')
        csv_dir = 'bee_traffic_estimates'
        fp, u, d, l = find_min_lat_file(csv_dir)
        print(fp, u, d, l)
        plot_bee_traffic(fp)
        print('Test 16: pass')

    def runTest(self):
        pass

if __name__ == '__main__':
    unittest.main()