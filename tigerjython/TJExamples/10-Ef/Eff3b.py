

from gamegrid import *

neighbours = [[4, 1, 16], [2, 5, 7], [], [], [9, 13], [11, 14], [], [], 
             [17, 6, 3], [], [], [], [], [10, 12], [], [], [15, 8], []] 

locations = [Location(6, 0), Location(6, 1), Location(4, 2), Location(13, 3),
             Location(1, 1), Location(6, 2), Location(12, 3), Location(8, 2),
             Location(12, 2), Location(0, 2), Location(1, 3), Location(5, 3),
             Location(3, 3), Location(2, 2), Location(7, 3), Location(10, 2), 
             Location(11, 1), Location(11, 3)]

def drawGraph():
    getBg().clear()
    for i in range(len(locations)):
        getBg().setPaintColor(Color.lightGray)
        getBg().fillCircle(toPoint(locations[i]), 6) 
        getBg().setPaintColor(Color.black)
        getBg().drawText(str(i), toPoint(locations[i]))
        for k in neighbours[i]:
            drawConnection(i, k)
    refresh()

def drawConnection(i, k):
    getBg().setPaintColor(Color.gray)
    startPoint = toPoint(locations[i])
    endPoint = toPoint(locations[k])
    getBg().drawLine(startPoint, endPoint) 
    getBg().fillCircle(getMarkerPoint(endPoint, startPoint, 10), 3)

def search(node):
    global targetFound
    if targetFound:
        return
    visited.append(node) # put (push) to stack
    alien.setLocation(locations[node])
    refresh()
    if node == targetNode:
        setStatusText("Target " + str(targetNode) + "achieved. Path: " 
                      + str(visited))
        targetFound = True
        return
    else:
        setStatusText("Current node " + str(node) + " .  Visited: " 
        + str(visited))
    getKeyCodeWait(True) # exit if GameGrid is disposed
  
    for neighbour in neighbours[node]:
        search(neighbour)  # Recursive call
    visited.pop()
    
makeGameGrid(14, 4, 50, Color.red, False)
setTitle("Tree-traversal (depth-first search). Press a key...")
addStatusBar(30)
show()
setBgColor(Color.white)
drawGraph()
 
startNode = -1
while startNode < 0 or startNode > 17:
   startNode = inputInt("Start node  (0..17):")  
targetNode = -1
while targetNode < 0 or targetNode > 17:
   targetNode = inputInt("Target node  (0..17):")

visited = []
targetFound = False
alien = Actor("sprites/alieng_trans.png")
addActor(alien, locations[startNode])

search(startNode)
setTitle("Tree-traversal (depth-first search). Target achieved")

