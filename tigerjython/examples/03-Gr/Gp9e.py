from gpanel import *

def drawGraph():
   clear()
   for i in range(len(graph)):
      move(graph[i]) 
      if i == iNode:
         setColor("red")
      else:
         setColor("green")           
      fillCircle(2)
  
   setColor("blue")
   for i in range(len(graph)):
      for k in range(i, len(graph)):
         line(graph[i], graph[k])

def onMousePressed(e):
   global iNode
   x = toWindowX(e.getX())
   y = toWindowY(e.getY())
   if isLeftMouseButton(e):
      iNode = near(x, y)
   if isRightMouseButton(e):
      index = near(x, y)
      if index != -1:
         graph.pop(index)
         iNode = -1
      else:
         pt = [x, y]
         graph.append(pt)
   drawGraph()

def onMouseDragged(e):
   if isLeftMouseButton(e):
      if iNode == -1:
         return
      x = toWindowX(e.getX())
      y = toWindowY(e.getY())
      graph[iNode] = [x, y]
      drawGraph()

def onMouseReleased(e):
   global iNode
   if isLeftMouseButton(e):
      iNode = -1
      drawGraph()

def near(x, y):
   for i in range(len(graph)):
      p = graph[i]
      d = (p[0] - x) * (p[0] - x) + (p[1] - y) * (p[1] - y)
      if  d < 10:
         return i
   return -1

graph = []
iNode = -1
makeGPanel(0, 100, 0, 100, 
           mousePressed = onMousePressed, 
           mouseDragged = onMouseDragged,
           mouseReleased = onMouseReleased)
