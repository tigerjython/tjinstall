#from nxtrobot import *
from ev3robot import *

def onPressed(port):
    if motor.isMoving():
        motor.stop()
    else:
        motor.forward()
        
robot = LegoRobot()

motor = Motor(MotorPort.A)
robot.addPart(motor)
ts = TouchSensor(SensorPort.S1, 
         pressed = onPressed)
robot.addPart(ts)
while not robot.isEscapeHit():
    pass
robot.exit()

