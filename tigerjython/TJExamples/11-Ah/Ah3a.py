from gpanel import *
from math import sin

def sinc(x):
    y = sin(x) / x
    return y

makeGPanel(-24, 24, -1.2, 1.2)
drawGrid(-20, 20, -1.0, 1, "darkgray")
title("Sinus Cardinalis: y = sin(x) / x")

x = -20
dx = 0.1
while x <= 20:
    y = sinc(x)
    if x == -20:
        move(x, y)
    else:
        draw(x, y)
    x += dx
