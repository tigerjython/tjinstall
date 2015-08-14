# from nxtrobot import *
from ev3robot import *

robot = LegoRobot()
us = UltrasonicSensor(SensorPort.S3)
robot.addPart(us)
isAutonomous = robot.isAutonomous()
while not robot.isEscapeHit():  
    dist = us.getDistance()
    print "d = ", dist
    robot.drawString("d=" + str(dist), 0, 3)
    robot.playTone(10 * dist + 100, 50)
    if dist == 255:
        robot.playTone(10 * dist + 100, 50)
    if isAutonomous:
       Tools.delay(1000)
    else:
       Tools.delay(200)
robot.exit()

