# Button1.py

from raspibrick import *

robot = Robot()
n = 0
while not isEscapeHit():
    print n
    n += 1
    Tools.delay(100)
print "Terminating..."
robot.exit()
