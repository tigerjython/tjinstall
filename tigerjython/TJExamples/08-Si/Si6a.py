import random
from gpanel import *

z = 10000
    
makeGPanel(-1, 11, -1, 11)
title("Uuniformly distributed value pairs")
drawGrid(10, 10, "gray")

xval = [0] * z
yval = [0] * z

for i in range(z):
    xval[i] = 10 * random.random()
    yval[i] = 10 * random.random()
    move(xval[i], yval[i])
    fillCircle(0.03)

