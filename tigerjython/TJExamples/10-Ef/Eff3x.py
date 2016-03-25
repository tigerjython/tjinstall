# Eff3x.py
# FEHLER: Rücklauf von Knoten 13 auf Knoten 0

neighbours = [[4, 1, 16], [2, 5, 7], [], [], [9, 13], [11, 14], [], [], 
             [17, 6, 3], [], [], [], [], [10, 12, 0], [], [], [15, 8], []] 

def search(node):
    visited.append(node) # put (push) to stack

    # Check for solution
    if node == targetNode:
        print "Ziel ", targetNode, "erreicht. Pfad:", visited
        targetFound = True
        return
        
    for neighbour in neighbours[node]:
        search(neighbour) # recursive call
    visited.pop() # redraw (pop) from stack

startNode = -1
while startNode < 0 or startNode > 17:
   startNode = inputInt("Startknoten (0..17):")
targetNode = -1
while targetNode < 0 or targetNode > 17:
   targetNode = inputInt("Zielknoten (0..17):")
visited = []
search(startNode)
