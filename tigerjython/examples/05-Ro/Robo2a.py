from simrobot import *
#from nxtrobot import *
#from ev3robot import *

RobotContext.useObstacle("sprites/bg.gif", 250, 250)
RobotContext.setStartPosition(310, 470)

moveTime = 5000
turnTime = 580

robot = LegoRobot()
gear = Gear()
gear.setSpeed(50)
robot.addPart(gear)
gear.forward(moveTime)
gear.left(turnTime)
gear.forward(moveTime)
gear.right(turnTime)
gear.forward(moveTime)
gear.right(turnTime)
gear.forward(moveTime)
gear.left(turnTime)
gear.forward(moveTime)
robot.exit()
