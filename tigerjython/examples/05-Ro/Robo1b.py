# Robo1b.py

from simrobot import *
#from nxtrobot import *
#from ev3robot import *
  
robot = LegoRobot()
gear = Gear()
robot.addPart(gear)
gear.setSpeed(50)
gear.forward(2000)
gear.left(580)
gear.forward(2000)
robot.exit()
