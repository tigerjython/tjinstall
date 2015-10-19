# Cam5.py
# Herausfinden, ob sich das Bild aendert. Remote mode

from raspibrick import *
from gpanel import *

def takeSnapshot():
    jpeg = camera.captureAndTransfer(width, height)
    img = readImage(jpeg)
    if img != None:
        image(img, -1, -1)
    return img

width = 120
height = 90

robot = Robot()
camera = Camera()
pair = [None, None]

makeGPanel(Size(width-2, height-2))
window(0, width, 0, height)
i = 0
while robot.isConnected():
    pair[i] = takeSnapshot()
    if i == 0:
        i = 1
    elif i == 1:
        i = 0
    if pair[0] == None or pair[1] == None:
        continue
    count = 0
    for x in range(width):
        for y in range(height):
            c0 = pair[0].getPixelColor(x,y)
            c1 = pair[1].getPixelColor(x,y)
            r = abs(c0.getRed() - c1.getRed())      
            g = abs(c0.getGreen() - c1.getGreen())      
            b = abs(c0.getBlue() - c1.getBlue())      
            if r > 10 or g > 10 or b > 10:
                count += 1
    print "count", count
    if count > (width * height) // 10:
        playTone(3000, 100)
robot.exit()

