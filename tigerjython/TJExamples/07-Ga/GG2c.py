from gamegrid import *

# ---------------- class Animal ----------------
class Animal():
    def __init__(self, imgPath): 
        self.imagePath = imgPath 
    def showMe(self, x, y):  
         bg.drawImage(self.imagePath, x, y) 
         
# ---------------- class Pet ----------------
class Pet(Animal): 
    def __init__(self, imgPath, name): 
        Animal.__init__(self, imgPath) 
        self.name = name
    def tell(self, x, y):
        bg.drawText(self.name, Point(x, y))

# ---------------- class Dog ----------------
class Dog(Pet):
    def __init__(self, imgPath, name): 
        Pet.__init__(self, imgPath, name)       
    def tell(self, x, y): # Overriding
        bg.setPaintColor(Color.blue)
        bg.drawText(self.name + " tells 'Waoh'", Point(x, y))

# ---------------- class Cat ----------------
class Cat(Pet):
    def __init__(self, imgPath, name):
        Pet.__init__(self, imgPath, name) 
    def tell(self, x, y): # Overriding
        bg.setPaintColor(Color.gray)
        bg.drawText(self.name + "  tells 'Meow'", Point(x, y))

makeGameGrid(600, 600, 1, False)
setBgColor(Color.green)
show()
doRun()
bg = getBg()

alex = Dog("sprites/dog.gif", "Alex")
alex.showMe(100, 100) 
alex.tell(200, 130)  # Overriden method is called

rex = Dog("sprites/dog.gif", "Rex")
rex.showMe(100, 300) 
rex.tell(200, 330)  # Overriden method is called

xara = Cat("sprites/cat.gif", "Xara")
xara.showMe(100, 500) 
xara.tell(200, 530)  # Overriden method is called

