# Led4a.py

from raspisim import *
import thread

def blinker(period):
    while isRunning:
        if isLeftBlinking:
           ledLeft.setColor(Color.white)
           Tools.delay(period // 2)
           ledLeft.setColor(Color.black)
        if isRightBlinking:
           ledRight.setColor(Color.white)
           Tools.delay(300)
           ledRight.setColor(Color.black)
        Tools.delay(period // 2)
    print "Thread finished" 

def switchLamp(lamp, on):
    if on:
        lamp.setColor(Color.white)
    else:    
        lamp.setColor(Color.black)

robot = Robot()
gear = Gear()
gear.setSpeed(40)    

ledFront = Led(LED_FRONT)
ledLeft = Led(LED_LEFT)
ledRight = Led(LED_RIGHT)
ledRear = Led(LED_REAR)
isLeftBlinking = False
isRightBlinking = False    
isRunning = True
thread.start_new_thread(blinker, (500,))
    
while not isEscapeHit():
    if isUpHit():
        gear.forward()
        isLeftBlinking = False
        isRightBlinking = False
        switchLamp(ledRear, False)
        switchLamp(ledFront, True)
    if isDownHit():
        gear.backward()
        isLeftBlinking = False
        isRightBlinking = False
        switchLamp(ledRear, True)
        switchLamp(ledFront, False)
    if isLeftHit():
        gear.leftArc(1)
        isLeftBlinking = True
        isRightBlinking = False       
        switchLamp(ledFront, True)
        switchLamp(ledRear, False)       
    if isRightHit():
        gear.rightArc(1)
        isLeftBlinking = False
        isRightBlinking = True       
        switchLamp(ledFront, True)
        switchLamp(ledRear, False)       
    if isEnterHit():
        gear.stop()
        isLeftBlinking = False
        isRightBlinking = False
        switchLamp(ledFront, False)
        switchLamp(ledRear, False)       
isRunning = False
Led.clearAll()
print "All done"               
robot.exit()

