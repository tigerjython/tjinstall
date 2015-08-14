from gpanel import *
import math
  
def rho(phi):
   return math.sin(n * phi)

def doIt():
   phi = 0
   while phi < nbTurns * math.pi:
      r = rho(phi)
      x = r * math.cos(phi)   
      y = r * math.sin(phi)   
      if phi == 0:
        move(x, y)
      else:
        draw(x, y)
      phi += dphi

n = math.sqrt(2)
dphi = 0.01
nbTurns = 100
makeGPanel(-1.2, 1.2, -1.2, 1.2)
doIt()
printerPlot(doIt)

