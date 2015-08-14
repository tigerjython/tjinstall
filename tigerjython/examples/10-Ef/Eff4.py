# Eff4a.py
# 5 nodes, all connected

def getNeighbours(node):
    return range(0, node) + range(node + 1, 5)

def search(node):
    global nbSolution
    visited.append(node)  # node marked as visited

    # Check for solution
    if node == targetNode:
        nbSolution += 1
        print nbSolution, ". Weg:", visited
        # don't stop to get all solutions
        
    for neighbour in getNeighbours(node):
        if neighbour not in visited: # Check if already visited
            search(neighbour) # recursive call
    visited.pop() 

startNode = 0
targetNode = 4
nbSolution = 0
visited = []
search(startNode)
