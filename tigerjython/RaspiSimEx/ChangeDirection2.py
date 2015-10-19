# ChangeDirection2.py

from raspisim import *

robot = Robot()
gear = Gear()
gear.setSpeed(60)
gear.rightArc(0.15, 2000)
gear.leftArc(0.15, 3000)
robot.exit()

