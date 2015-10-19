# Repeat1.py

from raspisim import *

robot = Robot()
gear = Gear()
i = 0
while i < 4:
    gear.forward(2000)
    gear.left(550)
    i = i + 1
robot.exit()

