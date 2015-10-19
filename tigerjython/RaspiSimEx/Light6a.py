# Light6a.py
# Shadow

from raspisim import *

RobotContext.useTorch(1, 250, 250, 100)
RobotContext.useShadow(50, 150, 450, 200)
RobotContext.useShadow(100, 300, 350, 450)
  
robot = Robot()
gear = Gear()
ls = LightSensor(LS_FRONT_LEFT)
gear.leftArc(0.5)
isLightOn = False

while not isEscapeHit():
    v = ls.getValue()
    if not isLightOn and v == 0:
        isLightOn = True
        Led.setColorAll(Color.white)
    if isLightOn and v > 0:
        isLightOn = False
        Led.clearAll()
    Tools.delay(100)
robot.exit()   