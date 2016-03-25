from random import randint
from gpanel import *
import math

z = 10000 # number of double rolls
k = 10 # scalefactor

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

def deviation(xval):
    n = len(xval)
    xm = mean(xval)
    sx = 0
    for i in range(n):
        sx += (xval[i] - xm) * (xval[i] - xm)
    sx = math.sqrt(sx / n)
    return sx

def correlation(xval, yval):
    return covariance(xval, yval) / (deviation(xval) * deviation(yval))
    
makeGPanel(-1 * k, 11 * k, -2 * k, 14 * k)
title("Double rolls. Independent random variables.")
addStatusBar(30)
drawGrid(0, 10 * k, 0, 13 * k, 10, 13, "gray")

xval =  [0] * z
yval =  [0] * z
xyval = [0] * z

for i in range(z):
    a = k * randint(1, 6)
    b = k * randint(1, 6)
    xval[i] = a
    yval[i] = a + b
    xyval[i] = xval[i] * yval[i]
    move(xval[i], yval[i])
    fillCircle(0.2 * k)

xm = mean(xval)
ym = mean(yval)
xym = mean(xyval)
c = xym - xm * ym
setStatusText("E(x) = " + dec2(xm) + \
          ",  E(y) = " + dec2(ym) + \
          ",  E(x, y) = " + dec2(xym) + \
          ",  covariance = " + dec2(covariance(xval, yval)) + \
          ",  correlation = " + dec2(correlation(xval, yval)))

