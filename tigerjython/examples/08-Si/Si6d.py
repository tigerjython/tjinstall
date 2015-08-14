from random import randint
from gpanel import *

z = 10000 # number of double rolls

def dec2(x):
    return str(round(x, 2))

def mean(xval):
    n = len(xval)
    sum = 0
    for i in range(n):
        sum += xval[i]
    return sum / n

makeGPanel(-1, 8, -1, 8)
title("Double rolls. Independent random variables")
addStatusBar(30)
drawGrid(0, 7, 0, 7, 7, 7, "gray")

xval =  [0] * z
yval =  [0] * z
xyval = [0] * z

for i in range(z):
    a = randint(1, 6)
    b = randint(1, 6)
    xval[i] = a
    yval[i] = b
    xyval[i] = xval[i] * yval[i]
    move(xval[i], yval[i])
    fillCircle(0.2)

xm = mean(xval)
ym = mean(yval)
xym = mean(xyval)
setStatusText("E(x) = " + dec2(xm) + \
          ",  E(y) = " + dec2(ym) + \
          ",  E(x, y) = " + dec2(xym))

