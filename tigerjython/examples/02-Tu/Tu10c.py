from gturtle import *

def onMouseMoved(x, y):
    setHeading(towards(x, y))
    forward(10)
      
makeTurtle(mouseMoved = onMouseMoved)
speed(-1)

