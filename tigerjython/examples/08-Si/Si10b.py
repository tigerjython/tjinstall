from gturtle import *
from gpanel import *
import math
import random

makeTurtle()
makeGPanel(-100, 1100, -10, 110)
windowPosition(850, 10)
drawGrid(0, 1000, 0, 100)
title("Mean distance versus time")
ht()
pu()

for t in range(100, 1100, 100):
    setY(250 - t / 2)
    label(str(t))    
    sum = 0
    repeat 1000:
        repeat t: 
           if random.randint(0, 1) == 1:
               setHeading(90)
           else:
               setHeading(-90)
           forward(2.5)
        dot(3)
        r = abs(getX())
        sum += r
        setX(0)
    d = sum / 1000   
    print "t =", t, "d =", d, "q = d / sqrt(t) =", d / math.sqrt(t)  
    draw(t, d)
    fillCircle(5)
print "all done"
