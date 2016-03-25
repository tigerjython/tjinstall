from gamegrid import *
from gpanel import *
import math
import random

# =================== class Particle ====================
class Particle(Actor):
    def __init__(self):
        Actor.__init__(self, "sprites/ball_0.gif")
 
    # Called when actor is added to gamegrid
    def reset(self):
        self.isLeft = True
  
    def advance(self, distance):
        pt = self.gameGrid.toPoint(self.getNextMoveLocation())
        dir = self.getDirection()
        # Left/right wall
        if pt.x < 0 or pt.x > w:
            self.setDirection(180 - dir)
        # Top/bottom wall
        if pt.y < 0 or pt.y > h:
            self.setDirection(360 - dir)
        # Separation
        if (pt.y < h // 2 - r or pt.y > h // 2 + r) and \
            pt.x > self.gameGrid.getPgWidth() // 2 - 2 and \
            pt.x < self.gameGrid.getPgWidth() // 2 + 2:
                self.setDirection(180 - dir)

        self.move(distance)
        if self.getX() < w // 2:
            self.isLeft = True
        else:
            self.isLeft = False

    def act(self):
        self.advance(3)
        
    def atLeft(self):
        return self.isLeft

# =================== class CollisionListener =========
class CollisionListener(GGActorCollisionListener):
    # Collision callback: just exchange direction and speed
    def collide(self, a,  b):
        dir1 = a.getDirection()
        dir2 = b.getDirection()
        sd1 = a.getSlowDown()
        sd2 = b.getSlowDown()
        a.setDirection(dir2)
        a.setSlowDown(sd2)
        b.setDirection(dir1)
        b.setSlowDown(sd1)
        return 5  # Wait a moment until collision is rearmed


# =================== Global sections =================
def drawSeparation():
    getBg().setLineWidth(3)
    getBg().drawLine(w // 2, 0, w // 2, h // 2 - r)
    getBg().drawLine(w // 2, h, w // 2, h // 2 + r)

def init():
    collisionListener = CollisionListener()
    for i in range(nbParticles):
        particles[i] = Particle()

        # Put them at random locations, but apart of each other
        ok = False
        while not ok:
            ok = True
            loc = getRandomLocation()
            if loc.x > w / 2 - 20:
                ok = False
            continue

        for k in range(i):
            dx = particles[k].getLocation().x - loc.x
            dy = particles[k].getLocation().y - loc.y
            if dx * dx + dy * dy < 300:
                ok = False
        addActor(particles[i], loc, getRandomDirection())
        delay(100)

        # Select collision area
        particles[i].setCollisionCircle(Point(0, 0), 8)
        # Select collision listener 
        particles[i].addActorCollisionListener(collisionListener)

        # Set speed in groups of 5
        if i < 5:
            particles[i].setSlowDown(2)
        elif i < 10:
            particles[i].setSlowDown(3)
        elif i < 15:
            particles[i].setSlowDown(4)
    
    # Define collision partners
    for i in range(nbParticles):
        for k in range(i + 1, nbParticles):
            particles[i].addCollisionActor(particles[k])

def binomial(n, k):
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    k = min(k, n - k) # take advantage of symmetry
    c = 1
    for i in range(k):
        c = c * (n - i) / (i + 1)
    return c
                                    
r = 50  # Radius of hole
w = 400
h = 400
nbParticles = 20
particles = [0] * nbParticles
makeGPanel(Size(600, 300))
window(-6, 66, -2, 22)
title("Entropy")
windowPosition(600, 20)
drawGrid(0, 60, 0, 20)
makeGameGrid(w, h, 1, False)
setSimulationPeriod(10)
addStatusBar(20)
drawSeparation()
setTitle("Entropy")
show()
init()
doRun()

t = 0
while not isDisposed():
    nbLeft = 0
    for particle in particles:
        if particle.atLeft():
            nbLeft += 1
    entropy = round(math.log(binomial(nbParticles, nbLeft), 2), 1)
    setStatusText("(Left,Right) = (" + str(nbLeft) + "," + str(nbParticles - nbLeft) + ")" +
        "    Entropie = " + str(entropy) + " bit")
    if t % 60 == 0:
        clear()
        lineWidth(1)
        drawGrid(0, 60, 0, 20)
        lineWidth(3)
        move(0, entropy)
    else:
        draw(t % 60, entropy)
    t += 1
    delay(1000)
dispose() # GPanel

