from gturtle import *

def line(x1, y1, x2, y2):
    setPos(x1, y1)
    moveTo(x2, y2)
    
makeTurtle()
hideTurtle()

for i in range(21):
    line(10 * i, 0, 200, 10 * i)



