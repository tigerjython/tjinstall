from gpanel import *
makeGPanel(0, 400, 0, 400)

for y in range(0, 400, 10):
   for x in range(0, 400, 10):
      setColor(getRandomX11Color())
      move(x + 5, y + 5)
      fillRectangle(10, 10)
      delay(1)    

