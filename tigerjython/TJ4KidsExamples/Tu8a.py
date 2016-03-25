import math
from gturtle import *

def heron(a, b, c):
    s = (a + b + c) / 2
    f = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return f

makeTurtle()
startPath()
a = 200
forward(a)
right(144)
b = 150
forward(b)
c = distance(0, 0)
fillPath()
flaeche = heron(a, b, c)
label("  Fläche: " + str(flaeche))