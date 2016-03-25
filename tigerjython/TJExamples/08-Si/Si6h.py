import random
from gpanel import *
import math

z = 1000
a = 0.6
b = 2
sigma = 1

def f(x):
    y = a * x + b
    return y

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
    
makeGPanel(-1, 11, -1, 11)
title("y = 0.6 * x + 2 normally distributed measurement errors")
addStatusBar(30)
drawGrid(0, 10, 0, 10, "gray")
setColor("blue")
lineWidth(3)
line(0, f(0), 10, f(10))

xval = [0] * z
yval = [0] * z

setColor("black")
for i in range(z):
    x = i / 100
    xval[i] = x
    yval[i] = f(x) + random.gauss(0, sigma)
    move(xval[i], yval[i])
    fillCircle(0.03)

xm = mean(xval)
ym = mean(yval)
move(xm, ym)
circle(0.5)

setStatusText("E(x) = " + dec2(xm) + \
          ",  E(y) = " + dec2(ym) + \
          ",  correlation = " + dec2(correlation(xval, yval)))

