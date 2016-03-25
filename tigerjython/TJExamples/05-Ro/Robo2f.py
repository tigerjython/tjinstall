# Robo2f.py (zusatz)

from ev3robot import *

def onActionPerformed(port, command):
    global state
    if command == 1:
        state = "LEFT"
    elif command == 3:
        state = "RIGHT"
    elif command == 2:
        state = "RUN"

moveTime = 5000
turnTime = 580
memory = []       
robot = LegoRobot()
gear = Gear()
gear.setSpeed(50)
robot.addPart(gear)
irs = IRRemoteSensor(SensorPort.S1, actionPerformed = onActionPerformed)
robot.addPart(irs)
state = "FORWARD"
robot.drawString("Learning...", 0, 3)

while not robot.isEscapeHit():
    if state == "FORWARD":
        gear.forward(moveTime)
        state = "STOPPED"
    elif state == "LEFT":
        memory.append(0)
        gear.left(turnTime)
        gear.forward(moveTime)
        state = "STOPPED"
    elif state == "RIGHT":
        memory.append(1)
        gear.right(turnTime)
        gear.forward(moveTime)
        state = "STOPPED"
    elif state == "RUN":
        robot.drawString("Executing...", 0, 3)
        robot.reset()
        gear.forward(moveTime)
        for k in memory:
            if k == 0:
                gear.left(turnTime)
            else:         
                gear.right(turnTime)
            gear.forward(moveTime)
        gear.stop() 
        robot.drawString("All done", 0, 3)
        state = "STOPPED"
robot.exit()