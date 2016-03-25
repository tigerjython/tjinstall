# Ah1e.py
# Eifersucht, Ende

from gamegrid import *
import itertools

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
    setTitle("State: " + str(state) + ", bin: " + stateToString(state)) 
    if isStateAllowed(state):
        setStatusText("Situation allowed")
    else:
        setStatusText("Situation not allowed")
    refresh()

def stateToString(state):
    return str(bin(state)[2:]).zfill(7)

def showState(state):
    sbin = stateToString(state)
    for i in range(7):
        if sbin[i] == "0":
           actors[i].setLocation(left_locations[i])
        else:
           actors[i].setLocation(right_locations[i])
    refresh()

def getTransferInfo(state1, state2):
    state1 = state1 & 63
    state2 = state2 & 63
    mod = state1 ^ state2
    passList = []
    for n in range(6):
        if mod % 2 == 1:
            if n // 2 == 0:
                couple = "blue"
            elif n // 2 == 1:
                couple = "green"
            elif n // 2 == 2:
                couple = "red"
            if n % 2 == 0:
               passList.append("f" + couple)
            else:
               passList.append("m" + couple)
        mod = mod // 2
    return passList

def getTransferSequence(solution):
    transferSequence = []
    oldState = solution[0]
    for state in solution[1:]:
        transferSequence.append(getTransferInfo(oldState, state))
        oldState = state
    return transferSequence

def isStateAllowed(state):
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

def removeForbiddenTransfers(li):
    forbiddenPairs = [(0, 3), (0, 5), (1, 2), (2, 5), (1, 4), (3, 4)]
    allowedPairs = []
    for pair in li:
        if pair not in forbiddenPairs:
            allowedPairs.append(pair)
    return allowedPairs  
        
def getNeighbours(state):
    neighbours = []
    li_one = []  # one person in boat
    bin = stateToString(state)
    if state < 64:  # boat at left
        for i in range(6):
            if bin[6 - i] == "0":
                li_one.append(i)
        li_two = list(itertools.combinations(li_one, 2)) # two persons in boat
        li_two = removeForbiddenTransfers(li_two)
    else: # boat at right
        for i in range(6):
            if bin[6 - i] == "1":
                li_one.append(i)
        li_two = list(itertools.combinations(li_one, 2))
        li_two = removeForbiddenTransfers(li_two)

    li_values = []
    if state < 64:  # boat at left, restrict to two persons transfer
        for li in li_two:
            li_values.append(2**li[0] + 2**li[1] + 64) 
    else:  # boat at right, one or two persons transfer
        for i in li_one:
            li_values.append(2**i + 64)
        for li in li_two:
            li_values.append(2**li[0] + 2**li[1] + 64) 
   
    for value in li_values:
        v = state ^ value
        if isStateAllowed(v):  # restrict to allowed states
            neighbours.append(v)
    return neighbours

def search(state):
    visited.append(state)  # state marked as visited

    # Check for solution
    if state == targetState:
        solutions.append(visited[:])
        
    for neighbour in getNeighbours(state):
        if neighbour not in visited: # Check if already visited
            search(neighbour) # recursive call
    visited.pop() 

nbSolution = 0             
makeGameGrid(7, 3, 50, None, False, mousePressed = pressEvent)
addStatusBar(30)
setBgColor(Color.white)
setTitle("Searching...")
show()
visited = []
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
targetState = 127 
solutions = []
search(startState)

maxLength = 0
maxSolution = None
minLength = 100
minSolution = None
for solution in solutions:
    if len(solution) > maxLength:
        maxLength = len(solution)
        maxSolution = solution
    if len(solution) < minLength:
        minLength = len(solution)
        minSolution = solution
setStatusText("#Solutions: " + str(len(solutions)) + ", Min Length: " + str(minLength) + ", Max Length: " + str(maxLength))

setTitle("Press key to cycle")
oldState = startState
for state in minSolution[1:]:
    getKeyCodeWait(True)
    showState(state)
    info = getTransferInfo(oldState, state)
    setTitle("#Transferred: " + str(info))
    oldState = state
setTitle("Done. #Boat Transfers: " + str((len(minSolution) - 1)))   
