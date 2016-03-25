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

makeGPanel(-10, 110, -0.1, 1.1)
title("Sterbewahrscheinlichkeit (Blau -> Männer, Rot -> Frauen)")
drawGrid(0, 100, 0, 1.0)
qx = readData("qx.dat")
qy = readData("qy.dat")
for t in range(101):
    setColor("blue")
    p = qx[t]
    line(t, 0, t, p)
    setColor("red")
    q = qy[t]
    line(t + 0.2, 0, t + 0.2, q)
