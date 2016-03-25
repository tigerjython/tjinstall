# Eff1d.py

from gamegrid import *
import random

def bodyHeight(dwarf):
    return dwarf.getImage().getHeight()

def compare(dwarf1, dwarf2):
    if bodyHeight(dwarf1) < bodyHeight(dwarf2):
        return -1
    elif bodyHeight(dwarf1) > bodyHeight(dwarf2):
        return 1
    else:
        return 0

def updateGrid():
   removeAllActors()
   for i in range(len(li)):
       addActor(li[i], Location(i, 0))

n = 7
li = []

makeGameGrid(n, 1, 170, Color.red, False)
setBgColor(Color.white)
show()
for i in range(0 , n):
    dwarf = Actor("sprites/dwarf" + str(i) + ".png")
    li.append(dwarf)
random.shuffle(li)
updateGrid()
setTitle("Timsort. Press any key to get result...")
getKeyCodeWait()
li = sorted(li, cmp = compare)
updateGrid()

setTitle("All done.")

   
