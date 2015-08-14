from gturtle import *

def onMouseMoved(x, y):
      moveTo(x, y)
      
makeTurtle(mouseMoved = onMouseMoved)
setCustomCursor("sprites/cutemouse.gif")
speed(-1)

