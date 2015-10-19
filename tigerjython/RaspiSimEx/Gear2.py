# Gear2.py

from raspisim import *

robot = Robot()
gear = Gear()
while not isEscapeHit():
    gear.forward()
    Tools.delay(2000)
    gear.left()
    Tools.delay(550);
#    Tools.delay(554) # last value for square
 