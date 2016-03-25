from gamegrid import *
from entrydialog import *

neighbours = {
 'Althaus':['Bellevue', 'Dom', 'Enge'], 
 'Bellevue':['Althaus', 'City', 'Dom'], 
 'City':['Bellevue', 'Dom', 'Friedhof'], 
 'Dom':['Althaus', 'Bellevue', 'City', 'Enge', 'Friedhof'], 
 'Enge':['Althaus', 'Dom'], 
 'Friedhof':['Althaus', 'City', 'Dom']}

distances = {
   ('Althaus', 'Bellevue'):5, ('Althaus', 'Dom'):9, 
   ('Althaus', 'Enge'):6, ('Althaus', 'Friedhof'):15,
   ('Bellevue', 'City'):3, ('Bellevue', 'Dom'):13, 
   ('City', 'Dom'):4, ('City', 'Friedhof'):3, 
   ('Dom', 'Enge'):2, ('Dom', 'Friedhof'):12}

locations = {
 'Althaus':Location(2, 0), 
 'Bellevue':Location(0, 1), 
 'City':Location(1, 3), 
 'Dom':Location(4, 2), 
 'Enge':Location(5, 0), 
 'Friedhof':Location(3, 4)}

def getNeighbourDistance(station1, station2):
    if station1 < station2:
        return distances[(station1, station2)]
    return distances[(station2, station1)]

def totalDistance(li):
    sum = 0
    for i in range(len(li) - 1):
        sum += getNeighbourDistance(li[i], li[i + 1])
    return sum

def drawGraph():
    getBg().clear()
    getBg().setPaintColor(Color.blue)
    getBg().setLineWidth(1)
    for station in locations:
        location = locations[station]
        getBg().fillCircle(toPoint(location), 10) 
        startPoint = toPoint(location)
        getBg().drawText(station, startPoint)
        for s in neighbours[station]:
            drawConnection(station, s)
            if s < station:
                distance = distances[(s, station)]
            else:
                distance = distances[(station, s)]
            endPoint = toPoint(locations[s]) 
            getBg().drawText(str(distance), 
                   getDividingPoint(startPoint, endPoint, 0.5))
    refresh()
         
def drawConnection(startStation, endStation):
    startPoint = toPoint(locations[startStation])
    endPoint = toPoint(locations[endStation])
    getBg().drawLine(startPoint, endPoint)

def search(station):
    global trackToTarget, trackLength    
    visited.append(station)  # station marked as visited

    # Check for solution
    if station == targetStation:
        currentDistance = totalDistance(visited)
        if currentDistance < trackLength:
            trackLength = currentDistance
            trackToTarget = visited[:]
        
    for s in neighbours[station]:
        if s not in visited:  # if all are visited, recursion returns
            search(s) # recursive call
    visited.pop() # station may be visited by another path 

def init():
    global visited, trackToTarget, trackLength
    visited = []
    trackToTarget = [] 
    trackLength = 1000
    drawGraph()
    
makeGameGrid(7, 5, 100, None, "sprites/city.png", False)
setTitle("City Guide")
addStatusBar(30)
setStatusText("What is your journey?") 
show()
init()
entry1 = StringEntry("Start:", "Althaus")
entry2 = StringEntry("Target:", "Dom")
pane1 = EntryPane(entry1, entry2)
btn = ButtonEntry("Search")
pane2 = EntryPane(btn)
dlg = EntryDialog(10, 600, pane1, pane2)

while not dlg.isDisposed():
    if isDisposed():
        dlg.dispose()
        break
    if btn.isTouched():
        init()
        startStation = entry1.getValue()
        targetStation = entry2.getValue()
        if not (startStation in locations.keys() and targetStation in locations.keys()):
            setStatusText("Illegal station name")
            continue
        search(startStation)
        setStatusText("Shortest way from " + startStation + " to " + targetStation 
           + ": " + ",".join(trackToTarget) + ". Length = " + str(trackLength))
        for i in range(len(trackToTarget) - 1):
            s1 = trackToTarget[i]
            s2 = trackToTarget[i + 1]
            getBg().setPaintColor(Color.black)
            getBg().setLineWidth(3)
            drawConnection(s1, s2)
        refresh()   
dispose()