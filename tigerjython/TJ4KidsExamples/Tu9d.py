from gturtle import *

makeTurtle()
hideTurtle()

repeat 10000:
    setRandomPos(400, 400)
    x = getX()
    y = getY()
    if not (x > -50 and x < 50):
       setPenColor("red")
       dot(4)
    else:
       setPenColor("gray")
       dot(3)
