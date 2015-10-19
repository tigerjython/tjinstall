# KeyControl3.py

from raspisim import *

robot = Robot()
gear = Gear()
speed = 15

while not isEscapeHit():
    if isUpHit():
        speed += 5
        print "speed =", speed
        gear.setSpeed(speed)
        gear.forward()
    elif isDownHit():
        speed += - 5
        print "speed =", speed
        gear.setSpeed(speed)
        gear.forward()
    elif isLeftHit():
        gear.leftArc(0.1)
    elif isRightHit():
        gear.rightArc(0.1)
    elif isEnterHit():
        gear.stop()    
robot.exit()

