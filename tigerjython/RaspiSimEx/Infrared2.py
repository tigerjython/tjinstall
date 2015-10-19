# Infrared2.py

from raspisim import *

RobotContext.setStartPosition(250, 250)
RobotContext.setStartDirection(-90)
RobotContext.useBackground("sprites/track.gif")
  
robot = Robot()
gear = Gear()

irs1 = InfraredSensor(IR_LINE_LEFT)
irs2 = InfraredSensor(IR_LINE_RIGHT)
gear.setSpeed(30)
gear.forward()
r = 0.1
while not robot.isEscapeHit():
    v1 = irs1.getValue()
    v2 = irs2.getValue()
    if v1 == 0 and v2 == 0:
        gear.forward()
    elif v1 == 0 and v2 == 1:
        gear.rightArc(r)
    elif v1 == 1 and v2 == 0:
        gear.leftArc(r)
    else: 
        gear.backward()
robot.exit()
