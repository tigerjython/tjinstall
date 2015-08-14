from gpanel import *
makeGPanel(0, 100, 0, 100)

KEY_ESCAPE = 27
KEY_LEFT = 37
KEY_RIGHT = 39
KEY_UP = 38
KEY_DOWN = 40


def drawCircle():
   move(x, y)
   setColor("green")
   fillCircle(5)
   setColor("black")
   circle(5)
   

text("Bewege den Kreis mit Cursortasten.")
x = 50
y = 50
drawCircle();
 
while True:
   key = getKeyCodeWait()
   if key == KEY_ESCAPE:
      break
   elif key == KEY_LEFT:
      x -= 1
      drawCircle()
   elif key == KEY_RIGHT:
      x += 1
      drawCircle()
   elif key == KEY_UP:
      y += 1
      drawCircle()
   elif key == KEY_DOWN:
      y -= 1
      drawCircle()      
dispose()
