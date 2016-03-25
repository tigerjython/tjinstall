# Tu14a.py

from gturtle import *

def dreieck():
    startPath()
    repeat 3:
        forward(50)
        right(120)
    fillPath()
     
def propeller(x, y, a):
    setPos(x, y)
    heading(a)
    repeat 4:
        dreieck()
        right(90)

def flugzeug(x, y):
   heading(0)
   setPos(x, y)
   drawImage("sprites/airplane.png")

makeTurtle()
hideTurtle()
# kein automatisches Rendering
enableRepaint(False)

dt = 40  # Zeitinkrement
a = 0    # Winkelinitialisierung
da = 10   # Winkelinkrement

# Animationsschleife
while True:
   propeller(0, 0, a)
   repaint()     # Rendern
   delay(dt)     # Warten
   clear("gray") # Löschen
   flugzeug(0, 60)
   a += da       # Neue Lage
    