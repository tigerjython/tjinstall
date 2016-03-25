# Robo1a.py

#from simrobot import *
#from ev3robot import *
from nxtrobot import *
  
robot = LegoRobot()
gear = Gear()
robot.addPart(gear)
gear.setSpeed(50)
gear.forward()
Tools.delay(2000)
gear.left()
Tools.delay(580)
gear.forward();
Tools.delay(2000)
robot.exit()
