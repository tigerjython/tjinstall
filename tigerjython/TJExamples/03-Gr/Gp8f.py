from gpanel import *

def updateGraphics():
   # erase all
   clear()
 
   # draw points
   lineWidth(1)
   for i in range(4):
      move(points[i])
      if active == i:
         setColor("green")
         fillCircle(2)
      setColor("black")
      circle(2)

   # draw tangents
   setColor("red")
   line(points[0], points[1])
   line(points[3], points[2])

   # draw Bezier curve
   setColor("blue")
   lineWidth(3)
   cubicBezier(points[0], points[1], points[2], points[3])

def onMouseDragged(x, y):
   if active == -1:
      return
   points[active][0] = x
   points[active][1] = y
   updateGraphics()

def onMouseReleased(x, y):
   active = -1
   updateGraphics()

def onMouseMoved(x, y):
   global active   
   active = near(x, y)
   updateGraphics()

def near(x, y):
   for i in range(4):
      rsquare = (x - points[i][0]) * (x - points[i][0]) + (y - points[i][1]) * (y - points[i][1])
      if rsquare < 4:
         return i
   return -1      

pt1 = [20, 20]
pc1 = [10, 80]
pc2 = [90, 80]
pt2 = [80, 20]
points = [pt1, pc1, pc2, pt2]
active = -1

makeGPanel(0, 100, 0, 100,
           mouseDragged = onMouseDragged,
           mouseReleased = onMouseReleased,
           mouseMoved = onMouseMoved)
updateGraphics()
