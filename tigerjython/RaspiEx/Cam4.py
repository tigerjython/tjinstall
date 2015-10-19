# Cam4.py
# Fernsteuerung: Positionieren, Aufnahme, Darstellung (remote mode)

from raspibrick import *
from gpanel import *

def takeSnapshot():
    jpeg = camera.captureAndTransfer(width, height)
    img = readImage(jpeg)
    if img != None:
        image(img, 0, 0)

width = 640
height = 480

robot = Robot()
gear = Gear()
gear.setSpeed(30)
camera = Camera()
horzMotor = ServoMotor(2, 300, 1.6)
vertMotor = ServoMotor(3, 320, 2)
makeGPanel(Size(width, height))
window(0, width, 0, height)
takeSnapshot()
horzPos = 0
vertPos = 0
n = 0
while robot.isConnected():
    doMove = False
    c = getKeyCode()
    if c == 65535:
        continue
    print c
    if c == 40 and vertPos < 50:     
        vertPos += 10
        doMove = True
    elif c == 38 and vertPos > - 50:
        vertPos -= 10
        doMove = True
    elif c == 37 and horzPos < 50:
        horzPos += 10
        doMove = True
    elif c == 39 and horzPos > - 50:
        horzPos -= 10
        doMove = True
    elif c == 65:  # a
        gear.leftArc(0.1)
    elif c == 87:  # w 
        gear.forward()
    elif c == 83:  # s 
        gear.rightArc(0.1)
    elif c == 88:  # x 
        gear.stop()
    elif c == 81:  # q    
       takeSnapshot()
    if doMove:
        horzMotor.setPos(horzPos)
        vertMotor.setPos(vertPos)
print "All done"
robot.exit()

