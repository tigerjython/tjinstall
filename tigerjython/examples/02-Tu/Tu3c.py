from gturtle import *

makeTurtle()

setPos(-200, 0)
right(45)

repeat 5:
    playTone(392, 400)   
    forward(20)    
    right(90)
    playTone(523, 400)
    forward(20)  
    left(90)
