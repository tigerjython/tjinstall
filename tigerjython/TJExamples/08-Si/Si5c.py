from gpanel import *

def a(n):
     return (1 + 1/n)**n

makeGPanel(-10, 110, 1.9, 3.1)
title("Euler Number")
drawGrid(0, 100, 2.0, 3.0, "gray")
for n in range(1, 101):
    move(n, a(n))
    fillCircle(0.5)

