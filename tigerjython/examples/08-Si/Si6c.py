import random
from gpanel import *
import math

z = 1000
a = 0.2
b = 2

def f(x):
    y = -x * (a * x - b)
    return y

makeGPanel(-1, 11, -1, 11)
title("y = -x * (0.2 * x - 2) with normally distributed noise")
drawGrid(0, 10, 0, 10, "gray")

xval = [0] * z
yval = [0] * z

for i in range(z):
    x = i / 100
    xval[i] = x
    yval[i] = f(x) + random.gauss(0, 0.5)
    move(xval[i], yval[i])
    fillCircle(0.03)

