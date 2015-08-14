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

def covariance(xval, yval):
    n = len(xval)
    xm = mean(xval)
    ym = mean(yval)
    cxy = 0
    for i in range(n):
       cxy += (xval[i] - xm) * (yval[i] - ym)
    return cxy / n
    
makeGPanel(-1, 11, -2, 14)
title("Double rolls. Independent random variables")
addStatusBar(30)
drawGrid(0, 10, 0, 13, 10, 13, "gray")

xval =  [0] * z
yval =  [0] * z
xyval = [0] * z

for i in range(z):
    a = randint(1, 6)
    b = randint(1, 6)
    xval[i] = a
    yval[i] = a + b
    xyval[i] = xval[i] * yval[i]
    move(xval[i], yval[i])
    fillCircle(0.2)

xm = mean(xval)
ym = mean(yval)
xym = mean(xyval)
c = xym - xm * ym
setStatusText("E(x) = " + dec2(xm) + \
          ",  E(y) = " + dec2(ym) + \
          ",  E(x, y) = " + dec2(xym) + \
          ",  c = " + dec2(c) + \
          ",  covariance = " + dec2(covariance(xval, yval)))

