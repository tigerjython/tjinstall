from gturtle import *

def field(x, y):
    setPos(x, y)
    startPath()
    repeat 4:
        forward(30)
        left(90)
    fillPath()    

makeTurtle()
hideTurtle()
for i in range(8):
    for k in range(8):
        if (i + k) % 2 == 0:
            field(30 * i, 30 * k)
 
