# GG5a.py

from gamegrid import *
import math

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
        self.vx = self.speed * math.cos(math.radians(self.getDirection()))
        self.vy = self.speed * math.sin(math.radians(self.getDirection()))
        
    def act(self):
        self.vy = self.vy + g * self.dt
        self.px = self.px + self.vx * self.dt
        self.py = self.py + self.vy * self.dt
        self.setLocation(Location(int(self.px), int(self.py)))
        self.setDirection(math.degrees(math.atan2(self.vy, self.vx)))
        if not self.isInGrid():
            self.removeSelf()
            crossbow.show(0) # Load crossbow

# ------ End of class definitions --------------------
        
def keyCallback(e):
    code = e.getKeyCode()   
    if code == KeyEvent.VK_UP:
        crossbow.setDirection(crossbow.getDirection() - 5)
    elif code == KeyEvent.VK_DOWN:
        crossbow.setDirection(crossbow.getDirection() + 5)
    elif code == KeyEvent.VK_SPACE:
        if crossbow.getIdVisible() == 1: # Wait until crossbow is loaded
            return
        crossbow.show(1) # crossbow is released
        dart = Dart(100)
        addActorNoRefresh(dart, crossbow.getLocation(), 
                                crossbow.getDirection())   

screenWidth = 600
screenHeight = 400
g = 9.81

makeGameGrid(screenWidth, screenHeight, 1, False, keyPressed = keyCallback)
setTitle("Use Cursor up/down to target, Space to shoot.")
setBgColor(makeColor("skyblue"))
crossbow = Crossbow()
addActor(crossbow, Location(80, 320))
setSimulationPeriod(30)
doRun()
show()

