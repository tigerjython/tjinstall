from gturtle import *
import math

def tree(s):
    if s < 2:
        return
    square(s)
    forward(s)
    s1 = s / math.sqrt(2)
    left(45)
    tree(s1)
    right(90)
    forward(s1)
    tree(s1)
    back(s1)
    left(45)
    back(s)

def square(s):
    repeat 4:
        forward(s)
        right(90)

makeTurtle()
ht()
setPos(-50, -200)
tree(100)
