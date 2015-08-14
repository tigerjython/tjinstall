from ev3robot import *

robot = LegoRobot()
gear = Gear()
robot.addPart(gear)
irs = IRRemoteSensor(SensorPort.S1)
robot.addPart(irs)
isRunning = True

while not robot.isEscapeHit() and isRunning:
    command = irs.getCommand()    
    if command == 1:
        gear.leftArc(0.2)
    if command == 3:
        gear.rightArc(0.2)
    if command == 5:
        gear.forward()
    if command == 2:
        gear.stop()
    if command == 4:
        isRunning = False       
robot.exit()