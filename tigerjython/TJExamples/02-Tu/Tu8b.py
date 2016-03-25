from gturtle import *

def triangle():
    repeat 3: 
        forward(100) 
        right(120)
 
makeTurtle()
i = 0
while i < 6:
    if i == 0 or i == 2 or i == 4:
         setPenColor("red")
    else:
         setPenColor("green")     

    fillToPoint(0, 0)
    triangle()
    right(60)
    i = i + 1
