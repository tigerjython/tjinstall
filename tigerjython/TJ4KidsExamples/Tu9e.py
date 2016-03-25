from gturtle import *

n = inputInt("Welches Auto (1, 2, 3)")
if n == 1:
    makeTurtle("sprites/car0.png")
elif n == 2:
    makeTurtle("sprites/car1.png")
elif n == 3:
    makeTurtle("sprites/car2.png")
else:
    msgDlg("Illegale Eingabe") 

if n > 0 and n < 4:
    rightCircle(100)
