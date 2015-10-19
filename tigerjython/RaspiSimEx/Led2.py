# Led1.py

from raspisim import *

robot = Robot()
gear = Gear()
Led.setColorAll(Color.white)
gear.leftArc(0.5)
while not isEscapeHit():
    Tools.delay(2000)
    Led.setColorAll(Color.black)
    Tools.delay(2000)
    Led.setColorAll(Color.white)
print "All done"
robot.exit()
