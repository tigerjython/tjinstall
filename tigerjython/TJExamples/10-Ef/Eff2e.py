from gpanel import *

def collatz(n):
    nb = 0
    while n != 1:
        nb += 1
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    return nb             

z = 10000 # max n
yval = [0] * (z + 1)
for n in range(1, z + 1):
    yval[n] = collatz(n)
ymax = (max(yval) // 100  + 1) * 100

makeGPanel(-0.1 * z, 1.1 * z, -0.1 * ymax, 1.1 * ymax)
title("Collatz Assumption")
drawGrid(0, z, 0, ymax, "gray")

for x in range(1, z + 1):
    move(x, yval[x])
    fillCircle(z / 200)

