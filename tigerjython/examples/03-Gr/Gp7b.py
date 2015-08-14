from gpanel import *      

def onMouseMoved(x, y):
    move(x, y)
    setColor("red")
    fillCircle(.04) 
    setColor("black")
    circle(.04)  

makeGPanel(mouseMoved = onMouseMoved)
