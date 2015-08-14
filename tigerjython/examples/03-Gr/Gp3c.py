from gpanel import *

def drawStone(x, y):
   setColor(getRandomX11Color())
   move(x + SIZE/2, y + SIZE/2)
   fillRectangle(SIZE, SIZE)

makeGPanel(0, 400, 0, 400)

SIZE = 50

for x in range(0, 400, SIZE):
   for y in range(0, 400, SIZE):
      drawStone(x, y)     

