from gturtle import *

makeTurtle()
hideTurtle()
openDot(400)

repeat 10000:
    setRandomPos(400, 400)
    rsquare = getX() * getX() + getY() * getY()
    if rsquare < 40000:
       setPenColor("red")
       dot(4)
    else:
       setPenColor("gray")
       dot(3)
