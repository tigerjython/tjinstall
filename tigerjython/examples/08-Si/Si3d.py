# Si3d.py
# Chi-Quadrat / Zufriedenheit Frau-Mann kombiniert

from gpanel import *
import random

n = 1000 # Totale Anzahl (Frauen + Männer)

def drawGrid(xmax, ymax):
    # Horizontal
    for i in range(11):
        y = ymax / 10 * i
        line(0, y, xmax, y)
        text(0, y, str(y))
    # Vertical
    for k in range(11):
        x = xmax / 10 * k
        line(x, 0, x, ymax)
        text(x, -0.05 * ymax, str(x / 10))

def showSpreading():
    sum = 0
    for i in range(len(h)):
        sum += h[i]
        if sum > 9500: 
            break
    setColor("green")        
    lineWidth(2)
    line(i, 0, i, 1000)
    text(i, -100, str(i /  10))
    return i
     
def showDistribution():
    setColor("blue")
    lineWidth(4)
    for i in range(max):
        line(i, 0, i, h[i])

def chisquare(m, f):
    u1 = n / 2 * p
    u2 = n / 2 * (1 - p)
    chisquare = \
         (m[0] - u1) * (m[0] - u1) / u1 \
       + (f[0] - u1) * (f[0] - u1) / u1 \
       + (m[1] - u2) * (m[1] - u2) / u2 \
       + (f[1] - u2) * (f[1] - u2) / u2
    return chisquare

def sim():
    # men's simulation
    m = [0] * 2
    for i in range((n / 2) + 1):
        t = random.random()
        if t < p:
           m[0] += 1
        else:
           m[1] += 1

    # womens's simulation
    f = [0] * 2
    for i in range((n / 2) + 1):
        t = random.random()
        if t < p:
           f[0] += 1
        else:
           f[1] += 1
    return chisquare(m, f)

#ma = [60, 440] # sum = n / 2
#fr = [80, 420] # sum = n / 2
ma = [155, 345]
fr = [180, 320]
#ma = [65, 435] 
#fr = [80, 420]
#ma = [250, 250] 
#fr = [250, 250]
p = (ma[0] + fr[0]) / n
print "Zustimmungswahrscheinlichkeit:",  p

max = 100
makeGPanel(-0.1 * max, 1.1 * max, -100, 1100)
title("Chi-Quadrat Test bei Zufriedenheit-Mann-Frau")
drawGrid(max, 1000)
h = [0] * max

#print sim()

repeat 10000:
    c = int(10 * sim())
    if c < max:
        h[c] += 1

showDistribution()
s = showSpreading()

# Observed data
c = chisquare(ma, fr)
if c <= s / 10:
   print "Same:", c
else:
   print "Different:", c

a = ma[0]
b = fr[0]
c = ma[1]
d = fr[1]

g = n * (a * d - b * c) * (a * d - b * c) / ((a + b) * (a + c) * (c + d) * (b + d))
print "Prüfgrösse:", g  
