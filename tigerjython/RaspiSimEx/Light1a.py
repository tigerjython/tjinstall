# Light1a.py

from raspisim import *

RobotContext.useTorch(1, 150, 250, 100)
  
def onDark(id, v):
    print "dark event at", id, "with v:", v

def onBright(id, v):
    print "bright event at", id, "with v:", v
    
robot = Robot()
ls = LightSensor(LS_FRONT_LEFT, dark = onDark, bright = onBright)
while not robot.isEscapeHit():
    continue
robot.exit()
