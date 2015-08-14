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
    for x in range(ulx, lrx):
        for y in range(uly, lry):
            col = img.getPixelColor(x, y)
            red = col.getRed()
            green = col.getGreen()
            blue = col. getBlue()
            col1 = makeColor(3 * red // 4, green, blue)
            img.setPixelColor(x, y, col1)
    image(img, 0, size)
        
x1 = y1 = 0
x2 = y2 = 0

makeGPanel(Size(size, size), 
    mousePressed = onMousePressed, 
    mouseDragged = onMouseDragged, 
    mouseReleased = onMouseReleased)
window(0, size, size, 0)    # y axis downwards

img = getImage("sprites/colorfrog.png")
image(img, 0, size)
