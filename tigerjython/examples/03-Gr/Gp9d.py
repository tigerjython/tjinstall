from gpanel import *

def drawGraph():
   clear()
   for pt in graph:
      move(pt) 
      fillCircle(2)
   
   for i in range(len(graph)):
      for k in range(i, len(graph)):
         line(graph[i], graph[k])

def onMousePressed(e):
   x = toWindowX(e.getX())
   y = toWindowY(e.getY())
   pt = [x, y]
   graph.append(pt)
   drawGraph()

graph = []
makeGPanel(0, 100, 0, 100, mousePressed = onMousePressed)
