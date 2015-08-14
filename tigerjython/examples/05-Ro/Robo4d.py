# Robo4d.py

from simrobot import *
#from nxtrobot import *
#from ev3robot import *

mesh = [[50, 0], [25, 43], [-25, 43], [-50, 0], 
        [-25, -43], [25, -43]] 
RobotContext.useTarget("sprites/redtarget.gif", 
                    mesh, 400, 400)
RobotContext.useObstacle("sprites/redtarget.gif",400,400)                      

def pressCallback(port):
   gear.stop()

def searchTarget():
   global left, right
   found = False
   step = 0
   while robot.isRunning():  
      gear.right(50)
      step = step + 1
      dist = us.getDistance()
      if dist != -1:
         if not found:
            found = True
            left = step
            print "Left border found at " + str(left)
      else:
         if found:   
            right = step
            print "Right border  found at " + str(right)
            break

robot = LegoRobot()
gear = Gear()
robot.addPart(gear)
gear.setSpeed(10)

us = UltrasonicSensor(SensorPort.S1)
robot.addPart(us)
us.setBeamAreaColor(Color.green)  
us.setProximityCircleColor(Color.lightGray)

ts = TouchSensor(SensorPort.S3, pressed = pressCallback)
robot.addPart(ts)

print "Searching target..."
searchTarget()

print "Turning to target..."
gear.left((right - left) * 25)
print "Moving forward..."
gear.forward()

while robot.isRunning() and gear.isMoving(): 
   dist = us.getDistance()
   print "Distance = " + str(dist)
robot.exit()
