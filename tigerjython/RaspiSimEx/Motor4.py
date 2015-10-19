# Motor4.py

from raspisim import *

robot = Robot()
motL = Motor(MOTOR_LEFT)
motR = Motor(MOTOR_RIGHT)

motL.forward()
motR.forward()
Tools.delay(2000)

motR.backward()
Tools.delay(2000)
    
robot.exit()