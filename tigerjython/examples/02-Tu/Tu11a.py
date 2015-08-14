from gturtle import *

maya = Turtle()
maya.setColor("red")
maya.setPenColor("green")
maya.setPos(0, -200)

repeat 7:
    repeat 4:
        maya.forward(50)
        maya.right(90)
    maya.forward(50)
