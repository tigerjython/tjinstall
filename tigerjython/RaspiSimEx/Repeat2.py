# Repeat2.py

from raspisim import *

robot = Robot()
gear = Gear()
for i in range(4):
    gear.leftArc(0.1, 1800)
    gear.backward(1000)    
robot.exit()

