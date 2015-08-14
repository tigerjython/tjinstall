from gpanel import *
import random

NB_DROPS = 10000

def onMousePressed(x, y):
    if isLeftMouseButton():
        pt = [x, y]
        move(pt)
        circle(0.5)
        corners.append(pt)
    if isRightMouseButton():
        wakeUp()

def go():
    global nbHit
    setColor("gray")
    fillPolygon(corners)
    for i in range(NB_DROPS):
        pt = [100 * random.random(), 100 * random.random()]
        color = getPixelColorStr(pt)
        if color == "black":
            setColor("green")
            point(pt)
        if color == "gray" or color == "red":
            nbHit += 1
            setColor("red")
            point(pt)
    title("All done. #hits: " + str(nbHit) + " of " + str(NB_DROPS))

makeGPanel(0, 100, 0, 100, mousePressed = onMousePressed)
title("Select corners with left button. Start dropping with right button")
bgColor("black")
setColor("white")
corners = []
nbHit = 0
putSleep()
go()

