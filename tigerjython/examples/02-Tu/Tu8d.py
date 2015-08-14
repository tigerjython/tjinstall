from gturtle import *

def square(sidelength):    
    repeat 4: 
        forward(sidelength) 
        left(90)

makeTurtle()
hideTurtle()

i = 0
while 1 == 1:
    if i > 120:
        break
    square(i)
    right(6)
    i += 2
print "i =", i
