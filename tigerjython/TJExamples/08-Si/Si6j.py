import random
from gpanel import *
import math

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
    return covariance(xval, yval)/(deviation(xval)*deviation(yval))
def shift(offset):
    signal1 = [0] * 1000
    for i in range(1000):
       signal1[i] = signal[(i + offset) % 1000]
    return signal1

makeGPanel(-10, 110, -2.4, 2.4)
title("Noisy signal. Press a key...")
drawGrid(0, 100, -2, 2.0, "lightgray")

t = 0
dt = 0.1
signal = [0] * 1000
while t < 100:
    y = 0.1 * math.sin(t) # Pure signal
#    noise = 0
    noise = random.gauss(0, 0.2)
    z = y + noise
    if t == 0:
        move(t, z + 1)
    else:
        draw(t, z + 1)
    signal[int(10 * t)] = z
    t += dt

getKeyWait()
title("Signal after autocorrelation")
for di in range(1, 1000):
    y = correlation(signal, shift(di))
    if di == 1:
        move(di / 10, y - 1)
    else:
        draw(di / 10, y - 1)

