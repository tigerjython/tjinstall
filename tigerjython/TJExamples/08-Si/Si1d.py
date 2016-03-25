from gpanel import *
import random

n = 10000
p = 0.48

def istMaedchen():
# True: Mädchen, False: Knabe
    r = random.random()
    if r < p:
       return True
    return False

def familie():
    nbMaedchen = 0
    repeat 4:
        if istMaedchen():
            nbMaedchen += 1
    hMaedchen[nbMaedchen] += 1

def drawAxes():
    text(2500, 0, "2500")
    line(2500, 0, 3000, 0)
    text("3000")
    line(2500, 0, 2500, 50)
    text("50")

def versuchsreihe():
    global hMaedchen
    hMaedchen = [0] * 5
    repeat n:
        familie()
    return hMaedchen[1]

t = [0] * 10001
makeGPanel(2450, 3050, -5, 55)
drawAxes()
         
for i in range(1000):
    z = versuchsreihe()
    t[z] += 1
    line(z, 0, z, t[z])

a = 0
for i in range(10001):
    a += i * t[i]
avg = int(a / 1000)
lineWidth(4)
setColor("red")
line(avg, 0, avg, 40) 
text(avg, -2, str(avg))       

setColor("green")
line(2800, 0, 2800, 30) 
text(2800, -2, "2800")       
