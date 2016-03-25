from gturtle import *

makeTurtle()

def star(size, filled):
    if filled:
        startPath()
    repeat 9:
        forward(size)
        left(175)
        forward(size)
        left(225)
    if filled:
        fillPath()

clear("black")
repeat 5:
    color = askColor("Color selection", "yellow")
    setPenColor(color) 
    setFillColor(color)
    setRandomPos(400, 400)
    back(100)
    star(100, True)
