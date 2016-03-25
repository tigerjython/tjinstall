from soundsystem import *
import math
import random
from gpanel import *

n = 5000

def mean(xval):
    sum = 0
    for i in range(n):
        sum += xval[i]
    return sum / n

def covariance(xval, k):
    cxy = 0
    for i in range(n):
       cxy += (xval[i] - xm) * (xval[(i + k) % n] - xm)
    return cxy / n

def deviation(xval):
    xm = mean(xval)
    sx = 0
    for i in range(n):
        sx += (xval[i] - xm) * (xval[i] - xm)
    sx = math.sqrt(sx / n)
    return sx

makeGPanel(-100, 1100, -11000, 11000)
drawGrid(0, 1000, -10000, 10000)
title("Press <SPACE> to repeat. Any other key to continue.")

signal = []
for i in range(5000):
    value = int(200 *  (math.sin(6.28 / 20 * i) + random.gauss(0, 4)))
    signal.append(value)
    if i == 0:
        move(i, value + 5000)
    elif i <= 1000:
        draw(i, value + 5000)

ch = 32
while ch == 32:
    openMonoPlayer(signal, 5000)
    play()
    ch = getKeyCodeWait()

title("Autocorrelation running. Please wait...")
signal1 = []
xm = mean(signal)
sigma = deviation(signal)
q = 20000 / (sigma * sigma)
for di in range(1, 5000):
    value = int(q *  covariance(signal, di))
    signal1.append(value)
title("Autocorrelation Done. Press any key to repeat.")
for i in range(1, 1000):
    if i == 1:
        move(i, signal1[i] - 5000)
    else:
        draw(i, signal1[i] - 5000)

while True:
    openMonoPlayer(signal1, 5000)
    play()
    getKeyCodeWait()

