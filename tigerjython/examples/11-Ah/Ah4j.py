from gturtle import *
import thread

def onMousePressed(event):
#    createStar(event)
    thread.start_new_thread(createStar, (event,))

def createStar(event):
    t = Turtle(tf)
    x = t.toTurtleX(event.getX())
    y = t.toTurtleY(event.getY())
    t.setPos(x, y)
    t.startPath()
    repeat 9:
        t.forward(100)
        t.right(160)
    t.fillPath()        
     
tf = TurtleFrame(mousePressed = onMousePressed)
tf.setTitle("Klick To Create A Working Turtle")
