# Eff5d.py
# n Queens Problem
'''
node = [1, 4, -1, 5, 3, 6, -1, 7]  wo der Index die Zeilennummer ist i = 0..7 und die Zahlen die Spaltennummer ist, wo sich auf
dieser Zeile eine Dame befindet (-1 für leere Zeile (keine Dame))a

Es hat also im node 8 Zahlen, wobei die Zahlen 0..7 höchstens einmal vorkommen, -1 aber mehrmals

 
'''

# Laufzeit ungefähr exponentiell in n

from gamegrid import *
import time

n = 8 # number of queens

def getNeighbours(node):
# Gibt eine Liste mit nodes zurück, welche ausgehend vom gegebenen node erlaubt sind, d.h. wo man eine Dame mehr gesetzt hat

    cells = [] # list of occupied cells
    for i in range(n):
        if node[i] != -1:
           cells.append([i, node[i]])

    forbidden = [] # list of forbidden cells
    for cell in cells:
        a = cell[0]
        b = cell[1]
        for i in range(n):
            forbidden.append([i, b])  # same column
        for k in range(n):
            forbidden.append([a, k])  # same row
        for loc in getDiagonalLocations(Location(a, b), True):   #diagonal up
            forbidden.append([loc.x, loc.y])
        for loc in getDiagonalLocations(Location(a, b), False):  #diagonal down
            forbidden.append([loc.x, loc.y])

    allowed = [] # list of all allowed cells = all cells - forbidden cells
    for i in range(n):
        for k in range(n):
            cell = [i, k]
            if not cell in forbidden:
                allowed.append(cell)

    neighbourNodes = []  # list of given node + one allowed cell
    for cell in allowed:
        neighbourNode = node[:]
        i = cell[0] # row
        k = cell[1] # col
        neighbourNode[i] = k 
        neighbourNodes.append(neighbourNode)
    return neighbourNodes        

def search(node):
    global nbSolution, nbSearchCalls, startTime
    if isDisposed():   # GameGrid is closed
        return
    visited.append(node)  # node marked as visited
    nbSearchCalls += 1

    # Check for solution
    if not -1 in node and not node in solutions:
        nbSolution += 1
        nbSearchCalls = 0
        elapsedTime = time.clock() - startTime
        setTitle("Lösung # " + str(nbSolution) + ".  Zeit: " + str(elapsedTime) + " s. Drücke Taste..." )
        drawSolution(node)
        solutions.append(node)    
        getKeyCodeWait(True)
        startTime = time.clock()
        setTitle("Bin am Suchen. Bitte warten..." )
        
    for s in getNeighbours(node):
        if not s in visited:  # not needed, no cycles
            search(s) # recursive call
    visited.pop()  #backtrack

def drawBoard():
    for i in range(n):
        for k in range(n):
            if (i + k) % 2 == 0:
                getBg().fillCell(Location(i, k), Color.lightGray)

def drawSolution(node):
    removeAllActors()
    for i in range(n):
        addActorNoRefresh(Actor("sprites/chesswhite_1.png"), Location(node[i], i))
    refresh()

makeGameGrid(n, n, 600 // n, False)
setBgColor(Color.darkGray)
drawBoard()
show()
setTitle("Bin am Suchen. Bitte warten..." )

visited = []
solutions = []
startNode = [-1] * n  # all cells empty
nbSolution = 0
nbSearchCalls = 0
startTime = time.clock()
search(startNode)
elapsedTime = time.clock() - startTime
setTitle("Suche beendet. " + str(nbSolution) + " Lösungen gefunden. Zeit: " + str(elapsedTime) + " s")
