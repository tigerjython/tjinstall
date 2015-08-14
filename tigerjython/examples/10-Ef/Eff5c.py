# Eff5c.py
# Laufende Grafik, mit sichtbarem Backtrack

from gamegrid import *
from sys import exit

m = 5
n = 5

def drawBoard():
    for i in range(m):
        for k in range(n):
            if (i + k) % 2 == 0:
                getBg().fillCell(Location(i, k), Color.lightGray)

def squareToNum(square):
    return square[0] + m * square[1]

def numToSquare(z):
     x = z % m
     y = z // m
     return [x, y]

def getNeighbours(node):
    occupied = []
    for z in node:
        occupied.append(numToSquare(z))
    lastNum = node[len(node) - 1]    
    x = numToSquare(lastNum)[0]
    y = numToSquare(lastNum)[1]
    jumps = [[x-1, y-2], [x+1, y-2], [x+2, y-1], [x+2, y+1],
             [x+1, y+2], [x-1, y+2], [x-2, y+1], [x-2, y-1]]
    allowed = []
    for jump in jumps:
        x = jump[0]
        y = jump[1]
        if not (x < 0 or x > m - 1 or y < 0 or y > n - 1 or jump in occupied):
            allowed.append(jump)         
    neighbours = []
    for square in allowed:
        current = node[:]
        current.append(squareToNum(square))
        neighbours.append(current)
    return neighbours

def search(node):
    global targetFound, count, maxLen
    if targetFound or isDisposed():
        exit()
    visited.append(node)  # push
    maxLen = max(maxLen, len(node))
    count += 1

    removeAllActors()    
    for i in range(len(node) - 1):
        addActorNoRefresh(Actor("sprites/chesswhite_3.png"), Location(numToSquare(node[i])[0], numToSquare(node[i])[1]))
    addActor(Actor("sprites/chessblack_3.png"), Location(numToSquare(node[len(node) - 1])[0], numToSquare(node[len(node) - 1])[1]))
    setTitle("Suchschritt: " + str(count) + ", Gesetzte: " + str(len(node)) + " (max: " + str(maxLen) + ")")
    delay(1000)

    # Check for termination
    if len(node) == m * n:
        targetFound = True
        setTitle("Suchschritt: " + str(count) +  ", Ziel erreicht")
        return
        
    for neighbour in getNeighbours(node):
        if neighbour not in visited:
            backSteps = [node]
            backStepsList.append(backSteps)
            backSteps.append(neighbour)
          
            search(neighbour) # recursive call

            backSteps.reverse()
            for p in backSteps:
               setTitle("Muss  zurückgehen...")
               loc = Location(numToSquare(p[len(p) - 1])[0], numToSquare(p[len(p) - 1])[1])
               addActorNoRefresh(Actor("sprites/checkred.gif"), loc)
               refresh()
               delay(1000)
            backStepsList.pop()
            
    visited.pop() # pop

targetFound = False
visited = []
count = 0
maxLen = 0
backStepsList = []

makeGameGrid(m, n, 600 // max(m, n), False)
setBgColor(Color.darkGray)
show()
drawBoard()

startNode = [0]
search(startNode)
