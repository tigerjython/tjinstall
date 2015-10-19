# Infrared1.py

from raspisim import *

RobotContext.useObstacle("sprites/bar0.gif", 250, 100)
RobotContext.useObstacle("sprites/bar1.gif", 400, 250)
RobotContext.useObstacle("sprites/bar2.gif", 250, 400)
RobotContext.useObstacle("sprites/bar3.gif", 100, 250)

robot = Robot()
gear = Gear()

irs = InfraredSensor(IR_CENTER)
gear.setSpeed(30)
gear.forward()
while not isEscapeHit():
    if irs.getValue() == 1:
        gear.backward(1200)
        gear.left(750)
        gear.forward()

print "All done"
robot.exit()
