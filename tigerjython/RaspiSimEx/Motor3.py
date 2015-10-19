# Motor3.py

from raspisim import *

robot = Robot()
motL = Motor(MOTOR_LEFT)
motR = Motor(MOTOR_RIGHT)

motL.forward()
motR.forward()
Tools.delay(2000)

motL.setSpeed(70)
Tools.delay(2000)
    
motR.setSpeed(70)
Tools.delay(2000)
robot.exit()