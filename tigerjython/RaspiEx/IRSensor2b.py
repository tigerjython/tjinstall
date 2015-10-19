# IRSensor2a.py

from raspibrick import *

def onBright(id):
    gear.backward(2000)
    gear.left(200)
    gear.forward()

robot = Robot()
ir_left = InfraredSensor(IR_CENTER, bright = onBright)
gear = Gear()
gear.forward()

# For remote mode not really needed, terminate by closing connection box
#while not isEscapeHit():
#    Tools.delay(100)   
#robot.exit()

