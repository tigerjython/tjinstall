# Infrared1a.py
# Events

from raspisim import *

RobotContext.useObstacle("sprites/bar0.gif", 250, 100)
RobotContext.useObstacle("sprites/bar1.gif", 400, 250)
RobotContext.useObstacle("sprites/bar2.gif", 250, 400)
RobotContext.useObstacle("sprites/bar3.gif", 100, 250)

def onActivated(id):
    print "activated at", id
    gear.backward(1200)
    gear.left(750)
    gear.forward()

def onPassivated(id):
    print "passivated at", id
        
robot = Robot()
gear = Gear()
gear.setSpeed(30)
gear.forward()

irs = InfraredSensor(IR_CENTER, activated = onActivated, passivated = onPassivated)
while not isEscapeHit():
    continue

print "All done"
robot.exit()
