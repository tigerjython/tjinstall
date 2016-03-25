from gamegrid import *

n = 8 # number of queens

def getNeighbours(node):
    squares = [] # list of occupied squares
    for i in range(n):
        if node[i] != -1:
           squares.append(Location(node[i], i))

    forbidden = [] # list of forbidden squares
    for location in squares:
        a = location.x 
        b = location.y
        for x in range(n):
            forbidden.append(Location(x, b))  # same row
        for y in range(n):
            forbidden.append(Location(a, y))  # same column
        for loc in getDiagonalLocations(location, True):   #diagonal up
            forbidden.append(loc)
        for loc in getDiagonalLocations(location, False):  #diagonal down
            forbidden.append(loc)

    allowed = [] # list of all allowed squares = all - forbidden
    for i in range(n):
        for k in range(n):
            loc = Location(i, k)
            if not loc in forbidden:
                allowed.append(loc)

    neighbourNodes = [] 
    for loc in allowed:
        neighbourNode = node[:]
        i = loc.y # row
        k = loc.x # col
        neighbourNode[i] = k 
        neighbourNodes.append(neighbourNode)
    return neighbourNodes        

def search(node):
    global found
    if found or isDisposed(): 
        return
    visited.append(node)  # node marked as visited

    # Check for solution
    if not -1 in node: 
        found = True
        drawNode(node)
        
    for s in getNeighbours(node):
        search(s)
    visited.pop()

def drawBoard():
    for i in range(n):
        for k in range(n):
            if (i + k) % 2 == 0:
                getBg().fillCell(Location(i, k), Color.white)

def drawNode(node):
    removeAllActors()
    for i in range(n):
        addActorNoRefresh(Actor("sprites/chesswhite_1.png"), Location(node[i], i))
    refresh()

makeGameGrid(n, n, 600 // n, False)
setBgColor(Color.darkGray)
drawBoard()
show()
setTitle("Searching. Please wait..." )

visited = []
found = False
startNode = [-1] * n  # all squares empty
search(startNode)
setTitle("Search complete. ")

