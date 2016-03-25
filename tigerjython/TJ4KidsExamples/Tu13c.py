from gturtle import *

makeTurtle()
repeat:
    s = inputString("Gib einen Turtlebefehl ein")
    try:
        exec(s)
    except:
        msgDlg("Illegale Eingabe")
