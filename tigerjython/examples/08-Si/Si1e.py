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
    text("2500")
    line(0, 0, 500, 0)
    text("3000")
    line(0, 0, 0, 50)
    text("50")

def versuchsreihe():
    global hMaedchen
    hMaedchen = [0] * 5
    repeat n:
        familie()
    return hMaedchen[1]

t = [0] * 501
makeGPanel(-50, 550, -5, 55)
drawAxes()
         
for i in range(1000):
    z = versuchsreihe()
    index = z - 2500
    if index >= 0 and index <= 500:
        t[index] += 1
    line(index, 0, index, t[index])

a = 0
for i in range(501):
    a += (2500 + i) * t[i]

avg = int(a / 1000)
avgIndex = avg - 2500
lineWidth(4)
setColor("red")
line(avgIndex, 0, avgIndex, 40) 
text(avgIndex, -2, str(avg))

b = 0
for s in range(250):
    b += t[s + avgIndex]
    if b > 350:
        break
print s

setColor("green")
line(avgIndex + s, 0, avgIndex + s, 30) 
text(avgIndex + s, -2, str(avg + s))
line(avgIndex - s, 0, avgIndex - s, 30) 
text(avgIndex - s, -2, str(avg - s))
 

       
