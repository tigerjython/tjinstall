# Tu9d.py

from gturtle import *
makeTurtle()
hideTurtle()

repeat 10000:
    setRandomPos(400, 400)
    x = getX()
    y = getY()
    if x <= -50 or x >= 50:
       setPenColor("red")
       dot(4)
    else:
       setPenColor("gray")
       dot(3)
