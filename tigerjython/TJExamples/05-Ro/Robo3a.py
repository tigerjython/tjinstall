# Robo3a.py

from simrobot import *
#from nxtrobot import *
#from ev3robot import *

RobotContext.setStartPosition(250, 490)
RobotContext.useBackground("sprites/roadtest.gif")

robot = LegoRobot()
gear = Gear()
robot.addPart(gear)
ls = LightSensor(SensorPort.S3)
robot.addPart(ls)
ls.activate(True)
gear.forward()

while not robot.isEscapeHit():
    v = ls.getValue()
    print v
    Tools.delay(100)
robot.exit()
