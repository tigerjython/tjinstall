from simrobot import *
#from nxtrobot import *
#from ev3robot import *

mesh = [[50, 0], [25, 43], [-25, 43], [-50, 0], 
          [-25, -43], [25, -43]] 
RobotContext.useTarget("sprites/redtarget.gif", mesh, 400, 400)

def searchTarget():
    global left, right
    found = False
    step = 0
    while not robot.isEscapeHit():  
        gear.right(50)
        step = step + 1
        dist = us.getDistance()
        print "d = ", dist
        if dist != -1:  # simulation
#        if dist < 80:   # real
            if not found:
                found = True
                left = step
                print "Left at", left
                robot.playTone(10 * dist + 100, 1000)
        else:
            if found:    
                right = step
                print "Right at ", right
                robot.playTone(10 * dist + 100, 1000)
                break

left = 0
right = 0
robot = LegoRobot()
gear = Gear()
robot.addPart(gear)
us = UltrasonicSensor(SensorPort.S1)
robot.addPart(us)
us.setBeamAreaColor(makeColor("green"))  
us.setProximityCircleColor(makeColor("lightgray"))
gear.setSpeed(5)

print "Searching..."
searchTarget()

gear.left((right - left) * 25)   # simulation
#gear.left((right - left) * 100)  # real

print "Moving forward..."
gear.forward()

while not robot.isEscapeHit() and gear.isMoving(): 
    dist = us.getDistance()
    print "d =", dist
    robot.playTone(10 * dist + 100, 100)
    if dist < 30:
        gear.stop()
print "All done"        
robot.exit()

