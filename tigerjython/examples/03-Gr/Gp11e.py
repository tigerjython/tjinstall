from gpanel import *

size = 300

def onMousePressed(e):
    global x1, y1
    global x2, y2
    setColor("blue")
    setXORMode("white")
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
    setPaintMode()
    ulx = min(x1, x2)
    lrx = max(x1, x2)
    uly = min(y1, y2)
    lry = max(y1, y2)
    doIt(ulx, uly, lrx, lry)    

def doIt(ulx, uly, lrx, lry):
    width = lrx - ulx
    height = lry - uly
    if ulx < 0 or uly < 0 or lrx > size or lry > size:
        return
    if width < 20 or height < 20:
        return
    
    cropped = GBitmap.crop(img, ulx, uly, lrx, lry)
    p = GPanel(Size(width, height))  # another GPanel
    p.window(0, width, 0, height)
    p.image(cropped, 0, 0)
    rc = save(cropped, "mypict.jpg", "jpg") 
    if rc:
        p.title("Saving OK")
    else:
        p.title("Saving Failed")

    
x1 = y1 = 0
x2 = y2 = 0

makeGPanel(Size(size, size), 
    mousePressed = onMousePressed, 
    mouseDragged = onMouseDragged, 
    mouseReleased = onMouseReleased)
window(0, size, size, 0)    # y axis downwards

img = getImage("sprites/colorfrog.png")
image(img, 0, size)
