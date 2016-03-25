from gturtle import *

def square(sidelength):    
    repeat(4): 
        forward(sidelength) 
        right(90)
      
makeTurtle()
sidelength = inputInt("Enter the side length")
square(sidelength)


