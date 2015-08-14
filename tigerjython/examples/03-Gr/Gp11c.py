from gpanel import *

size = 300

def onMousePressed(e):
    global x1, y1
    global x2, y2
    setColor("blue")
    setXORMode(Color.white) # set XOR paint mode
    x1 = x2 = e.getX()
    y1 = y2 = e.getY()

def onMouseDragged(e):
    global x2, y2
    rectangle(x1, y1, x2, y2) # erase old
    x2 = e.getX()
    y2 = e.getY()
    rectangle(x1, y1, x2, y2) # draw new

def onMouseReleased(e):
    rectangle(x1, y1, x2, y2) # erase old
    setPaintMode() # establish normal paint mode
    ulx = min(x1, x2)
    lrx = max(x1, x2)
    uly = min(y1, y2)
    lry = max(y1, y2)
    doIt(ulx, uly, lrx, lry)

def doIt(ulx, uly, lrx, lry):
    print "ulx = ", ulx, "uly = ", uly
    print "lrx = ", lrx, "lry = ", lry
    
x1 = y1 = 0
x2 = y2 = 0

makeGPanel(Size(size, size), 
    mousePressed = onMousePressed, 
    mouseDragged = onMouseDragged, 
    mouseReleased = onMouseReleased)
window(0, size, size, 0)    # y axis downwards

img = getImage("sprites/colorfrog.png")
image(img, 0, size)
