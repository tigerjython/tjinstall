# Robo3b.py

from simrobot import *
#from nxtrobot import *
#from ev3robot import *

RobotContext.setStartPosition(50, 490)
RobotContext.useBackground("sprites/road.gif")
  
robot = LegoRobot()
gear = Gear()
robot.addPart(gear)
ls = LightSensor(SensorPort.S3)
robot.addPart(ls)
ls.activate(True)
gear.forward()
nominal = 501

while not robot.isEscapeHit():
    actual = ls.getValue()
    if actual == nominal:
        gear.forward()
    elif actual < nominal:
        gear.leftArc(0.1)
    elif actual > nominal:
        gear.rightArc(0.1)

robot.exit()
