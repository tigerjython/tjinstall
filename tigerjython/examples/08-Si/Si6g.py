import random
from gpanel import *
import math

data = [["Australia", 4.8, 5.141],
        ["Austria", 8.7, 24.720],
        ["Belgium", 5.7, 9.005],
        ["Canada", 3.9, 6.253],
        ["Denmark", 8.2, 24.915],
        ["Finland", 6.8, 7.371],
        ["France", 6.6, 9.177],
        ["Germany", 11.6, 12.572],
        ["Greece", 2.5, 1.797],
        ["Italy", 4.1, 3.279],
        ["Ireland", 8.8, 12.967],
        ["Netherlands", 4.5, 11.337],
        ["Norway", 9.2, 21.614],
        ["Poland", 2.7, 3.140],
        ["Portugal", 2.7, 1.885],
        ["Spain", 3.2, 1.705],
        ["Sweden", 6.2, 30.300],
        ["Switzerland", 11.9, 30.949],
        ["United Kingdom", 9.8, 19.165],
        ["United States", 5.3, 10.811]]

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

makeGPanel(-2, 17, -5, 55)
drawGrid(0, 15, 0, 50, "lightgray")

xval = []
yval = []

for country in data:
    d = country[1]
    v = country[2]
    xval.append(d)
    yval.append(v)   
    move(d, v)
    fillCircle(0.2)
    text(country[0])

title("Chocolate-Brainpower-Correlation: " + dec2(correlation(xval, yval)))
