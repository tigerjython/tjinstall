# KeyControl1.py

from raspisim import *

robot = Robot()
gear = Gear()
gear.setSpeed(20)

while not isEscapeHit():
    if isUpHit():
        gear.forward()
    elif isDownHit():
        gear.backward()
    elif isLeftHit():
        gear.leftArc(0.1)
    elif isRightHit():
        gear.rightArc(0.1)
    elif isEnterHit():
        gear.stop()    
robot.exit()

