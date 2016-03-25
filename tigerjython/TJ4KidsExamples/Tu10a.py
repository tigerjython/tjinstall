from gturtle import *

makeTurtle()
hideTurtle()
setPos(-300, -200)

a = 1
while a < 100:
    forward(10)
    right(a)
    a = 1.01 * a
    

