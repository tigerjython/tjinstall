# Ah1b.py
# Sudoku, isValid

from gamegrid import *

def pressEvent(e):
    loc = toLocationInGrid(e.getX(), e.getY())
    if loc in fixedLocations:
        setStatusText("Location fixed")
        return
    x = loc.x
    y = loc.y
    value = startState[y][x]
    value = (value + 1)  % 10
    startState[y][x] = value
    showState(startState)
    if isValid(startState):
        setStatusText("State valid")
    else:
        setStatusText("Invalid state")

def getBlockValues(state, x, y):
    return [state[y][x], state[y][x + 1], state[y][x + 2], 
            state[y + 1][x], state[y + 1][x + 1], state[y + 1][x + 2],
            state[y + 2][x], state[y + 2][x + 1], state[ y + 2][x + 2]]
           
def showState(state):
    removeAllActors()
    for y in range(9):
        for x in range(9):
            loc = Location(x, y)
            value = state[y][x]
            if  value != 0:
                if loc in fixedLocations:
                    c = Color.black
                else:
                    c = Color.red
                digit = TextActor(str(value), c, Color.white, Font("Arial", Font.BOLD, 20))
                addActorNoRefresh(digit, loc)
    refresh()

def isValid(state):
    # Check lines
    for y in range(9):
        values = []
        for x in range(9):
            value = state[y][x]
            if value > 0 and value in values:
                return False
            else:
                values.append(value)    
    # Check rows
    for x in range(9):
        values = []
        for y in range(9):
            value = state[y][x]
            if value > 0 and value in values:
                return False
            else:
                values.append(value)    

    # Check blocks
    for yblock in range(3):
        for xblock in range(3):
            values = []
            li = getBlockValues(state, 3 * xblock, 3 * yblock)
            for value in li:
                if value > 0 and value in values:
                    return False
                else:
                    values.append(value)
    return True

makeGameGrid(9, 9, 50, Color.red, False, mousePressed = pressEvent)
show()
setTitle("Sudoku")
addStatusBar(30)
setBgColor(Color.white)
getBg().setLineWidth(3)
getBg().setPaintColor(Color.red)
for x in range(4):
    getBg().drawLine(150 * x, 0, 150 * x, 450) 
for y in range(4):
    getBg().drawLine(0, 150 * y, 450, 150 * y) 

startState = [ \
[0, 6, 0, 7, 9, 8, 0, 1, 2],
[7, 9, 4, 1, 0, 5, 0, 6, 8],
[2, 0, 1, 4, 0, 0, 9, 5, 7],
[0, 0, 0, 2, 1, 0, 5, 0, 0],
[0, 5, 6, 3, 0, 0, 2, 4, 1],
[0, 1, 2, 5, 4, 0, 7, 3, 9],
[6, 3, 0, 8, 7, 4, 0, 0, 0],
[1, 0, 5, 6, 0, 2, 8, 0, 0],
[4, 2, 8, 9, 0, 1, 0, 7, 0]]
      
fixedLocations = [] 
for x in range(9):
    for y in range(9):
        if startState[y][x] != 0:
            fixedLocations.append(Location(x, y))

showState(startState)
