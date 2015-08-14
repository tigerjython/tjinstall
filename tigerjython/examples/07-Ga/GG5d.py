from gamegrid import *
import random
import math

# ---------- class Fruit ------------------------
class Fruit(Actor):
    def  __init__(self, spriteImg, vx):
        Actor.__init__(self, True, spriteImg, 2) 
        self.vx = vx
        self.vy = 0
        self.isSliced = False

    def reset(self): # Called when Fruit is added to GameGrid
        self.px = self.getX()
        self.py = self.getY()
    
    def act(self):
        self.movePhysically()
        self.turn(10)

    def movePhysically(self):
        self.dt = 0.002 * getSimulationPeriod()
        self.vy = self.vy + g * self.dt
        self.px = self.px + self.vx * self.dt
        self.py = self.py + self.vy * self.dt
        self.setLocation(Location(int(self.px), int(self.py)))
        self.cleanUp()
   
    def cleanUp(self):
        if not self.isInGrid(): 
            if not self.isSliced:
                FruitFactory.nbMissed += 1
            self.removeSelf()

    def sliceFruit(self):
        if not self.isSliced:
            self.isSliced = True
            self.show(1)
            FruitFactory.nbHit += 1
      
    def collide(self, actor1, actor2):
       actor1.sliceFruit()
       return 0

# ------ class Melon -----------
class Melon(Fruit):
    def __init__(self, vx):
        Fruit.__init__(self, "sprites/melon.gif", 2)
        self.vx = vx

# ------ class Orange -----------
class Orange(Fruit):
    def __init__(self, vx):
        Fruit.__init__(self, "sprites/orange.gif", vx)

# ------ class Strawberry -----------
class Strawberry(Fruit):
    def __init__(self, vx):
        Fruit.__init__(self, "sprites/strawberry.gif", vx)

# ------------------- class FruitFactory -------------------
class FruitFactory(Actor):
    myCapacity = 0
    myFruitFactory = None
    nbGenerated = 0
    nbMissed = 0
    nbHit = 0
        
    @staticmethod
    def create(capacity, slowDown):
        if FruitFactory.myFruitFactory == None:
            FruitFactory.myCapacity = capacity
            FruitFactory.myFruitFactory = FruitFactory()
            FruitFactory.myFruitFactory.setSlowDown(slowDown)  
        return FruitFactory.myFruitFactory

    def act(self): 
        self.createRandomFruit()

    @staticmethod
    def createRandomFruit():
        if FruitFactory.nbGenerated == FruitFactory.myCapacity:
            return
        vx = -(random.random() * 20 + 30)
        r = random.randint(0, 2)
        if r == 0:
            fruit = Melon(vx)
        elif r == 1:
            fruit = Orange(vx)
        else:
            fruit = Strawberry(vx)
        FruitFactory.nbGenerated += 1
        y = int(random.random() * screenHeight / 2)
        addActorNoRefresh(fruit, Location(screenWidth-50, y), 180)
        # for a new fruit, the collision partners are all existing darts
        fruit.addCollisionActors(toArrayList(getActors(Dart)))

# ------------------- class Crossbow -----------------------
class Crossbow(Actor):
    def __init__(self):
        Actor.__init__(self, True, "sprites/crossbow.gif", 2)

# ------ class Dart ----------------
class Dart(Actor):
    def __init__(self, speed):
        Actor.__init__(self, True, "sprites/dart.gif")
        self.speed = speed
        self.dt = 0.005 * getSimulationPeriod()

    # Called when actor is added to GameGrid
    def reset(self):
        self.px = self.getX()
        self.py = self.getY()
        dx = math.cos(math.radians(self.getDirectionStart()))
        self.vx = self.speed * dx
        dy = math.sin(math.radians(self.getDirectionStart()))
        self.vy = self.speed * dy
        
    def act(self):
        if isGameOver:
            return
        self.vy = self.vy + g * self.dt
        self.px = self.px + self.vx * self.dt
        self.py = self.py + self.vy * self.dt
        self.setLocation(Location(int(self.px), int(self.py)))
        self.setDirection(math.degrees(math.atan2(self.vy, self.vx)))
        if not self.isInGrid():
            self.removeSelf()
            crossbow.show(0) # Load crossbow

    def collide(self, actor1, actor2):
        actor2.sliceFruit()
        return 0

# ------ End of class definitions --------------------
        
def keyCallback(e):
    code = e.getKeyCode()   
    if code == KeyEvent.VK_UP:
        crossbow.setDirection(crossbow.getDirection() - 5)
    elif code == KeyEvent.VK_DOWN:
        crossbow.setDirection(crossbow.getDirection() + 5)
    elif code == KeyEvent.VK_SPACE:
        if isGameOver:
            return
        if crossbow.getIdVisible() == 1: # Wait until crossbow is loaded
            return
        crossbow.show(1) # crossbow is released
        dart = Dart(100)
        addActorNoRefresh(dart, crossbow.getLocation(), crossbow.getDirection())
        # for a new dart, the collision partners are all existing fruits
        dart.addCollisionActors(toArrayList(getActors(Fruit)))

 
FACTORY_CAPACITY = 20
FACTORY_SLOWDOWN = 35
screenWidth = 600
screenHeight = 400
g = 9.81
isGameOver = False

makeGameGrid(screenWidth, screenHeight, 1, False, keyPressed = keyCallback)
setTitle("Use Cursor up/down to target, Space to shoot.")
setBgColor(makeColor("skyblue"))
addStatusBar(30)
factory = FruitFactory.create(FACTORY_CAPACITY, FACTORY_SLOWDOWN)
addActor(factory, Location(0, 0))  # needed to run act()
crossbow = Crossbow()
addActor(crossbow, Location(80, 320))
setSimulationPeriod(30)
doRun()
show()

while not isDisposed() and not isGameOver:
   # Don't show message if same 
   oldMsg = ""
   msg = "#hit: "+str(FruitFactory.nbHit)+" #missed: "+str(FruitFactory.nbMissed)
   if  msg != oldMsg:
        setStatusText(msg)
        oldMsg = msg
   if FruitFactory.nbHit + FruitFactory.nbMissed == FACTORY_CAPACITY:
       isGameOver = True
       removeActors(Dart)
       setStatusText("You smashed " + str(FruitFactory.nbHit) + " out of " 
       + str(FACTORY_CAPACITY) + " fruits")
       addActor(Actor("sprites/gameover.gif"), Location(300, 200))
        
   delay(100)

