from gamegrid import *

# ---------------- class MyMouseTouchListener ------------
class MyMouseTouchListener(GGMouseTouchListener):
    def mouseTouched(self, actor, mouse, spot):
        global touchedActor, hotSpot
        event = mouse.getEvent()
        if event == GGMouse.lPress:
            touchedActor = actor
            touchedActor.setOnTop()
            hotSpot = spot
        elif event == GGMouse.lRelease:
            touchedActor.setLocationOffset(Point(0, 0))
            touchedActor = None
        refresh()

def dragCallback(e):
    if touchedActor == None:
        return
    pt = Point(e.getX() - hotSpot.x, e.getY() - hotSpot.y)
    touchedActor.setPixelLocation(pt)
    refresh()

makeGameGrid(5, 5, 100, Color.red, False, mouseDragged = dragCallback)
setBgColor(Color.gray)
setTitle("Drag Actors!")
for i in range(4):
    nemo = Actor("sprites/car" + str(i) + ".gif")
    addActor(nemo, getRandomEmptyLocation())
    nemo.addMouseTouchListener(MyMouseTouchListener(), 
    GGMouse.lPress | GGMouse.lRelease, True)
show()
