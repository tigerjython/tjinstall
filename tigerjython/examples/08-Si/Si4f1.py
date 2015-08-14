import random
from gpanel import *

n = 1000 # Number of simulations
a = 100 # Number of partners

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

makeGPanel(-10, 110, -0.1, 1.1)
title("The probability of finding the best partner from  100")
drawGrid(0, 100, 0, 1.0)

for x in range(1, 100):
    sum = 0
    repeat n:
        z = sim(x)
        if z[1] == 99:  # best score
            sum += 1
    p = sum / n
    if x == 1:
        move(x, p)    
    else:
        draw(x, p)    

