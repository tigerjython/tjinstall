# Motor1.py

from raspibrick import *

robot = Robot()
mot = Motor(MOTOR_LEFT)
mot.forward()
Tools.delay(3000)
mot.stop()
Tools.delay(3000)
robot.exit()
print "All done"
