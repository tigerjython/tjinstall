from gpanel import *

def onMousePressed(x, y):
    global x1, y1, x2, y2
    storeGraphics()
    x1 = x
    y1 = y
    x2 = x1
    y2 = y1
    setColor("red")
 
def onMouseDragged(x, y):
    global x2, y2
    recallGraphics()
    x2 = x
    y2 = y
    line(x1, y1, x2, y2) 

def onMouseReleased(x, y):
    setColor("white")
    if not (x1 == x2 and y1 == y2):
        line(x1, y1, x2, y2) 

x1 = 0
y1 = 0
x2 = 0
y2 = 0

makeGPanel(mousePressed = onMousePressed, 
              mouseDragged = onMouseDragged,
              mouseReleased = onMouseReleased)
title("Press And Drag To Draw Lines")
bgColor("blue")
setColor("white")
lineWidth(2)

