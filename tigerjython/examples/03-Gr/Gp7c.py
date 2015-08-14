from gpanel import *

def onMousePressed(x, y):
    move(x, y)

def onMouseDragged(x, y):
    draw(x, y)

makeGPanel(mousePressed = onMousePressed, 
           mouseDragged = onMouseDragged)

