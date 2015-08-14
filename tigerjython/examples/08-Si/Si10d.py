# S11d.py

from gamegrid import *

# =================== class Particle ====================
class Particle(Actor):
    def __init__(self):
        Actor.__init__(self, "sprites/ball.gif", 2)
 
    # Called when actor is added to gamegrid
    def reset(p):
        p.oldPt = p.gameGrid.toPoint(p.getLocationStart())
   
    def advance(p, distance):
        pt = p.gameGrid.toPoint(p.getNextMoveLocation())
        dir = p.getDirection()
        # Left/right wall
        if pt.x < 5 or pt.x > w - 5:
            p.setDirection(180 - dir)
        # Top/bottom wall
        if pt.y < 5 or pt.y > h - 5:
            p.setDirection(360 - dir)
        p.move(distance)

    def act(p):
        p.advance(3)
        if p.getIdVisible() == 1:
            pt = p.gameGrid.toPoint(p.getLocation())
            p.getBackground().drawLine(p.oldPt.x, p.oldPt.y, pt.x, pt.y)
            p.oldPt.x = pt.x
            p.oldPt.y = pt.y

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
        return 10  # Wait a moment until collision is rearmed
    
# =================== Global section ====================
def init():
    collisionListener = CollisionListener()
    for i in range(nbParticles):
        particles[i] = Particle()
        # Put them at random locations, but apart of each other
        ok = False
        while not ok:
            ok = True
            loc = getRandomLocation()

        for k in range(i):
            dx = particles[k].getLocation().x - loc.x
            dy = particles[k].getLocation().y - loc.y
            if dx * dx + dy * dy < 300:
                ok = False
        addActor(particles[i], loc, getRandomDirection())
        # Select collision area
        particles[i].setCollisionCircle(Point(0, 0), 8)
        # Select collision listener 
        particles[i].addActorCollisionListener(collisionListener)
        # Set speed in groups of 10
        if i < 10:
            particles[i].setSlowDown(2)
        elif i < 20:
            particles[i].setSlowDown(3)
        elif i < 30:
            particles[i].setSlowDown(4)
    #  Define collision partners
    for i in range(nbParticles):
        for k in range(i + 1, nbParticles):
            particles[i].addCollisionActor(particles[k])
    particles[0].show(1)        

w = 400
h = 400
nbParticles = 40
particles = [0] * nbParticles

makeGameGrid(w, h, 1, False)
setSimulationPeriod(10)
setTitle("Brownian Movement")
show()
init()
doRun()

