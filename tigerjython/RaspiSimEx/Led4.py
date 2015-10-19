# Led4.py

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
           Tools.delay(period // 2)
           ledRight.setColor(Color.black)
        Tools.delay(period // 2)
    print "Thread finished"    

robot = Robot()
ledLeft = Led(LED_LEFT)
ledRight = Led(LED_RIGHT)
isLeftBlinking = False
isRightBlinking = False    
isRunning = True
thread.start_new_thread(blinker, (500,))
    
while not isEscapeHit():
    if isLeftHit():
        isLeftBlinking = True
        isRightBlinking = False       
    if isRightHit():
        isLeftBlinking = False
        isRightBlinking = True       
    if isEnterHit():
        isLeftBlinking = False
        isRightBlinking = False
isRunning = False
robot.exit()

