# Light1a.py

from raspibrick import *

def onDark(value):
    print "dark event with v:", value

def onBright(value):
    print "bright event with v:", value

robot = Robot()
ls = LightSensor(LS_FRONT_LEFT)
while not robot.isEscapeHit():
    continue
robot.exit()
print "All done"