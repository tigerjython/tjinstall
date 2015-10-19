# Gear3.py
# leftArc, radius independent of speed

from raspisim import *

robot = Robot()
gear = Gear()
#  gear.setSpeed(100)
gear.setSpeed(30)

gear.forward()
Tools.delay(500)
gear.leftArc(1)
Tools.delay(10000)