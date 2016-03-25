# Eff1a.py
# children sort

from gamegrid import *
import random

def bodyHeight(dwarf):
    return dwarf.getImage().getHeight()

def updateGrid():
   removeAllActors()
   for i in range(len(startList)):
       addActor(startList[i], Location(i, 0))
   for i in range(len(targetList)):
       addActor(targetList[i], Location(i, 1))

def getSmallest(li):
    global count
    smallest = li[0]
    for dwarf in li:
        count += 1
        if bodyHeight(dwarf) < bodyHeight(smallest):
            smallest = dwarf
    return smallest

n = 7

makeGameGrid(n, 2, 150, Color.red, False)
setBgColor(Color.white)
show()

startList = []
targetList = []

for i in range(0 , n):
    dwarf = Actor("sprites/dwarf" + str(i) + ".png")
    startList.append(dwarf)
random.shuffle(startList)
updateGrid()
setTitle("Children Sort. Press <SPACE> to sort...")
count = 0
while not isDisposed() and len(startList) > 0:
    c = getKeyCodeWait()
    if c == 32:
        smallest = getSmallest(startList)
        targetList.append(smallest)
        startList.remove(smallest)
        count += 1
        setTitle("Count: " + str(count) + " <SPACE> for next step...")
        updateGrid()
setTitle("Count: " + str(count) + " All done")

   
