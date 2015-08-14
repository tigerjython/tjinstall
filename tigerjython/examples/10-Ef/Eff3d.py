from gamegrid import *

def createMaze():
    global maze
    maze = GGMaze(11, 11)
    for x in range(11):
        for y in range(11):
            loc = Location(x, y)
            if maze.isWall(loc):
                getBg().fillCell(loc, Color(0, 50, 0))
            else:    
                getBg().fillCell(loc, Color(255, 228, 196))
    refresh()

def getNeighbours(node):
    neighbours = []
    for loc in node.getNeighbourLocations(0.5):
        if isInGrid(loc) and not maze.isWall(loc):
           neighbours.append(loc)
    return neighbours
    
def search(node):
    global targetFound, manual
    if targetFound:
        return
    visited.append(node)  # push
    alien.setLocation(node)
    refresh()
    delay(500)
    if manual:
        if getKeyCodeWait(True) == 10:  #Enter
            setTitle("Finding target...")
            manual = False

    # Check for termination
    if node == exitLocation:
        targetFound = True
        
    for neighbour in getNeighbours(node):
        if neighbour not in visited:
            backSteps = [node]
            backStepsList.append(backSteps)
            backSteps.append(neighbour)

            search(neighbour) # recursive call

            backSteps.reverse()
            if not targetFound:
                for loc in backSteps[1:]:
                    setTitle("Must go back...")
                    alien.setLocation(loc)
                    refresh()
                    delay(500)
                if manual:    
                    setTitle("Went back. Press key...")
                else:
                    setTitle("Went back. Find target...")
            backStepsList.pop()
    visited.pop() # pop

manual = True
targetFound = False
visited = []
backStepsList = []
makeGameGrid(11, 11, 40, False)
setTitle("Press a key. (<Enter> for automatic")
show()
createMaze()
startLocation = maze.getStartLocation()
exitLocation = maze.getExitLocation()
alien = Actor("sprites/alieng.png")
addActor(alien, startLocation)
search(startLocation)
setTitle("Target found")

