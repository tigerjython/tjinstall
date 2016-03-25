from gpanel import *
import math

def sin(x):
   return math.sin(math.radians(x))

def cos(x):
   return math.cos(math.radians(x))

def cartesian(polar):
   return [polar[0] * cos(polar[1]), polar[0] * sin(polar[1])]       

def rho(phi):
   return sin(n * phi)

def doIt():
   for i in range(361):
      k = i * d
      pt = [rho(k), k]
      corners.append(pt)   
      
   draw(cartesian(corners[0]))   
   for pt in corners:
      draw(cartesian(pt))
  
corners = []
n = 3
d = 47
makeGPanel(-1.2, 1.2, -1.2, 1.2)
doIt()
printerPlot(doIt)
