# Eff5b.py
# Grafik am Ende

from gamegrid import *

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
    if targetFound:
        return

    visited.append(node)  # push
    maxLen = max(maxLen, len(node))
    setTitle("Suchschritt: " + str(count) + ", Gesetzte: " + str(len(node)) + "( max: " + str(maxLen) + ")")
    count += 1

    # Check for termination
    if len(node) == m * n:
        targetFound = True
        setTitle("Suchschritt: " + str(count) +  ", Ziel erreicht. Zeige Lösung:")
        for i in range(len(node)):
            loc = Location(numToSquare(node[i])[0], numToSquare(node[i])[1])
            addActor(Actor("sprites/chesswhite_3.png"), loc)
            addActor(TextActor(str(i + 1)), loc)
            if not isDisposed():
                delay(1000)
        return
        
    for neighbour in getNeighbours(node):
        if neighbour not in visited:
            search(neighbour) # recursive call
    visited.pop() # pop

targetFound = False
visited = []
count = 0
maxLen = 0

makeGameGrid(m, n, 600 // max(m, n), False)
setBgColor(Color.darkGray)
show()
drawBoard()

startNode = [0]
search(startNode)
