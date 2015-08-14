from gpanel import *
import random
from javax.swing import JTextField, JLabel, JButton

def actionCallback(e):
   wakeUp()
   
def createGUI():
   addComponent(lbl1)
   addComponent(tf1)
   addComponent(btn1)
   addComponent(lbl2)
   addComponent(tf2)
   validate()

def init():
   tf2.setText("")
   clear()
   move(0.5, 0.5)
   rectangle(1, 1)
   move(0, 0)
   arc(1, 0, 90)

def doIt(n):
   hits = 0
   for i in range(n):
      zx = random.random()
      zy = random.random()
      if zx * zx + zy * zy < 1:
         hits = hits + 1
         setColor("red")
      else:
         setColor("green")
      point(zx, zy)
   return hits

lbl1 = JLabel("Number of drops: ")
lbl2 = JLabel("          PI = ")
tf1 = JTextField(6)
tf2 = JTextField(10)
btn1 = JButton("OK", actionListener = actionCallback)

makeGPanel("Monte Carlo Simulation", -0.1, 1.1, -0.1, 1.1)
createGUI()
tf1.setText("10000")
init()

while True:
   putSleep()
   init()
   n = int(tf1.getText())
   k = doIt(n)
   pi =  4 * k / n
   tf2.setText(str(pi))

