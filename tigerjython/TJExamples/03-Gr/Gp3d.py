# Gb5d.py

from gpanel import *
makeGPanel(0, 400, 0, 400)

def drawStone(x, y):
   SIZE = 10
   setColor(getRandomX11Color())
   move(x + SIZE/2, y + SIZE/2)
   fillRectangle(SIZE, SIZE)

SIZE = 50

for x in range(0, 400, SIZE):
   for y in range(0, 400, SIZE):
      drawStone(x, y)

print SIZE
