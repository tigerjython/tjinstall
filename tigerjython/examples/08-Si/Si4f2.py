import random
from gpanel import *

n = 1000 # Number of simulations

def sim(x):
    # Random permutation [0..99]
    t = [0] * 100
    for i in range(0, 100):
        t[i] = i
    random.shuffle(t)
    best = max(t[0:x])
    for i in range(x, 100):
        if  t[i] > best:
            return [i, t[i]]    
    return [99, t[99]]

makeGPanel(-10, 110, -10, 110)
title("Mean qualification after waiting for a  partner")
drawGrid(0, 100, 0, 100)

for x in range(1, 99):
    sum = 0
    repeat n:
        u = sim(x)
        sum += u[1]
    y = sum / n
    if x == 1:
       move(x, y)
    else:
       draw(x, y)

