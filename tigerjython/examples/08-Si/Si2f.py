# Si2e.py
# Alterspyramide

import exceptions
from gpanel import *

def readData(filename):
    table = []
    fData = open(filename)
    while True:
        line = fData.readline().replace(" ", "").replace("'", "")
        if line == "":
            break
        line = line[:-1] # remove trailing \n
        try:
            q = float(line)
        except exceptions.ValueError:
           break
        table.append(q)
    fData.close()
    return table

def drawAxis():
    text(0, -3, "0")
    line(0, 0, 0, 100)
    text(0, 103, "100")
    lineWidth(1)
    for y in range(11):
        line(-80000, 10* y, 80000, 10 * y)
        text(str(10 * y))

makeGPanel(-100000, 100000, -10, 110)
title("Alterspyramide (Grün -> Männer, Rot -> Frauen)")
lineWidth(4)
zx = readData("zx.dat")
zy = readData("zy.dat")
for t in range(101):
    setColor("red")
    x = zx[t]
    line(0, t, -x, t)
    setColor("darkgreen")
    y = zy[t]
    line(0, t, y, t)
setColor("black")
drawAxis()
