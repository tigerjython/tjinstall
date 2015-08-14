from gamegrid import *

# ---------------- class Animal ----------------
class Animal():
    def showMe(self, x, y):
         bg.drawImage(imagePath, x, y) 

def pressCallback(e):
    myAnimal = Animal()
    myAnimal.showMe(e.getX(), e.getY())

imagePath = "sprites/animal.gif"
makeGameGrid(600, 600, 1, False, mousePressed = pressCallback)
setBgColor(Color.green)
show()
doRun()
bg = getBg()
