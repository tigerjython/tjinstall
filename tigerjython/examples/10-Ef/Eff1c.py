# Eff1c.py

from gamegrid import *
import random

def bubbleSize(bubble):
    return bubble.getImage().getHeight()

def updateGrid():
   removeAllActors()
   for i in range(len(li)):
       addActor(li[i], Location(i, 0))

def exchange(i, j):
    temp = li[i]
    li[i] = li[j]
    li[j] = temp

n = 7
li = []

makeGameGrid(n, 1, 150, Color.red, False)
setBgColor(Color.white)
show()
for i in range(0 , n):
    bubble = Actor("sprites/bubble" + str(i) + ".png")
    li.append(bubble)
random.shuffle(li)
updateGrid()
setTitle("Bubble Sort. Press <SPACE> for next step...")
k = n - 1
i = 0
count = 0
while not isDisposed() and k > 0:
    getBg().fillCell(Location(i, 0), makeColor("beige"))
    getBg().fillCell(Location(i + 1, 0), makeColor("beige"))
    refresh()
    c = getKeyCodeWait()
    if c == 32:
        count += 1
        bubble1 = li[i]
        bubble2 = li[i + 1]
        refresh()
        if bubbleSize(bubble1) > bubbleSize(bubble2):
             exchange(i, i + 1)
             setTitle("Last Action: Exchange. Count: " + str(count))
        else:
             setTitle("Last Action: No Exchange. Count: " + str(count))
        getBg().clear()        
        updateGrid()
        if i == k - 1:
            k = k - 1
            i = 0
        else:
            i += 1
getBg().clear()
refresh()
setTitle("All done. Count: " + str(count))

   
