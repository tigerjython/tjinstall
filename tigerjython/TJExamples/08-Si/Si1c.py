# Si1c.py

from gpanel import *
from random import randint

z = 10000
n = 100 

def versuch():
    gewonnen = 0
    repeat n:
        a = randint(1, 6)
        b = randint(1, 6)
        c = randint(1, 6)
        if a == 6 or b == 6 or c == 6:
            gewonnen += 1
    return gewonnen

def drawGrid():
    # Horizontal
    for i in range(11):
        y = 100 * i
        line(0, y, n, y)
        text(0, y, str(y))
    # Vertical
    for k in range(11):
        x = n / 10 * k
        line(x, 0, x, 1000)
        text(x, -50, str(x))

makeGPanel(-0.1 * n, 1.1 * n, -100, 1100)
drawGrid()
h = [0] * (n + 1)
title("Starting Experiment. Please wait...")
repeat z:
    x = versuch()
    h[x] += 1
title("Experiment Done")

lineWidth(2)
setColor("blue")
for x in range(n + 1):
    line(x, 0, x, h[x])

    
