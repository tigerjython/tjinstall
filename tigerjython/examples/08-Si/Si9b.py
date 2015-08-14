from gamegrid import *
import math
import random

# =================== class Tree =======================
class Tree(Actor):
    def __init__(self):
        Actor.__init__(self, "sprites/tree1.png")

# =================== class Bird =======================
class Bird(Actor):
    def __init__(self):
        Actor.__init__(self, True, "sprites/arrow1.png")
        self.r = GGVector(0, 0)  # Position
        self.v = GGVector(0, 0)  # Velocity
        self.a = GGVector(0, 0)  # Acceleration
 
    # Called when actor is added to gamegrid
    def reset(self):
        self.r.x = self.getX()
        self.r.y = self.getY()
        self.v.x = startVelocity * math.cos(math.radians(self.getDirection()))
        self.v.y = startVelocity * math.sin(math.radians(self.getDirection()))
  
    # ----------- cohesion ---------------
    def cohesion(self, distance):
        return self.getCenterOfMass(distance).sub(self.r)

    # ----------- alignment --------------
    def alignment(self, distance):
        align = self.getAverageVelocity(distance)
        align = align.sub(self.v)
        return align

    # ----------- separation -------------
    def separation(self, distance):
        repulse = GGVector()
        # ------ from birds ------
        for p in birdPositions:
            dist = p.sub(self.r)
            d = dist.magnitude()
            if d < distance and d != 0:
                repulse = repulse.add(dist.mult((d - distance) / d))

        # ------ from trees ------
        trees = self.gameGrid.getActors(Tree)
        for actor in trees:
            p = GGVector(actor.getX(), actor.getY())
            dist = p.sub(self.r)
            d = dist.magnitude()
            if d < distance and d != 0:
               repulse = repulse.add(dist.mult((d - distance) / d))
        return repulse
  
    # ----------- wall interaction -------
    def wallInteraction(self):
        width = self.gameGrid.getWidth()
        height = self.gameGrid.getHeight()
        acc = GGVector()
        if self.r.x < wallDist:
            distFactor = (wallDist - self.r.x) / wallDist
            acc = GGVector(wallWeight * distFactor, 0)
        if width - self.r.x < wallDist:
            distFactor = ((width - self.r.x) - wallDist) / wallDist
            acc = GGVector(wallWeight * distFactor, 0)
        if self.r.y < wallDist:
            distFactor = (wallDist - self.r.y) / wallDist
            acc = GGVector(0, wallWeight * distFactor)
        if height - self.r.y < wallDist:
            distFactor = ((height - self.r.y) - wallDist) / wallDist
            acc = GGVector(0, wallWeight * distFactor)
        return acc
  
    def getPosition(self):
        return self.r
      
    def getVelocity(self):
        return self.v

    def getCenterOfMass(self, distance):
        center = GGVector()
        sum = 0
        for p in birdPositions:
            dist = p.sub(self.r)
            d = dist.magnitude()
            if d < distance:
                center = center.add(p)
                sum += 1
        if sum != 0:        
            return center.mult(1.0/sum)
        else:
            return center

    def getAverageVelocity(self, distance):
        avg = GGVector()
        sum = 0
        for i in range(len(birdPositions)):
            p = birdPositions[i]
            if (self.r.x - p.x) * (self.r.x - p.x) + \
               (self.r.y - p.y) * (self.r.y - p.y) < distance * distance:
                avg = avg.add(birdVelocities[i]);
                sum += 1
        return avg.mult(1.0/sum)

    def limitSpeed(self):
        m = self.v.magnitude()
        if m < minSpeed:
            self.v = self.v.mult(minSpeed / m)
        if m > maxSpeed:
            self.v = self.v.mult(minSpeed / m)

    def setAcceleration(self):
        self.a = self.cohesion(cohesionDist).mult(cohesionWeight)
        self.a = self.a.add(self.separation(separationDist).mult(separationWeight))
        self.a = self.a.add(self.alignment(alignmentDist).mult(alignmentWeight))
        self.a = self.a.add(self.wallInteraction())

    def act(self):
        self.setAcceleration()
        self.v = self.v.add(self.a) # new velocity
        self.limitSpeed()
        self.r = self.r.add(self.v) # new position
        self.setDirection(int(math.degrees(self.v.getDirection())))
        self.setLocation(Location(int(self.r.x), int(self.r.y)))


# =================== global section ==================
def populateTrees(number):
    blockSize = 70
    treesPerBlock = 10
    for block in range(number // treesPerBlock):
        x = getRandomNumber(800 // blockSize) * blockSize
        y = getRandomNumber(600 // blockSize) * blockSize
        for t in range(treesPerBlock):
            dx = getRandomNumber(blockSize)
            dy = getRandomNumber(blockSize)
            addActor(Tree(), Location(x + dx, y + dy))
                
def generateBirds(number):
    for i in range(number):
        addActorNoRefresh(Bird(), getRandomLocation(), 
                                  getRandomDirection())
    onAct()  # Initialize birdPositions, birdVelocities
     
def onAct():
    global birdPositions, birdVelocities
    # Update bird positions and velocities
    birdPositions = []
    birdVelocities = []
    for b in getActors(Bird):
        birdPositions.append(b.getPosition())
        birdVelocities.append(b.getVelocity())
 
def getRandomNumber(limit):
    return random.randint(0, limit-1)

# coupling constants 
cohesionDist = 100
cohesionWeight = 0.01
alignmentDist = 30
alignmentWeight = 1
separationDist = 30
separationWeight = 0.2
wallDist = 20
wallWeight = 2
maxSpeed = 20
minSpeed = 10
startVelocity = 10
numberTrees = 100
numberBirds = 50

birdPositions  = []
birdVelocities  = []

makeGameGrid(800, 600, 1, False)
registerAct(onAct)
setSimulationPeriod(10)
setBgColor(makeColor(25, 121, 212))
setTitle("Swarm Simulation")
show()
populateTrees(numberTrees)
generateBirds(numberBirds)
doRun()

