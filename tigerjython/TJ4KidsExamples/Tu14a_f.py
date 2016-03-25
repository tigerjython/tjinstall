from gturtle import *

def propeller(a):
    setHeading(a)
    repeat 3:
        fillToPoint()    
        rightArc(100, 90)
        right(90)
        rightArc(100, 90)
        left(30)       
    
makeTurtle()
hideTurtle()
# kein automatisches Rendering
enableRepaint(False)

dt = 40  # Zeitinkrement (ms)
a = 0    # Winkelinitialisierung
da = 10  # Winkelinkrement (Grad)

# Animationsschleife
while True:
   propeller(a)
   repaint()     # Rendern
   delay(dt)     # Warten
   clear("gray") # Löschen
   a += da       # Neue Lage
