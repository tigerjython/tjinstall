# Light4.py

from raspisim import *

RobotContext.useTorch(1, 150, 250, 100)
  
robot = Robot()
gear = Gear()
lsFL = LightSensor(LS_FRONT_LEFT)
lsFR = LightSensor(LS_FRONT_RIGHT)
lsRL = LightSensor(LS_REAR_LEFT)
lsRR = LightSensor(LS_REAR_RIGHT)
gear.setSpeed(25)
gear.forward()
s = 0.02
while not isEscapeHit():
    vFL = lsFL.getValue()
    vFR = lsFR.getValue()
    vRL = lsRL.getValue()
    vRR = lsRR.getValue()
    d = (vFL - vFR) / (vFL + vFR)
    if vRL + vRR > vFL + vFR:  # torch behind robot
        gear.right()
    elif d > -s and d < s:
        gear.forward()
    else:
        if d >= s:
            gear.rightArc(0.05)
        else:
            gear.leftArc(0.05)
robot.exit()   