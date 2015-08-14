from gturtle import *

makeTurtle()
setPos(-200, 30)
right(30)
fillToHorizontal(0)
setPenColor("sienna")

nr = 1
while nr <= 10:
    if nr > 3 and nr < 8:
        forward(60)
        right(120)
        forward(60)
        left(120)
    else:
        forward(30)
        right(120)
        forward(30)
        left(120)
  
    nr += 1
