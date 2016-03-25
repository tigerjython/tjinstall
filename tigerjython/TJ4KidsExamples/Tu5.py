from gturtle import *

def square():
    repeat 4: 
        forward(100) 
        left(90) 

makeTurtle()
setPenColor("red")
square()
right(120)
setPenColor("blue")
square()
right(120)
setPenColor("green")
square()
