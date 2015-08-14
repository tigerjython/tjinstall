from gamegrid import *

# ---------------- class Animal ----------------
class Animal():
    def __init__(self, imgPath):
        self.imagePath = imgPath  # Instance variable
    def showMe(self, x, y):  # Method definition
         bg.drawImage(self.imagePath, x, y) 

def pressCallback(e):
    myAnimal = Animal("sprites/animal.gif") # Object creation
    myAnimal.showMe(e.getX(), e.getY())  # Method call

makeGameGrid(600, 600, 1, False, mousePressed = pressCallback)
setBgColor(Color.green)
show()
doRun()
bg = getBg()

