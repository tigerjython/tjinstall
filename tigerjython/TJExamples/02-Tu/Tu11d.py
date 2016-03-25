from gturtle import *

def drawStar(x, y):
    t = Turtle(tf)
    t.setPos(x, y)
    t.fillToPoint(x, y)
    for i in range(6):
        t.forward(40)
        t.right(140)
        t.forward(40)
        t.left(80)

tf = TurtleFrame(mouseHit = drawStar)
