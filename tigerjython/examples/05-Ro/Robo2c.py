from simrobot import *
#from nxtrobot import *
#from ev3robot import *

RobotContext.useObstacle("sprites/bg.gif", 250, 250)
RobotContext.setStartPosition(310, 470)
RobotContext.showStatusBar(30)

def onButtonHit(buttonID):
    global state
    if buttonID == BrickButton.ID_LEFT:
        state = "LEFT"
    elif buttonID == BrickButton.ID_RIGHT:
        state = "RIGHT"
    elif buttonID == BrickButton.ID_ENTER:
        state = "RUN"

moveTime = 5000
turnTime = 580
memory = []        
robot = LegoRobot(buttonHit = onButtonHit)
gear = Gear()
gear.setSpeed(50)
robot.addPart(gear)
state = "FORWARD"

while not robot.isEscapeHit():
    if state == "FORWARD":
        robot.drawString("Moving forward", 0, 3)
        gear.forward(moveTime)
        state = "STOPPED"
        robot.drawString("Teach me!", 0, 3)
    elif state == "LEFT":
        memory.append(0)
        robot.drawString("Saved: LEFT-TURN", 0, 3)
        gear.left(turnTime)
        state = "FORWARD"
    elif state == "RIGHT":
        memory.append(1)
        robot.drawString("Saved: RIGHT-TURN", 0, 3)
        gear.right(turnTime)
        state = "FORWARD"
    elif state == "RUN":
        robot.drawString("Executing memory", 0, 1)
        robot.drawString(str(memory), 0, 2)
        robot.reset()
        robot.drawString("Moving forward", 0, 3)
        gear.forward(moveTime)
        for k in memory:
            if k == 0:
                robot.drawString("Turning left", 0, 3)
                gear.left(turnTime)
            else:          
                robot.drawString("Turning right", 0, 3)
                gear.right(turnTime)
            robot.drawString("Moving forward", 0, 3)
            gear.forward(moveTime)
        gear.stop()  
        robot.drawString("All done", 0, 3)
        state = "STOPPED"
robot.exit()

