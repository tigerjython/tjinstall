from gturtle import *

def square(sidelength):    
    repeat(4): 
        forward(sidelength) 
        left(90)
      
makeTurtle()
setPenColor("red")
square(80)
left(180)
setPenColor("green")
square(50)
