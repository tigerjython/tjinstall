# Light5.py

from raspisim import *

RobotContext.useTorch(1, 150, 250, 100)
  
robot = Robot()
gear = Gear()
ls = [0] * 4
for i in range(4):
   ls[i] = LightSensor(i)
gear.setSpeed(25)
gear.forward()
s = 0.02
isTurning = False
v = [0] * 4
while not isEscapeHit():
    for i in range(4):
        v[i] = ls[i].getValue()
    d = (v[0] - v[1]) / (v[0] + v[1])
    if v[2] + v[3] > v[0] + v[1]:  # torch behind robot
        if not isTurning:
            if v[2] > v[3]:
                gear.right()
            else:
                gear.left()
            isTurning = True
    else:
        isTurning = False
        if d > -s and d < s:
            gear.forward()
        else:
            if d >= s:
                gear.rightArc(0.05)
            else:
                gear.leftArc(0.05)
robot.exit()   