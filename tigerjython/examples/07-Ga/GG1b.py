from gamegrid import *

# ---------------- class Alien ----------------
class Alien(Actor):
    def __init__(self):
        Actor.__init__(self, "sprites/alien.png")
    
    def act(self):
        self.move()

makeGameGrid(10, 10, 60, Color.red, "sprites/town.jpg", False)
spin = Alien() # object creation, many instances can be created
urix = Alien()
addActor(spin, Location(2, 0), 90)
addActor(urix, Location(5, 0), 90)
show()
doRun()

