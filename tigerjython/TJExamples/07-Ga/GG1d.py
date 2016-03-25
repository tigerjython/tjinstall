from gamegrid import *
import random

# ---------------- class Alien ----------------
class Alien(Actor):
    def __init__(self):
        Actor.__init__(self, "sprites/alien.png")
    
    def act(self):
        self.move()

def pressCallback(e):
    location = toLocationInGrid(e.getX(), e.getY())
    actor = getOneActorAt(location)
    if actor != None:
        removeActor(actor)
    refresh()

makeGameGrid(10, 10, 60, Color.red, "sprites/town.jpg", False, 
             mousePressed = pressCallback)
setSimulationPeriod(800)
show()
doRun()

while not isDisposed():
    alien = Alien()
    addActor(alien, Location(random.randint(0, 9), 0), 90)
    delay(1000)

