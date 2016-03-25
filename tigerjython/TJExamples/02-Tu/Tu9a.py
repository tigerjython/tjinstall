from gturtle import *

def stairs(n):
    if  n == 0:
        return
    step()
    stairs(n - 1)

def step():
    forward(50)
    right(90)
    forward(50)
    left(90)
    
makeTurtle()
fillToHorizontal(0)
stairs(3)

