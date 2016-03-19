#!/usr/bin/env python
from math import *

def readFile(filename):
    res = []
    with open(filename) as f:
        for line in f.readlines():
            if line[0] == '#':
                continue
            ls = line.split('\t')
            if len(ls) != 2:
                print("Bad line:", line, ls)
            res = res + [(float(ls[0]), float(ls[1]))]
    return res

def linearErrors(xs, ys, a_0, a_1):
    o_y = sqrt(sum([(y - (a_0 + a_1 * x))**2 for (x, y) in zip(xs, ys)]) / (len(xs) - 2))
    xs2 = [x * x for x in xs]
    d = len(xs) * sum(xs2) - sum(xs) ** 2
    da_0 = o_y * sqrt(sum(xs2) * 1.0 / d)
    da_1 = o_y * sqrt(len(xs) * 1.0 / d)
    return da_0, da_1

xs = [-180, -135, -90, -45, 45, 90, 135, 180]
ys = [-0.09, -0.19, -0.29, -0.39, 0.1, 0.2, 0.3, 0.39]
#o_y = 0.03
a_0 = 0.00375
a_1 = 0.00217
_, da_1 = linearErrors(xs, ys, a_0, a_1)
#print("A1:", da_1)

xs = [0, 0.08, 0.11, 0.15, 0.19] * 2
ys = [0.714, 1.23, 1.505, 2.05, 2.54] + [0.717, 1.24, 1.569, 2.06, 2.55]
xs = [2 * 0.049 * x**2 for x in xs]
ys = [y**2 for y in ys]
a_0 = 0.46
a_1 = 1697

#xs = [1, 2, 3]
#ys = [1, 2, 3.1]
#a_0 = 0
#a_1 = 1

da_0, da_1 = linearErrors(xs, ys, a_0, a_1)
print("A2:", da_0, ";", da_1)

xs, ys = zip(*sorted(readFile("A4.txt")))
a_0 = 0.06
a_1 = 0.128
da_0, da_1 = linearErrors(xs, ys, a_0, a_1)
print("A4:", da_0, ";", da_1)

#dd = sqrt(0.002 ** 2 * (180/pi * 2.17e-3) ** 2 + 9e-5 ** 2 * (180/pi * 0.19) ** 2)
#print("d:", dd)
