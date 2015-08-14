from gturtle import *
from gpanel import *
import random

makeTurtle()
makeGPanel(-50, 550, -480, 480)
windowPosition(880, 10)
drawGrid(0, 500, -400, 400)
title("Mean distance versus time")
lineWidth(2)
setTitle("Random Walk")

t = 0
while t < 500:
    if random.randint(0, 1) == 1:
        setHeading(90)
    else:
        setHeading(-90)
    forward(10)
    x = getX()
    draw(t, x)
    t += 1
print "All done"