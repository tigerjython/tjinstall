# Light3.py

from raspisim import *

RobotContext.useTorch(1, 150, 250, 100)
RobotContext.useTorch(1, 250, 250, 100)
RobotContext.useTorch(1, 350, 250, 100)
  
robot = Robot()
gear = Gear()
lsL = LightSensor(LS_FRONT_LEFT)
lsR = LightSensor(LS_FRONT_RIGHT)
gear.setSpeed(25)
gear.forward()
s = 0.02
while not robot.isEscapeHit():
    vL = lsL.getValue()
    vR = lsR.getValue()
    d = (vL - vR) / (vL + vR)
    if d > -s and d < s:
        gear.forward()
    elif d >= s:
        gear.rightArc(0.05)
    else:
        gear.leftArc(0.05)
    Tools.delay(100)
robot.exit()
