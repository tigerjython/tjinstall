# IRSensor2.py

from raspibrick import *

robot = Robot()
ir_left = InfraredSensor(IR_CENTER)
gear = Gear()
gear.forward()

while not isEscapeHit():
    v = ir_left.getValue()
    if v == 1:
        gear.backward(2000)
        gear.left(200)
        gear.forward()
    Tools.delay(100)   
robot.exit()
