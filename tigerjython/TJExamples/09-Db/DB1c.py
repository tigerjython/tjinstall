import pickle
import os
from gamegrid import *

class Lobster(Actor):
   def __init__(self):
      Actor.__init__(self, True, "sprites/lobster.gif");
    
   def act(self):
      self.move()
      if not self.isMoveValid():
          self.turn(90)
          self.move()
          self.turn(90)

makeGameGrid(10, 2, 60, Color.red)
addStatusBar(30)
show()

path = "lobstergame.dat"
simulationPeriod = 500
startLocation = Location(0, 0)
if os.path.isfile(path):
    inp = open(path, "rb")
    dataDict = pickle.load(inp)
    inp.close()
    # Reading old game state
    simulationPeriod = dataDict["SimulationPeriod"]
    loc = dataDict["EndLocation"]
    location = Location(loc[0], loc[1])
    direction = dataDict["EndDirection"]
    setStatusText("Game state restored.")
else:
    location = startLocation
    direction = 0
    
clark = Lobster()
addActor(clark, startLocation)
clark.setLocation(location)
clark.setDirection(direction)
setSimulationPeriod(simulationPeriod)

while not isDisposed():
    delay(100)
gameData = {"SimulationPeriod": getSimulationPeriod(), 
            "EndLocation": [clark.getX(), clark.getY()],
            "EndDirection": clark.getDirection()}    
out = open(path, "wb")
pickle.dump(gameData, out)
out.close()
print "Game state saved"
    
