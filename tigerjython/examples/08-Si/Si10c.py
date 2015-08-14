from gturtle import *
from gpanel import *
import math

makeTurtle()
makeGPanel(-100, 1100, -10, 110)
windowPosition(850, 10)
drawGrid(0, 1000, 0, 100)
title("Mean distance versus time")
ht()
pu()

for t in range(100, 1100, 100):
    sum = 0
    clean()
    repeat 1000:
        repeat t: 
           fd(2.5)
           setRandomHeading()
        dot(3)
        r = math.sqrt(getX() * getX() + getY() * getY())
        sum += r
        home()
    d = sum / 1000   
    print "t =", t, "d =", d, "q = d / sqrt(t) =", d / math.sqrt(t)
    draw(t, d)
    fillCircle(5)
    delay(2000)
print "all done"
