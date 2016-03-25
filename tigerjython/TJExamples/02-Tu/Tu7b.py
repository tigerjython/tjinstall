from gturtle import *

def square():    
    repeat(4): 
        forward(100) 
        right(90)
      
makeTurtle()
n = inputInt("Enter a number: 1:red 2:green 3:yellow")
if n == 1:
    setFillColor("red")
elif n == 2: 
    setFillColor("green") 
elif n == 3:
    setFillColor("yellow") 
else:
    setFillColor("black")        
    
square()
fill(10, 10)


