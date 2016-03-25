import random
from gpanel import *

z = 10000
    
makeGPanel(-1, 11, -1, 11)
title("Normally distributed value pairs")
drawGrid(10, 10, "gray")

xval = [0] * z
yval = [0] * z

for i in range(z):
    xval[i] = random.gauss(5, 1)
    yval[i] = random.gauss(5, 1)
    move(xval[i], yval[i])
    fillCircle(0.03)

