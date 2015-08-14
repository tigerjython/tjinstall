from gpanel import *

def onMousePressed(x, y):
    move(x, y) 
    fillCircle(0.02)

makeGPanel(mousePressed = onMousePressed)
setColor("green")              

