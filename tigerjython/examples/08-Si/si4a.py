from gpanel import *
import random

n = 10000
p = 1/6

def sim():
    k = 1
    r = random.randint(1, 6)
    while r != 6:
        r = random.randint(1, 6)
        k += 1
    return k

makeGPanel(-5, 55, -200, 2200)
drawGrid(0, 50, 0, 2000)
title("Waiting on a 6")
h = [0] * 51
lineWidth(5)
sum = 0
repeat n:
    k = sim()
    sum += k
    if k <= 50:
        h[k] += 1
        line(k, 0, k, h[k])
mean_exp = sum / n

lineWidth(1)
setColor("red")
sum = 0
for k in range(1, 1000):
    pk = (1 - p)**(k - 1) * p
    nk = n * pk
    sum += nk * k
    if k <=50:
        line(k, 0, k, nk)
mean_theory = sum / n
title("Experiment: " + str(mean_exp) + "Theory: " + str(mean_theory))

