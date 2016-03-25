from gturtle import *

def step(t):
    repeat 4:
        t.forward(50)
        t.right(90)
    t.forward(50)
    
tf = TurtleFrame()

maya = Turtle(tf, "sprites/beetle.gif")
maya.setPenColor("green")
maya.setPos(0, -150)
pepe = Turtle(tf, "sprites/cuteturtle.gif")
pepe.setPos(200, 0)
pepe.left(90)

repeat 7:
    step(maya)
    step(pepe)
