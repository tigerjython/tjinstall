from gpanel import *

def drawCircle:
   p.fillCircle(.04)  
   


def mouseMoved(event):
 
   x = p.toWindowX(event.getX())
   y = p.toWindowY(event.getY())
   p.move(x, y)
   

p = GPanel(mouseMoved = mouseMoved)
p.setColor("red")

