from gpanel import *

makeGPanel(-20, 20, 0, 40)

for i in range(-20, 21):
    if i < 0:
        setColor("red")
    else:
        setColor("green")    
    line(i, 0, 0, 40)
