# Light6.py
# Shadow

from raspisim import *

RobotContext.useTorch(1, 250, 250, 100)
RobotContext.useShadow(50, 150, 450, 200)
RobotContext.useShadow(100, 300, 350, 450)
  
robot = Robot()
gear = Gear()
ls = LightSensor(LS_FRONT_LEFT)
gear.leftArc(0.5)
while not isEscapeHit():
    v = ls.getValue()
    print "v:", v
    Tools.delay(500)
robot.exit()   