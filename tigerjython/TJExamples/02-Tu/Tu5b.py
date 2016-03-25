from gturtle import *

def square(sidelength, color):
    setPenColor(color)    
    repeat(4): 
        forward(sidelength) 
        left(90)
      
makeTurtle()
square(100, "red")
left(120)
square(80, "green")
left(120)
square(60, "violet")


