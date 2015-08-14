# Robo4a.py

from simrobot import *
#from ev3robot import *
#from nxtrobot import *

def switchMotorState():
    if motor.isMoving():
        motor.stop()
    else:
        motor.forward()

robot = LegoRobot()
motor = Motor(MotorPort.A)
robot.addPart(motor)
ts = TouchSensor(SensorPort.S1)
robot.addPart(ts)

isOff = True
while not robot.isEscapeHit():
    if ts.isPressed() and isOff:
        isOff = False
        switchMotorState()

    if not ts.isPressed() and not isOff:
        isOff = True
