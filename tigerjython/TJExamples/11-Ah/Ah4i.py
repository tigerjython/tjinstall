# Ah4i.py

from gpanel import *
from javax.swing import *
import math
import thread

def rho(phi):
    return math.sin(n * phi)

def onButtonClick(e):
    global n
    enableGui(False)
    if e.getSource() == btn1:
        n = math.e
    elif e.getSource() == btn2:
        n = math.pi
#    drawRhodonea()    
    thread.start_new_thread(drawRhodonea, ())

def drawRhodonea():
    clear()
    phi = 0
    while phi < nbTurns * math.pi:
        r = rho(phi)
        x = r * math.cos(phi)    
        y = r * math.sin(phi)    
        if phi == 0:
          move(x, y)
        else:
          draw(x, y)
        phi += dphi
    enableGui(True)

def enableGui(enable):
    btn1.setEnabled(enable)
    btn2.setEnabled(enable)
                    
dphi = 0.01
nbTurns = 100
makeGPanel(-1.2, 1.2, -1.2, 1.2)
btn1 = JButton("Go (e)", actionListener = onButtonClick)
btn2 = JButton("Go (pi)", actionListener = onButtonClick)
addComponent(btn1)
addComponent(btn2)
validate()
