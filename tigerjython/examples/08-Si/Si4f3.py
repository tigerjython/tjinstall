# SiPartner3.py
# Optimale Partnerwahl

import random
from gpanel import *

n = 1000 # Number of simulations
a = 10

def sim(x):
    # Random permutation [0..99]
    t = [0] * a
    for i in range(0, a):
        t[i] = i
    random.shuffle(t)
    best = max(t[0:x])
    for i in range(x, a):
        if  t[i] > best:
            return [i, t[i]]    
    return [99, t[a - 1]]

makeGPanel(-0.1 * a, 1.1 * a, -0.1 * a, 1.1 * a)
title("Mittlere Qualifikation nach Warten auf Partner")
drawGrid(0, a, 0, a)

for x in range(1, a):
    sum = 0
    repeat n:
        u = sim(x)
        sum += u[1]
    y = sum / n
    if x == 1:
       move(x, y)
    else:
       draw(x, y)
    
