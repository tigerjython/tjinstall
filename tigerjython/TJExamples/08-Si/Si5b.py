from gpanel import *

def f(x, r):
     return r * x * (1 - x)

makeGPanel(-0.6, 4.4, -0.1, 1.1)
title("Tree Diagram")
drawGrid(0, 4.0, 0, 1.0, "gray")
for z in range(1001):
    r = 4 * z / 1000
    a = 0.5
    for i in range(1001):
        a = f(a, r)
        if i > 500:
            point(r, a)

