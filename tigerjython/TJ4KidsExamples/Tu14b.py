from gturtle import *

makeTurtle()
hideTurtle()
setPos(200, 0)
left(90)
wrap()
enableRepaint(False)

i = 0
while True:
    clear()
    drawImage("sprites/pony_" + str(i) + ".gif")
    repaint()
    delay(60)
    forward(5)
    i += 1
    if i == 7:
        i = 0
         
