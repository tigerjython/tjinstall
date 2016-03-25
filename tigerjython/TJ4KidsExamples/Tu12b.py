from gturtle import *

def makeButton(x, y):
    setPos(x, y)
    setFillColor("red")
    startPath()
    repeat 4:
        forward(40)
        right(90)
    fillPath()    

def drawLines():
    for pt1 in points:
        for pt2 in points:
            setPos(pt1)
            moveTo(pt2)

@onMouseHit
def onMouseHit(x, y):
    if x > 0 and x < 40 and y > -200 and y < -160:
        drawLines()
        print points
    else:
        setPos(x, y)    
        dot(8)
        pt = (x, y)
        points.append(pt)        

makeTurtle()
hideTurtle()
points = []
makeButton(0, -200)
