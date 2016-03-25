# Eff5a.py
# No graphics


m = 5
n = 5

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
    print "Suchschritt: ", count, ", Gesetzte: ", len(node), "( max: ", maxLen, ")"
    count += 1

    # Check for termination
    if len(node) == m * n:
        targetFound = True
        print "Suchschritt: ", count, ", Ziel erreicht:\n", node
        return
        
    for neighbour in getNeighbours(node):
        if neighbour not in visited:
            search(neighbour) # recursive call
    visited.pop() # pop

targetFound = False
visited = []
count = 0
maxLen = 0
startNode = [0]
search(startNode)
