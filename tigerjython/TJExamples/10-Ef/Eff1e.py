

from gamegrid import *
import random

class Dwarf(Actor):
    def __init__(self, name, size):
        Actor.__init__(self, "sprites/dwarf" + str(size) + ".png")
        self.name = name
        self.size = size
    def __eq__(self, a):  # ==
        return self.size == a.size
    def __ne__(self, a): # !=
        return self.size != a.size
    def __gt__(self, a): # >
        return self.size > a.size
    def __lt__(self, a): # <
        return self.size < a.size
    def __ge__(self, a): # >=
        return self.size >= a.size
    def __le__(self, a): # <=
        return self.size <= a.size
    def __str__(self):  # str() function
        return self.name

def compare(dwarf1, dwarf2):
    if dwarf1 < dwarf2:
        return -1
    elif dwarf1 > dwarf2:
        return 1
    else:
        return 0

def updateGrid():
   removeAllActors()
   for i in range(len(row)):
       addActor(row[i], Location(i, 0))
       addActor(TextActor(str(row[i])), Location(i, 0))

n = 7
row = []
names = ["Monday", "Tuesday", "Wednesday", "Thursday", 
         "Friday", "Saturday", "Sunday"]

makeGameGrid(n, 1, 170, Color.red, False)
setBgColor(Color.white)
show()
for i in range(0 , n):
    dwarf = Dwarf(names[i], i)
    row.append(dwarf)
random.shuffle(row)
updateGrid()
setTitle("Press any key to get result...")
getKeyCodeWait()
row = sorted(row, cmp = compare)
updateGrid()
setTitle("All done.")

