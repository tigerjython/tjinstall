# LED1.py
from raspibrick import *

robot = Robot()
Led.setColorAll(20, 20, 0)
while not isEscapeHit():
    continue
robot.exit()
