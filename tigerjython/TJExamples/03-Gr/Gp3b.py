from gpanel import *

def drawStone(x, y):
   setColor(getRandomX11Color())
   move(x + size/2, y + size/2)
   fillRectangle(size, size)

makeGPanel(0, 400, 0, 400)

size = 50

for x in range(0, 400, size):
   for y in range(0, 400, size):
      drawStone(x, y)     

