from gturtle import *

def square(s):
    repeat 4:
        forward(s)
        right(90)

makeTurtle()
hideTurtle()
setPos(-200, -200)
side = 400
repeat 100:
    square(side) 
    side -= 4
