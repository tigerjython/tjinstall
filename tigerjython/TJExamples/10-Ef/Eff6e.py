# Eff6b.py

from gconsole import *

def getKeyEvent():
    global word
    keyCode = getKeyCodeWait(True)
    if keyCode == KeyEvent.VK_A:
        return Events.a
    if keyCode == KeyEvent.VK_B:
        return Events.b
    return None

State = enum("S", "A", "B")
state = State.S
Events = enum("a", "b")
makeConsole()
word = ""
gprintln("State: " + str(state))
while True:
    entry = getKeyEvent()
    if entry == Events.a:
        if state == State.A:
            state = State.S
        elif state == State.B:
            state = State.S
        word += "a"
        gprint("Word: " + word + " -> ")
        gprintln("State: " + str(state))
    elif entry == Events.b:
        if state == State.S:
            state = State.B
        elif state == State.B:
            state = State.A
        word += "b"
        gprint("Word: " + word + " -> ")
        gprintln("State: " + str(state))
 
    
        
