from gturtle import *

def square():
    repeat 4:
        forward(50)
        right(90)

def drawGrid():
    for x in range(3):
        for y in range(3):
            setPos(50 * x, 50 * y)
            square()

@onMouseHit
def onMouseHit(x, y):
    global player
    if player == 1:
        setFillColor("red")
        player = 2
    elif player == 2:
        setFillColor("green")
        player = 1
    setPos(x, y)
    fill()

player = 1        
makeTurtle()
hideTurtle()
drawGrid()


