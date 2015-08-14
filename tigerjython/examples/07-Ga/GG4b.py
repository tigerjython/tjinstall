from gamegrid import *

def getRemoveMarble(start, dest):
    if getOneActorAt(start) == None:
        return None
    if getOneActorAt(dest) != None:
        return None
    if not isMarbleLocation(dest):
        return None
    if dest.x - start.x == 2 and dest.y == start.y:
        return getOneActorAt(Location(start.x + 1, start.y))
    if start.x - dest.x == 2 and dest.y == start.y:
        return getOneActorAt(Location(start.x - 1, start.y))
    if dest.y - start.y == 2 and dest.x == start.x:
        return getOneActorAt(Location(start.x, start.y + 1))
    if start.y - dest.y == 2 and dest.x == start.x:
        return getOneActorAt(Location(start.x, start.y - 1))

def isMarbleLocation(loc):
    if loc.x < 0 or loc.x > 6 or loc.y < 0 or loc.y > 6:
        return False
    if (loc.x == 0 or loc.x == 1 or loc.x == 5 or loc.x == 6) and \
       (loc.y == 0 or loc.y == 1 or loc.y == 5 or loc.y == 6):
        return False
    return True

def initBoard():
    for x in range(7):
        for y in range(7):
            loc = Location(x, y)
            if isMarbleLocation(loc):
                marble = Actor("sprites/marble.png")
                addActor(marble, loc)
    removeActorsAt(Location(3, 3)) # Remove marble in center

def pressEvent(e):
    global startLoc, movingMarble
    startLoc = toLocationInGrid(e.getX(), e.getY())
    movingMarble = getOneActorAt(startLoc)
    if movingMarble == None:
       setStatusText("Pressed at " + str(startLoc) + ". No marble found")
    else:
       setStatusText("Pressed at " + str(startLoc) + ". Marble found")

def dragEvent(e):
    if movingMarble == None:
        return
    startPoint = toPoint(startLoc)
    movingMarble.setLocationOffset(e.getX() - startPoint.x, 
                                   e.getY() - startPoint.y) 

def releaseEvent(e):
    if movingMarble == None:
        return
    destLoc = toLocationInGrid(e.getX(), e.getY())
    movingMarble.setLocationOffset(0, 0)
    removeMarble = getRemoveMarble(startLoc, destLoc)
    if removeMarble == None:
        setStatusText("Released at " + str(destLoc) + ". Not a valid move.")
    else:
        removeActor(removeMarble)
        movingMarble.setLocation(destLoc)    
        setStatusText("Released at " + str(destLoc)+ ". Marble removed.")
    

startLoc = None
movingMarble = None

makeGameGrid(7, 7, 70, None, "sprites/solitaire_board.png", False,
    mousePressed = pressEvent, mouseDragged = dragEvent, 
    mouseReleased = releaseEvent)
setBgColor(Color(255, 166, 0))
setSimulationPeriod(20)
addStatusBar(30)
setStatusText("Press-drag-release to make a move.")
initBoard()
show()
doRun()
