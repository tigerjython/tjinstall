# Eff1b.py
# Insertion sort

from gamegrid import *
import random

def cardValue(card):
    return card.getImage().getHeight()

def updateGrid():
   removeAllActors()
   for i in range(len(startList)):
       addActor(startList[i], Location(i, 0))
   for i in range(len(targetList)):
       addActor(targetList[i], Location(i, 1))

n = 9

makeGameGrid(n, 2, 130, Color.blue, False)
setBgColor(Color.white)
show()

startList = []
targetList = []

for i in range(0 , 9):
    card = Actor("sprites/" + "hearts" + str(i) + ".png")
    startList.append(card)

random.shuffle(startList)
updateGrid()
setTitle("Insertion Sort. Press <SPACE> to sort...")
count = 0

while not isDisposed() and len(startList) > 0:
    getBg().clear()
    c = getKeyCodeWait()
    if c == 32:
        pick = startList[0] # take first
        startList.remove(pick)
        i = 0
        while  i < len(targetList) and cardValue(pick) > cardValue(targetList[i]):
            i += 1
            count += 1
        targetList.insert(i, pick)
        count += 1
        setTitle("Count: " + str(count) + " <SPACE> for next step...")
        updateGrid()
setTitle("Count: " + str(count) + " All done")

   
