from gpanel import *

n  = 100

def p(k):
    return 2 * k * (n - k) / n / (n - 1)

makeGPanel(-10, 110, -0.1, 1.1)
drawGrid(0, 100, 0, 1.0)

sum = 0
for k in range(1, n - 1):
    if k == 1:
        move(k, p(k))
    else:
        draw(k, p(k))
    sum += 1 / p(k)

title("Time until everyone is ill: " + str(sum))

