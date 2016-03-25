import math
from gpanel import *
makeGPanel(-500, 500, -500, 500)
bgColor("darkgreen")

def step():
   global t
   x = RADIUS * math.cos(t)
   y = RADIUS * math.sin(t)
   t = t + 0.1
   if t > 6.28:
      t = 0
      setColor(getRandomX11Color())
   move(x, y)
   fillCircle(10)

t = 0
RADIUS = 200 

while True:
  step()
  delay(10)

