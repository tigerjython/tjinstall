from gturtle import *

def square(side):    
    repeat(4): 
        forward(side) 
        right(90)
      
makeTurtle()
s = inputInt("Enter the side length")
if s < 300:
    square(s)    
else:  
    print "The side length is too big"


