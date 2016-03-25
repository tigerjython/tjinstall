# Robo4e.py

from simrobot import *
#from nxtrobot import *
#from ev3robot import *

RobotContext.setStartPosition(250, 200)
RobotContext.setStartDirection(-90)
RobotContext.useBackground("sprites/circle.gif")
  
def onDark(port, level):
    gear.backward(2700)
    gear.left(580)
    gear.forward()

robot = LegoRobot()
gear = Gear()
robot.addPart(gear)
ls = LightSensor(SensorPort.S3, 
      dark = onDark)
robot.addPart(ls)
ls.activate(True)
gear.forward()
while not robot.isEscapeHit():
    pass
robot.exit()
