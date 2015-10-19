# Led1.py

from raspisim import *

robot = Robot()
while not isEnterHit():
    continue
leds = [0] * 4
for id in range(4):
    leds[id] = Led(id)

while not isEnterHit():
    continue
    
for id in range(4):
    leds[id].setColor(Color.yellow);
    while not isEnterHit():
        continue
Led.clearAll()
print "All done"
robot.exit()
