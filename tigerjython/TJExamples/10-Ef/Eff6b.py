# Eff6b.py

from gconsole import *

def getKeyEvent():
    keyCode = getKeyCodeWait(True)
    if keyCode == KeyEvent.VK_UP:   
        return Events.stop
    if keyCode == KeyEvent.VK_DOWN:
        return Events.work
    if keyCode == KeyEvent.VK_LEFT:
        return Events.turnOff
    if keyCode == KeyEvent.VK_RIGHT:
        return Events.turnOn
    return None

State = enum("OFF", "STANDBY", "WORKING")
state = State.OFF
Events = enum("turnOn", "turnOff", "stop", "work")
Actions = enum("LED_on", "LED_off", "Pump_on", "Pump_off")
makeConsole()
while True:
    gprintln("Zustand: " + str(state))
    entry = getKeyEvent()
    print entry
    if entry == Events.turnOff:
       if state == State.STANDBY:
            state = State.OFF
            gprintln("Aktion: " + str(Actions.LED_on))
       if state == State.WORKING:
            state = State.OFF
            gprintln("Aktion: " + str(Actions.LED_off))
            gprintln("Aktion: " + str(Actions.Pump_off))
    elif entry == Events.turnOn:
        if state == State.OFF:
            state = State.STANDBY
            gprintln("Aktion: " + str(Actions.LED_on))
    elif entry == Events.stop:
        if state == State.WORKING:
            state = State.STANDBY
            gprintln("Aktion: " + str(Actions.Pump_off))
    elif entry == Events.work:
        if state == State.STANDBY:
            state = State.WORKING
            gprintln("Aktion: " + str(Actions.Pump_off))
 
    
        
