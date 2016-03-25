from gturtle import *

makeTurtle()
right(90)
name = "Maya Bircher"
for c in name:
    forward(20)
    label(c)
right(90)    
for i in range(len(name)):
    forward(20)
    label(name[i])
