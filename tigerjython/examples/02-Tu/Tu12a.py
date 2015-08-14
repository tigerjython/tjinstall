from gturtle import *
import math

nbGenerations = 12

def doIt():
    rt(90)
    figure(300, nbGenerations, 1)

def figure(s, n, flag):
    if n == 0:
        fd(s);
    else:
        alpha = 45
        if flag == 1:
            alpha = -alpha
            flag = -flag
        lt(alpha)
        figure(s / math.sqrt(2), n - 1, -flag)
        rt(2 * alpha)
        figure(s / math.sqrt(2), n - 1, flag)
        lt(alpha)

makeTurtle()
ht()
setPos(-100, 100) # screen
doIt()
setPos(100, 0)      # printer
printerPlot(doIt)

