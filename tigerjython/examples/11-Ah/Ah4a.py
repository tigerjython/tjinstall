# Ah4a.py

from gturtle import *
import thread

def paint(t, isLeft):
    for i in range(16):
        t.forward(20)
        if isLeft:
            t.left(90)
        else:
            t.right(90)
        t.forward(20)
        if isLeft:
            t.right(90)
        else:
            t.left(90)
    
tf = TurtleFrame()
john = Turtle(tf)
john.setPos(-160, -160)
laura = Turtle(tf)
laura.setColor("red")
laura.setPenColor("red")
laura.setPos(160, -160)
thread.start_new_thread(paint, (john, False))
thread.start_new_thread(paint, (laura, True))
