from gpanel import *
import random

def pair():
    # Select two distinct inhabitants
    a = random.randint(0, 99)
    b = a
    while b == a:
        b = random.randint(0, 99)
    z[a] = z[a] or z[b]
    z[b] = z[a]

def nbInfected():
    sum = 0
    for i in range(100):
        if z[i]:
            sum += 1
    return sum

makeGPanel(-50, 550, -10, 110)
title("The spread of an illness")
drawGrid(0, 500, 0, 100)
lineWidth(2)
setColor("blue")

z = [False] * 100
tmax =  500
t = 0
a = random.randint(0, 99) 
z[a] = True # random infected inhabitant
move(t, 1)

while t <= tmax:
    pair()
    infects = nbInfected()
    t += 1
    draw(t, infects)

