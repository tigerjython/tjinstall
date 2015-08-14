# Robo2e.py

from simrobot import *
#from nxtrobot import *
#from ev3robot import *

import time

RobotContext.useObstacle("sprites/bg2.gif", 250, 250)  
RobotContext.setStartPosition(410, 460)
RobotContext.showStatusBar(30)

def pressCallback(port):
    global startTime
    global backTime
    global turnTime
    global moveTime
    dt = time.clock() - startTime # time since last hit in s
    gear.backward(backTime)
    if dt > 2: 
        moveTime = int(dt * 1000) - backTime  # save long-track time
        node = [moveTime, 0] 
        memory.append(node) # save long-track time 
        gear.left(turnTime) # turning left   
    else:
        memory.pop() # discard node
        node = [moveTime, 1] 
        memory.append(node) 
        gear.right(2 * turnTime) # turning right
    robot.drawString("Memory: " + str(memory), 0, 1)
    gear.forward()
    startTime = time.clock()      

def run():
    for node in memory:
        moveTime = node[0]
        k = node[1]
        robot.drawString("Moving forward",0, 1)
        gear.forward(moveTime)
        if k == 0:
            robot.drawString("Turning left",0, 1)
            gear.left(turnTime)            
        elif k == 1:
            robot.drawString("Turning right",0, 1)
            gear.right(turnTime)            
    gear.forward() # must stop manually
    robot.drawString("All done, press DOWN to stop", 0, 1)          
    isExecuting = False
    
turnTime = 580
backTime = 850
     
robot = LegoRobot()
gear = Gear()
gear.setSpeed(50)
robot.addPart(gear)
ts = TouchSensor(SensorPort.S3, pressed = pressCallback)      
robot.addPart(ts)
startTime = time.clock()
moveTime = 0
memory = [] 
gear.forward()

while not robot.isEscapeHit():
    if robot.isDownHit():  
        gear.stop()
    elif robot.isEnterHit():
        robot.reset()    
        run()      
robot.exit()