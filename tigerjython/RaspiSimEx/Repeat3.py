# Repeat3.py

from raspisim import *

robot = Robot()
gear = Gear()
gear.setSpeed(70)
while not isEscapeHit():
    gear.leftArc(0.1)
robot.exit()

