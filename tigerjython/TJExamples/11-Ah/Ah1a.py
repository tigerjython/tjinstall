# Ah1a.py
# Sudoku, Einlesen

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
    
makeGameGrid(9, 9, 50, Color.red, False, mousePressed = pressEvent)
show()
setTitle("Sudoku")
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
