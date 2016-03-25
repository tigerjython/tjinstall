from gturtle import *

makeTurtle()
repeat:
    s = inputString("Gib einen Turtlebefehl ein:")
    exec(s)
