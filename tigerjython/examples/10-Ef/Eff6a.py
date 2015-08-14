from gconsole import *

def getKeyEvent():
    keyCode = getKeyCodeWait(True)
    if keyCode == KeyEvent.VK_UP:   
        return "stop"
    if keyCode == KeyEvent.VK_DOWN:
        return "work"
    if keyCode == KeyEvent.VK_LEFT:
        return "turnOff"
    if keyCode == KeyEvent.VK_RIGHT:
        return "turnOn"
    return ""
    
state = "OFF"  # Start state
makeConsole()
while True:
    gprintln("State: " + state)
    entry = getKeyEvent()
    if entry == "turnOff":
       if state == "STANDBY":
            state = "OFF"
            gprintln("LED off")
       if state == "WORKING":
            state = "OFF"
            gprintln("LED and pump off")
    elif entry == "turnOn":
        if state == "OFF":
            state = "STANDBY"
            gprintln("LED enabled")
    elif entry == "stop":
        if state == "WORKING":
            state = "STANDBY"
            gprintln("Pumpe off")
    elif entry == "work":
        if state == "STANDBY":
            state = "WORKING"
            gprintln("Pumpe enabled")

