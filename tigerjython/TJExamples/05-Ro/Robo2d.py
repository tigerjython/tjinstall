# Robo2d.py

from simrobot import *
#from nxtrobot import *
#from ev3robot import *

import time

RobotContext.useObstacle("sprites/bg.gif", 250, 250)  
RobotContext.setStartPosition(310, 470)
RobotContext.showStatusBar(30)

def onPressed(port):
    global startTime
    global backTime
    robot.drawString("Press event!", 0, 1)
    dt = time.clock() - startTime # time since last hit in s
    gear.backward(backTime)
    if dt > 2:
        memory.append(0) 
        gear.left(turnTime) # turning left   
    else:
        memory.pop()
        memory.append(1) 
        gear.right(2 * turnTime) # turning right
    robot.drawString("Mem: " + str(memory), 0, 1)
    gear.forward()
    startTime = time.clock()      

def run():
    for k in memory:
        robot.drawString("Moving forward", 0, 1)
        gear.forward(moveTime)
        if k == 0:
            robot.drawString("Turning left", 0, 1)
            gear.left(turnTime)            
        elif k == 1:
            robot.drawString("Turning right", 0, 1)
            gear.right(turnTime)            
    gear.forward(moveTime) 
    robot.drawString("All done", 0, 1)          
    isExecuting = False
    
moveTime = 5000
turnTime = 580
backTime = 850
memory = []      
robot = LegoRobot()
gear = Gear()
gear.setSpeed(50)
robot.addPart(gear)
ts = TouchSensor(SensorPort.S3, pressed = onPressed)      
robot.addPart(ts)
startTime = time.clock()
gear.forward()
robot.drawString("Moving forward", 0, 1)

while not robot.isEscapeHit():
    if robot.isEnterHit():
        robot.reset()    
        run()      
robot.exit()