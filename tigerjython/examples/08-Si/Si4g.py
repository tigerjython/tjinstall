from gamegrid import *
import random
import time

min = 2
max = 10

def random_t():
    return min + (max - min) * random.random()

# ---------------- class PassengerFactory ----------
class PassengerFactory(Actor):
    def __init__(self):
        self.nbPassenger = 0

    def board(self):
        for passenger in getActors(Passenger):
            passenger.removeSelf()
            passenger.board()
        self.nbPassenger = 0
    
    def act(self):
        if self.nbCycles % 10 == 0:
            passenger = Passenger(random.randint(0, 1))
            addActor(passenger, Location(400, 120 + 27 * self.nbPassenger))
            self.nbPassenger += 1

# ---------------- class Passenger -----------------
class Passenger(Actor):
    totalTime = 0
    totalNumber = 0

    def __init__(self, i):
        Actor.__init__(self, "sprites/pupil_" + str(i) + ".png")
        self.createTime = time.clock()

    def board(self):
        self.waitTime = time.clock() - self.createTime
        Passenger.totalTime += self.waitTime
        Passenger.totalNumber += 1
        mean = Passenger.totalTime / Passenger.totalNumber
        setStatusText("Mean waiting time: " + str(round(mean, 2)) + " s")
          
# ---------------- class Car -----------------------
class Bus(Actor):
    def __init__(self, lag):
        Actor.__init__(self, "sprites/car1.gif")
        self.lag = lag
        self.isBoarded = False

    def act(self):
        self.move()
        if self.getX() > 320 and not self.isBoarded:
            passengerFactory.board()
            self.isBoarded = True
            infoPanel.setWaitingTime(self.lag)
        if self.getX() > 1650:
            self.removeSelf()
     
# ---------------- class InformationPanel ----------
class InformationPanel(Actor):
    def __init__(self, waitingTime):
        Actor.__init__(self, "sprites/digit.png", 10)
        self.waitingTime = waitingTime

    def setWaitingTime(self, waitingTime):
        self.waitingTime = waitingTime
    
    def act(self):
        self.show(int(self.waitingTime + 0.5))
        if self.waitingTime > 0:
            self.waitingTime -= 0.1

periodic = askYesNo("Departures every 6 s?")
makeGameGrid(800, 600, 1, None, None, False)
addStatusBar(20)
setStatusText("Acquiring data...")
setBgColor(Color.white)
setSimulationPeriod(50)
show()
doRun()
if periodic:
    setTitle("Warting Time Paradoxon - Departure every 6 s")
else:
    setTitle("Waiting Time Paradoxon - Departure between 2 s and 10 s")

passengerFactory = PassengerFactory()
addActor(passengerFactory, Location(0, 0))

addActor(Actor("sprites/panel.png"), Location(500, 120))
addActor(TextActor("Next Bus"), Location(460, 110))
addActor(TextActor("s"), Location(540, 110))
infoPanel = InformationPanel(4)
infoPanel.setSlowDown(2)
addActor(infoPanel, Location(525, 110))

while not isDisposed():
    if periodic:
        lag = 6
    else:
        lag = random_t()
    bus = Bus(lag)
    addActor(bus, Location(-100, 40))
    a = time.clock()
    while time.clock() - a < lag and not isDisposed():
        delay(10)

