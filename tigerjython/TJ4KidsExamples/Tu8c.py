import math
from gturtle import *

def getC(c, a):
    x = a * a / c
    b = math.sqrt(c * c  - a * a)
    y = a * b / c
    return x, y

makeTurtle()

repeat:
    c = inputFloat("Hypotenuse c?")
    a = inputFloat("Kathete a?")

    clean()
    px, py = getC(c, a)
    moveTo(px, py)
    moveTo(c, 0)
    moveTo(0, 0)
