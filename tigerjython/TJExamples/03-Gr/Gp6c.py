from gpanel import *
import time

KEY_S = 83
KEY_F = 70

makeGPanel(0, 600, 0, 600)
title("Key 'f': faster, 's': slower")

enableRepaint(False)
x = 300
y = 300
v = 10
vmax = 50
isAhead = True

while True:
   startTime = time.clock()

   if kbhit():
      key = getKeyCode()
      if key == KEY_F:
         if v < vmax:
           v += 1
      elif key == KEY_S:
         if v > 0:
           v -= 1
   
   clear()
   setColor("black")
   text(10, 10, "Speed: " + str(v))
   if isAhead:
      x = x + v
   else:
      x = x - v
   move(x, y)
   setColor("red")
   fillCircle(20)
   repaint()
   if x > 600 or x < 0:
      isAhead = not isAhead
   while (time.clock() - startTime)  < 0.010:
      delay(1)
