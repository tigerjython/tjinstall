# Ultrasonic1a.py
# Events

from raspisim import *

mesh_hbar = [[200, 10], [-200, 10], [-200, -10], [200, -10]]
mesh_vbar = [[10, 200], [-10, 200], [-10, -200], [10, -200]]
RobotContext.useTarget("sprites/bar0.gif", mesh_hbar, 250, 100)
RobotContext.useTarget("sprites/bar0.gif", mesh_hbar, 250, 400)
RobotContext.useTarget("sprites/bar1.gif", mesh_vbar, 100, 250)
RobotContext.useTarget("sprites/bar1.gif", mesh_vbar, 400, 250)

def onNear(d):
    print "near event at d: ", d
    gear.backward(2000)
    gear.left(1000)
    gear.forward()

def onFar(d):
    print "far event at d: ", d

robot = Robot()
gear = Gear()
us = UltrasonicSensor(near = onNear, far = onFar)
us.setBeamAreaColor(Color.green)
us.setProximityCircleColor(Color.lightGray)
  
gear.setSpeed(25)
gear.forward()
    
while not isEscapeHit():
    continue
robot.exit()