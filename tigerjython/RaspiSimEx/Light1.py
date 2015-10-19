# Light1.py

from raspisim import *

RobotContext.useTorch(1, 150, 250, 100)
  
robot = Robot()
ls = LightSensor(LS_FRONT_LEFT)
while not robot.isEscapeHit():
    v = ls.getValue()
    print "v:", v
    Tools.delay(500)
robot.exit()
