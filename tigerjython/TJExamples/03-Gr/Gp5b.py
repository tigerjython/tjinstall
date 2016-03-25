from gpanel import *
import time

def step():
   global x
   global v
   clear()
   lineWidth(5)
   move(25, 300)
   rectangle(50, 100)
   move(575, 300)
   rectangle(50, 100)
   x = x + v
   image("_sprites/football.gif", x, 275)
   if x > 500 or x < 50:
      v = -v

makeGPanel(0, 600, 0, 600)
bgColor("forestgreen")
enableRepaint(False)

x = 300
v = 10

while True:
   startTime = time.clock()
   step()
   repaint()
   while (time.clock() - startTime)  < 0.020:
      delay(1)

