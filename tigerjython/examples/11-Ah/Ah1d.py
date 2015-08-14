# Ah1d.py
# Eifersucht, einlesen

from gamegrid import *

def pressEvent(e):
    global state
    loc = toLocationInGrid(e.getX(), e.getY())
    if loc in left_locations:
        actor = getOneActorAt(loc)
        if actor != None:
            x = 6 - actor.getX()
            y = actor.getY()
            actor.setLocation(Location(x, y))
    if loc in right_locations:
        actor = getOneActorAt(loc)
        if actor != None:
            x = 6 - actor.getX()
            y = actor.getY()
            actor.setLocation(Location(x, y))
    state = 0
    for i in range(7):
        loc = right_locations[i]
        actor = getOneActorAt(loc)
        if actor != None:
            state += 2**(6 - i)
    showState(state)

def stateToString(state):
    return str(bin(state)[2:]).zfill(7)

def showState(state):
    sbin = stateToString(state)
    for i in range(7):
        if sbin[i] == "0":
           actors[i].setLocation(left_locations[i])
        else:
           actors[i].setLocation(right_locations[i])
    setTitle("State: " + str(state) + ", bin: " + stateToString(state)) 
    if isStateAllowed(state):
        setStatusText("Situation allowed")
    else:
        setStatusText("Situation not allowed")
    refresh()

def isStateAllowed(state):
    print state
    stateStr = stateToString(state)
    mred = stateStr[1] == "1"
    fred = stateStr[2] == "1"
    mgreen = stateStr[3] == "1"
    fgreen = stateStr[4] == "1"
    mblue = stateStr[5] == "1"
    fblue = stateStr[6] == "1"

    if mred and not fred or not mred and fred:  # mred/fred not together
        if not fred and (not mgreen or not mblue) or fred and (mgreen or mblue):
            return False
    if mgreen and not fgreen or not mgreen and fgreen:  # mgreen/fgreen not together
        if not fgreen and (not mred or not mblue) or fgreen and (mred or mblue):
            return False
    if mblue and not fblue or not mblue and fblue:  # mblue/fblue not together
        if not fblue and (not mred or not mgreen) or fblue and (mred or mgreen):
            return False
    return True   

makeGameGrid(7, 3, 50, None, False, mousePressed = pressEvent)
setBgColor(Color.white)
addStatusBar(30)        
show()
actors = [Actor("sprites/boat.png"), 
   Actor("sprites/man_0.png"), Actor("sprites/woman_0.png"),
   Actor("sprites/man_1.png"), Actor("sprites/woman_1.png"),
   Actor("sprites/man_2.png"), Actor("sprites/woman_2.png")]

left_locations =  [Location(2, 0), 
                   Location(2, 1), Location(2, 2), 
                   Location(1, 1), Location(1, 2), 
                   Location(0, 1), Location(0, 2)] 
right_locations = [Location(4, 0), 
                   Location(4, 1), Location(4, 2), 
                   Location(5, 1), Location(5, 2), 
                   Location(6, 1), Location(6, 2)] 

for i in range(7):
    addActorNoRefresh(actors[i], left_locations[i])
for i in range(3):    
   getBg().fillCell(Location(3, i), Color.blue)   
refresh()

startState = 0
showState(startState) 
