# Led3.py
# blinking

from raspisim import *

robot = Robot()
led = Led(LED_FRONT)
while not isEscapeHit():
    led.setColor(Color.white)
    Tools.delay(500)
    led.setColor(Color.black)
    Tools.delay(500)
print "All done"
robot.exit()
