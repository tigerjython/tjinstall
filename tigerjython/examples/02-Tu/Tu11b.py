from gturtle import *

tf = TurtleFrame()

maya = Turtle(tf)
maya.setColor("red")
maya.setPenColor("red")
maya.setPos(0, -200)

pepe = Turtle(tf)
pepe.setColor("black")
pepe.setPenColor("black")
pepe.setPos(200, 0)
pepe.left(90)

repeat 7:
    repeat 4:
        maya.forward(50)
        maya.right(90)
        pepe.forward(50)
        pepe.left(90)
    maya.forward(50)    
    pepe.forward(50)
