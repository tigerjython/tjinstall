# Eff4-2.py
# Zweikrügeproblem
state = [4,2]

def transfer(state, source, target):
    # Assumption: source, target 0..2, 2: see; source != target
    s = state[:] # clone

    # vom krug 1 in krug 2
    if source == 0 and target == 1:
        if s[0] == 0 or s[1] == capacity[1]: # krug 1 leer oder krug 2 voll
             return s
        free = capacity[1] - s[1]
        if s[0] <= free: # krug 1 hat Platz
            s[1] += s[0]
            s[0] = 0
        else:  # krug 2 wird gefuellt
            s[1] = capacity[1]
            s[0] -= free
    
    # vom krug 1 in see
    if source == 0 and target == 2:
        if s[0] == 0:  # krug 1 leer
            return s
        s[0] = 0
        
    # vom krug 2 in krug 1
    if source == 1 and target == 0:
        if s[1] == 0 or s[0] == capacity[0]: # krug 2 leer oder krug 1 voll
             return s
        free = capacity[0] - s[0]
        if s[1] <= free: # krug 0 hat Platz
            s[0] += s[1]
            s[1] = 0
        else:  # krug 1 wird gefuellt
            s[0] = capacity[0]
            s[1] -= free

    # vom krug 2 in see
    if source == 1 and target == 2:
        if s[1] == 0:  # krug 2 leer
            return s
        s[1] = 0
    
    # vom see in krug 0
    if source == 2 and target == 0:
        if s[0] == capacity[0]:
            return s # krug voll
        s[0] = capacity[0]  # fuelle krug

    # vom see in krug 1
    if source == 2 and target == 1:
        if s[1] == capacity[1]:
            return s # krug voll
        s[1] = capacity[1]  # fuelle krueg
    return s

def getNeighbours(node):
# returns list of neighbours
    neighbours = []
    t = transfer(node, 0, 1) # from 0 to 1
    if t not in neighbours:
       neighbours.append(t)
    t = transfer(node, 0, 2) # from 0 to 2
    if t not in neighbours:
        neighbours.append(t)
    t = transfer(node, 1, 0) # from 1 to 0
    if  t not in neighbours:
        neighbours.append(t)
    t = transfer(node, 1, 2) # from 1 to 2
    if t not in neighbours:
        neighbours.append(t)
    t = transfer(node, 2, 0) # from 2 to 0
    if t not in neighbours:
        neighbours.append(t)
    t = transfer(node, 2, 1) # from 2 to 1
    if t not in neighbours:
        neighbours.append(t)
    return neighbours

def search(node):
    global nbSolution    
    visited.append(node)

    # Check for solution
    if node == targetNode:
        nbSolution += 1
        print nbSolution, ". Weg:", visited, ". Länge:", len(visited)
        
    for s in getNeighbours(node):
        if s not in visited: 
            search(s)
    visited.pop() 
 
capacity = [5, 3]
startNode = [0, 0]
targetNode = [4, 0]
nbSolution = 0
visited = []
#s = [3, 3]
#print transfer(s, 1, 0)
search(startNode)
print "Geschafft."
