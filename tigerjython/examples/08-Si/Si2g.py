# Si2e.py
# Veraenderng der Alterspyramide

import exceptions
from gpanel import *

k = 2.0

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

def drawPyramid():
    clear()
    title("Kinderzahl: " + str(k) + ", Jahr: " + str(year) + ", Einwohnerzahl: " + str(getTotal()))
    lineWidth(4)
    for t in range(101):
        setColor("red")
        x = zx[t]
        line(0, t, -x, t)
        setColor("darkgreen")
        y = zy[t]
        line(0, t, y, t)
    setColor("black")
    drawAxis()
    repaint()

def getTotal():
    total = 0
    for t in range(101):
        total += zx[t] + zy[t]
    return int(total)

def updatePop():
    global zx, zy
    zxnew = [0] * 110
    zynew = [0] * 110
    # Getting older and die
    for t in range(101):
        zxnew[t + 1] = zx[t] - zx[t] * qx[t]    
        zynew[t + 1] = zy[t] - zy[t] * qy[t]
    # Make baby
    r = k / 20
    nbMother = 0
    for t in range(20, 40):
        nbMother += zy[t]
    zxnew[0] = r / 2 * nbMother
    zynew[0] = zxnew[0]
    zx = zxnew
    zy = zynew    

makeGPanel(-100000, 100000, -10, 110)
zx = readData("zx.dat")
zy = readData("zy.dat")
qx = readData("qx.dat")
qy = readData("qy.dat")
year = 2012
enableRepaint(False)
while True:
    drawPyramid()
    getKeyWait()
    year += 1
    updatePop()
  
