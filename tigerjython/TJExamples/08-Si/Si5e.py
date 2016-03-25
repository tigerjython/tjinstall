from gpanel import *

def f(x):
    return 1 / 2 * (x + 2 / x)

makeGPanel(-1, 11, -1, 11)
title("Iterative square root begins at x = 10. Press a  key...")
drawGrid(0, 10, 0, 10, "gray")

for i in range(10, 1001):
    x = 10 / 1000 * i
    if i == 10:
        move(x, f(x))
    else:
        draw(x, f(x))
        
line(0, 0, 10, 10)

x = 10
move(x, f(x))
fillCircle(0.1)
it = 0
while not isDisposed():
    getKeyWait()
    it += 1
    xnew = f(x)
    line(x, f(x), xnew, f(x))
    line(xnew, f(x), xnew, f(xnew))
    x = xnew
    move(x, f(x))
    fillCircle(0.1)
    title("Iteration " + str(it) + ": x = " + str(x))

