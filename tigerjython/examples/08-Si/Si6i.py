import random
from gpanel import *
import math

z = 1000
a = 0.6
b = 2

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

sigma = 1
    
makeGPanel(-1, 11, -1, 11)
title("Simulate data points. Press a key...")
addStatusBar(30)
drawGrid(0, 10, 0, 10, "gray")
setStatusText("Press any key")

xval = [0] * z
yval = [0] * z

for i in range(z):
    x = i / 100
    xval[i] = x 
    yval[i] = f(x) + random.gauss(0, sigma)
    move(xval[i], yval[i])
    fillCircle(0.03)

getKeyWait()
xm = mean(xval)
ym = mean(yval)
move(xm, ym)
lineWidth(3)
circle(0.5)

def g(x):
    y = m * (x - xm) + ym
    return y

def errorSum():
    sum = 0
    for i in range(z):
        x = i / 100
        sum += (yval[i] - g(x)) * (yval[i] - g(x))
    return sum

m = 0
setColor("red")
lineWidth(1)
error_min = 0
while m < 5:
    line(0, g(0), 10, g(10))
    if m == 0:
        error_min = errorSum()
    else:
        if errorSum() < error_min:
            error_min = errorSum()
        else:
            break
    m += 0.01

title("Regression line found")
setColor("blue")
lineWidth(3)
line(0, g(0), 10, g(10))
setStatusText("Found slope: " +  dec2(m) + \
               ", Theory: " + dec2(covariance(xval, yval) 
              /(deviation(xval) * deviation(xval))))

