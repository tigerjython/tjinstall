from gpanel import *

makeGPanel(-10, 10, -10, 10)

xA = 0
yA = 0
xA_alias = xA
yA_alias = yA
xB = 0
yB = 5
xC = 5
yC = 0

fillTriangle(xA, yA, xB, yB, xC, yC)
xA = 1
setColor("green")
fillTriangle(xA_alias, yA_alias, xB, yB, xC, yC)

