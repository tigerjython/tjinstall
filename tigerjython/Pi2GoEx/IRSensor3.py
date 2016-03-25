# IRSensor3.py
# Events

from raspibrick import *

def onDark(id):
    print "dark event at", id

def onBright(id):
    print "bright event", id

robot = Robot()
irs = InfraredSensor(IR_CENTER, dark = onDark, bright = onBright)

while not isEscapeHit():
    Tools.delay(100)
robot.exit()
print "All done"